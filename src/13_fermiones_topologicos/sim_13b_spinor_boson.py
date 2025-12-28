import numpy as np
import matplotlib.pyplot as plt

def spinor_berry_phase():
    print("--- ÚLTIMA BALA: TEST DE ESPÍN EN CONDENSADO ESPINORIAL ---")
    
    # 1. CONFIGURACIÓN
    N = 100
    L = 10.0
    x = np.linspace(-L/2, L/2, N)
    y = np.linspace(-L/2, L/2, N)
    X, Y = np.meshgrid(x, y)
    
    # Coordenadas polares
    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)
    
    # 2. DEFINICIÓN DEL DEFECTO ESPINORIAL (HQV - Alice String)
    # ---------------------------------------------------------
    # Un vórtice donde el espinor rota pi al dar una vuelta completa.
    # Psi = [ cos(theta/2), sin(theta/2) * e^(i*phase) ] ?
    # No, la forma canónica de un espinor 1/2 es:
    # Psi(r, theta) = e^(i theta / 2) * [ 1, 0 ] (en un marco rotante)
    
    # Vamos a simular la rotación física del objeto entero.
    
    def get_spinor_defect(angle_rot_z):
        # Rotamos las coordenadas físicas
        Xr = X * np.cos(angle_rot_z) - Y * np.sin(angle_rot_z)
        Yr = X * np.sin(angle_rot_z) + Y * np.cos(angle_rot_z)
        Tr = np.arctan2(Yr, Xr)
        
        # Definición del Espinor (Vórtice de medio entero)
        # Componente 1: Vórtice carga 1
        # Componente 2: Vórtice carga 0
        # Esto crea una textura de espín no trivial.
        
        # Perfil de densidad (núcleo)
        Rr = np.sqrt(Xr**2 + Yr**2)
        Core = np.tanh(Rr)
        
        # Espinor base (Textura de Skyrmion 2D o Meron)
        # Psi_up   = cos(alpha/2)
        # Psi_down = sin(alpha/2) * e^(i*beta)
        # Donde alpha(r) va de 0 a pi, y beta = theta.
        
        # Perfil de ángulo polar (Skyrmion)
        # alpha(0) = 0 (Spin UP en el centro)
        # alpha(inf) = pi (Spin DOWN en el infinito)
        alpha_r = np.pi * np.tanh(Rr/2.0)
        
        psi_up = np.cos(alpha_r / 2.0)
        psi_down = np.sin(alpha_r / 2.0) * np.exp(1j * Tr)
        
        # Normalización local
        norm = np.sqrt(np.abs(psi_up)**2 + np.abs(psi_down)**2)
        psi_up /= norm
        psi_down /= norm
        
        return psi_up, psi_down

    # 3. CÁLCULO DE FASE DE BERRY
    # ---------------------------
    print("Rotando el Skyrmion/Espinor 360 grados...")
    
    steps = 100
    angles = np.linspace(0, 2*np.pi, steps)
    accum_phase = 0.0
    phases_plot = []
    
    # Estado inicial
    u_curr, d_curr = get_spinor_defect(angles[0])
    
    for i in range(1, steps):
        u_next, d_next = get_spinor_defect(angles[i])
        
        # Producto interno (Overlap) para espinores
        # <Psi1 | Psi2> = sum( u1* u2 + d1* d2 )
        overlap = np.sum(np.conj(u_curr)*u_next + np.conj(d_curr)*d_next)
        
        d_phase = np.angle(overlap)
        accum_phase += d_phase
        phases_plot.append(accum_phase)
        
        u_curr, d_curr = u_next, d_next

    # 4. RESULTADOS
    # -------------
    total_pi = accum_phase / np.pi
    print(f"\n--- RESULTADO FINAL (ESPINOR) ---")
    print(f"Fase acumulada: {total_pi:.4f} * PI")
    
    if abs(total_pi - 1.0) < 0.1 or abs(total_pi + 1.0) < 0.1:
        print("VEREDICTO: ¡FERMIÓN CONFIRMADO! (Espín 1/2)")
        print("El defecto topológico se comporta como un electrón.")
    elif abs(total_pi - 2.0) < 0.1:
        print("VEREDICTO: BOSÓN (Espín 1)")
    else:
        print(f"VEREDICTO: FASE EXÓTICA ({total_pi:.2f} PI)")

    plt.plot(np.degrees(angles[1:]), np.array(phases_plot)/np.pi)
    plt.axhline(1, color='r', linestyle='--', label='Fermión')
    plt.axhline(2, color='g', linestyle='--', label='Bosón')
    plt.legend()
    plt.title("Fase de Berry de un Defecto Espinorial")
    plt.xlabel("Ángulo de Rotación")
    plt.ylabel("Fase / PI")
    plt.grid(True, alpha=0.3)
    plt.show()

spinor_berry_phase()