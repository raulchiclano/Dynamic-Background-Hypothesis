import numpy as np
import matplotlib.pyplot as plt

def hopfion_spin_test():
    print("--- TAREA 1: TEST DE ESPÍN DEL HOPFIÓN (FASE DE BERRY) ---")
    
    # 1. CONFIGURACIÓN DE LA REJILLA
    # ------------------------------
    N = 64
    L = 8.0
    x = np.linspace(-L/2, L/2, N)
    y = np.linspace(-L/2, L/2, N)
    z = np.linspace(-L/2, L/2, N)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    
    # Elemento de volumen para integración
    dV = (L/N)**3

    # 2. DEFINICIÓN DEL HOPFIÓN ROTADO
    # --------------------------------
    # Usamos el mapa de Hopf estándar proyectado en R3
    # Q = Carga topológica (Linking number)
    
    def get_hopfion(angle_z):
        # Rotamos las coordenadas X, Y alrededor de Z
        # x' = x cos(a) - y sin(a)
        # y' = x sin(a) + y cos(a)
        
        c, s = np.cos(angle_z), np.sin(angle_z)
        Xr = X * c - Y * s
        Yr = X * s + Y * c
        Zr = Z
        
        R_sq = Xr**2 + Yr**2 + Zr**2
        
        # Mapa de Hopf (Q=1)
        # Psi ~ (2(x + iy)) / (2z + i(r^2 - 1))
        Numerator = 2 * (Xr + 1j * Yr)
        Denominator = 2 * Zr + 1j * (R_sq - 1.0)
        
        # Campo crudo
        Psi_raw = Numerator / Denominator
        
        # Aplicamos perfil de densidad para que sea físico (confinado)
        # Sin esto, la integral diverge o da ruido en los bordes
        Mag = np.abs(Psi_raw)
        # Perfil suave que va a 0 en el infinito y en el núcleo
        Density = (Mag**2) / ((1 + Mag**2)**2) 
        
        # Reconstruimos Psi normalizada
        Psi = np.sqrt(Density) * np.exp(1j * np.angle(Psi_raw))
        
        # Normalizar la función de onda total a 1
        Norm = np.sqrt(np.sum(np.abs(Psi)**2) * dV)
        return Psi / Norm

    # 3. BUCLE DE ROTACIÓN ADIABÁTICA
    # -------------------------------
    print("Iniciando rotación de 0 a 360 grados...")
    
    steps = 100
    angles = np.linspace(0, 2*np.pi, steps)
    berry_phase_accum = 0.0
    phases = []
    
    # Estado inicial
    Psi_current = get_hopfion(angles[0])
    
    for i in range(1, steps):
        # Estado siguiente rotado
        Psi_next = get_hopfion(angles[i])
        
        # Calcular solapamiento (Overlap) <Psi(t)|Psi(t+dt)>
        # Esto nos da el cambio de fase relativo
        overlap = np.sum(np.conj(Psi_current) * Psi_next) * dV
        
        # Extraer el ángulo del número complejo resultante
        # overlap = |overlap| * e^(i * d_theta)
        d_phase = np.angle(overlap)
        
        # Acumular
        berry_phase_accum += d_phase
        phases.append(berry_phase_accum)
        
        # Actualizar
        Psi_current = Psi_next

    # 4. RESULTADOS
    # -------------
    total_phase = berry_phase_accum
    total_phase_pi = total_phase / np.pi
    
    print(f"\n--- RESULTADO FINAL ---")
    print(f"Fase acumulada tras 360 grados: {total_phase:.4f} radianes")
    print(f"En unidades de PI: {total_phase_pi:.4f} * PI")
    
    # Clasificación
    # Tolerancia numérica pequeña
    tol = 0.1
    
    if abs(total_phase_pi - 2.0) < tol or abs(total_phase_pi) < tol:
        print("VEREDICTO: BOSÓN (Espín entero, 0 o 1)")
        print("La función de onda volvió a su signo original (+).")
    elif abs(total_phase_pi - 1.0) < tol or abs(total_phase_pi - 3.0) < tol:
        print("VEREDICTO: FERMIÓN (Espín 1/2)")
        print("La función de onda cambió de signo (-). ¡Éxito Topológico!")
    else:
        print("VEREDICTO: ANYON / FRACCIONARIO (Resultado complejo)")

    # 5. GRÁFICA
    # ----------
    plt.figure(figsize=(8, 5))
    plt.plot(np.degrees(angles[1:]), np.array(phases) / np.pi, label='Fase Acumulada', linewidth=2)
    
    # Líneas de referencia
    plt.axhline(1.0, color='r', linestyle='--', label='Fermión (1 PI)')
    plt.axhline(2.0, color='g', linestyle='--', label='Bosón (2 PI)')
    
    plt.xlabel('Ángulo de Rotación (Grados)')
    plt.ylabel(r'Fase de Berry ($\times \pi$)')
    plt.title('Test de Estadística de Espín: ¿Bosón o Fermión?')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

hopfion_spin_test()