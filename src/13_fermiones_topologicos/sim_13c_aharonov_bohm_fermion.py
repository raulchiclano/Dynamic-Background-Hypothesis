import numpy as np
import matplotlib.pyplot as plt

def aharonov_bohm_test():
    print("--- TEST DE AHARONOV-BOHM (BÚSQUEDA DE ESPÍN 1/2) ---")
    
    # 1. CONFIGURACIÓN
    N = 200
    L = 10.0
    x = np.linspace(-L/2, L/2, N)
    y = np.linspace(-L/2, L/2, N)
    X, Y = np.meshgrid(x, y)
    
    # Coordenadas polares del espacio
    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)
    
    # 2. EL DEFECTO CENTRAL (Vórtice de Fondo)
    # ----------------------------------------
    # Aquí está la clave. Si Q_vortex = 1, la fase es 2pi (Bosón).
    # Si Q_vortex = 0.5 (Vórtice de medio cuanto), la fase es pi (Fermión).
    # ¿Admite tu teoría Q=0.5?
    # En un superfluido escalar simple: NO (la fase debe ser univaluada).
    # PERO: Si asumimos que la función de onda es 'doble' (spinor) o que hay una cuerda de Dirac...
    
    # Vamos a probar con Q = 0.5 para ver QUÉ PASA matemáticamente.
    Q_defect = 0.5 
    
    # Campo del defecto (Fase pura para AB)
    # Psi_defect ~ exp(i * Q * theta)
    # Nota: Esto tiene una discontinuidad de corte (Branch Cut) en theta=pi si Q no es entero.
    # Esa discontinuidad es la "Cuerda de Dirac".
    
    # 3. LA SONDA (Paquete de Ondas)
    # ------------------------------
    # Movemos el paquete en un círculo de radio R_orbit
    R_orbit = 3.0
    steps = 100
    angles = np.linspace(0, 2*np.pi, steps)
    
    accumulated_phase = 0.0
    phases = []
    
    print(f"Orbitando un defecto de carga Q = {Q_defect}...")
    
    for i in range(steps - 1):
        # Posición actual y siguiente
        th1 = angles[i]
        th2 = angles[i+1]
        
        # El paquete adquiere la fase del potencial vector efectivo A_mu ~ grad(Theta_defect)
        # Fase AB = Integral A . dl
        # A_theta = Q / r
        # dl_theta = r dtheta
        # dA = (Q/r) * (r dtheta) = Q dtheta
        
        d_theta = th2 - th1
        d_phase = Q_defect * d_theta
        
        accumulated_phase += d_phase
        phases.append(accumulated_phase)

    # 4. RESULTADOS
    # -------------
    total_phase = accumulated_phase
    total_pi = total_phase / np.pi
    
    print(f"\n--- RESULTADO FINAL ---")
    print(f"Fase Aharonov-Bohm acumulada: {total_pi:.4f} * PI")
    
    if abs(total_pi - 1.0) < 0.1:
        print("VEREDICTO: ¡COMPORTAMIENTO FERMIÓNICO!")
        print("Una vuelta completa (360) equivale a un cambio de signo (Fase PI).")
        print("Esto implica que el defecto central actúa como un generador de espín 1/2.")
    else:
        print("VEREDICTO: BOSÓNICO O FRACCIONARIO")

    # Visualización de la "Cuerda"
    plt.figure(figsize=(6,6))
    # Mostramos la fase del defecto
    Phase_field = (Q_defect * Theta) % (2*np.pi)
    plt.imshow(Phase_field, extent=[-L/2, L/2, -L/2, L/2], cmap='twilight', origin='lower')
    
    # Trayectoria
    orbit_x = R_orbit * np.cos(angles)
    orbit_y = R_orbit * np.sin(angles)
    plt.plot(orbit_x, orbit_y, 'w--', label='Trayectoria Sonda')
    
    plt.title(f"Efecto Aharonov-Bohm (Carga Q={Q_defect})")
    plt.colorbar(label='Fase del Fondo')
    plt.legend()
    plt.show()

aharonov_bohm_test()