import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def simulate_cosmic_history():
    print("--- INICIANDO SIMULACIÓN COSMOLÓGICA FLRW (Fase 2.2) ---")
    
    # 1. PARÁMETROS DEL MODELO (Unidades Normalizadas)
    # ------------------------------------------------
    # H0 = 1 (Tiempo medido en unidades de tiempo de Hubble ~ 14 Gyr)
    # Densidades actuales (Omega)
    Om_r0 = 1e-4   # Radiación
    Om_m0 = 0.3    # Materia (Bariónica + Oscura aparente)
    # Om_psi0 se ajustará para que la suma sea 1 (Universo plano)
    
    # Parámetros del Potencial V = alpha*psi^2 + beta*psi^4 + V_shift
    # alpha < 0 para sombrero mexicano
    # Ajustamos V_shift para que el mínimo del potencial sea positivo (Energía Oscura observada)
    
    alpha = -10.0  # Parámetro de masa (controla la curvatura del potencial)
    beta = 10.0    # Parámetro de auto-interacción
    
    # El mínimo está en psi_min^2 = -alpha / (2*beta)
    psi_min = np.sqrt(-alpha / (2*beta))
    V_min_raw = alpha * psi_min**2 + beta * psi_min**4
    
    # Queremos que en el mínimo, rho_vac sea ~ 0.7 (Energía Oscura actual)
    target_DE = 0.7
    V_shift = target_DE - V_min_raw
    
    def Potential(psi):
        return alpha * psi**2 + beta * psi**4 + V_shift

    def dV_dpsi(psi):
        return 2 * alpha * psi + 4 * beta * psi**3

    # 2. ECUACIONES DIFERENCIALES (Sistema Acoplado)
    # ----------------------------------------------
    # Variables: y = [a, psi, dpsi_dt]
    # Tiempo t: Tiempo cósmico
    
    def cosmic_dynamics(y, t):
        a, psi, pi = y # pi = dpsi/dt
        
        # Evitar singularidad en t=0
        if a <= 1e-5: a = 1e-5
        
        # Densidades de fluidos estándar
        rho_r = Om_r0 / a**4
        rho_m = Om_m0 / a**3
        
        # Densidad y Presión del Fondo Dinámico
        rho_psi = 0.5 * pi**2 + Potential(psi)
        P_psi   = 0.5 * pi**2 - Potential(psi)
        
        # Ecuación de Friedmann (H^2 = 8piG/3 * rho_total)
        # En unidades normalizadas: H^2 = rho_total
        rho_total = rho_r + rho_m + rho_psi
        H = np.sqrt(np.abs(rho_total))
        
        # Ecuaciones de Movimiento
        dadt = a * H
        dpsidt = pi
        # Klein-Gordon: d2psi + 3H dpsi + V' = 0
        dpidt = -3 * H * pi - dV_dpsi(psi)
        
        return [dadt, dpsidt, dpidt]

    # 3. CONDICIONES INICIALES (Universo Temprano z ~ 1000)
    # -----------------------------------------------------
    # Empezamos desplazados del mínimo (Thawing Quintessence)
    # Si empezamos exactamente en el mínimo, w = -1 siempre.
    # Desplazamos psi un poco para ver dinámica.
    
    psi_init = 0.1 # Lejos del mínimo (que es ~0.7)
    pi_init = 0.0  # Quieto inicialmente (congelado por fricción de Hubble alta)
    a_init = 1e-4  # z = 10000
    
    y0 = [a_init, psi_init, pi_init]
    t = np.linspace(0, 1.5, 1000) # 1.5 tiempos de Hubble (pasado y futuro cercano)
    
    # Integración
    sol = odeint(cosmic_dynamics, y0, t)
    
    a = sol[:, 0]
    psi = sol[:, 1]
    pi = sol[:, 2]
    
    # 4. ANÁLISIS DE RESULTADOS (Post-Procesado)
    # ------------------------------------------
    # Recalculamos H, rho, w para graficar
    
    rho_r = Om_r0 / a**4
    rho_m = Om_m0 / a**3
    rho_psi = 0.5 * pi**2 + Potential(psi)
    P_psi = 0.5 * pi**2 - Potential(psi)
    
    w_psi = P_psi / rho_psi
    
    # Redshift z = 1/a - 1
    z = 1/a - 1
    
    # Filtrar para gráfico (z < 10)
    mask = (z < 5) & (z > -0.5)
    
    # 5. VISUALIZACIÓN
    # ----------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Gráfico 1: Evolución de Densidades (Omega)
    rho_tot = rho_r + rho_m + rho_psi
    ax1.plot(z[mask], (rho_m/rho_tot)[mask], label=r'Materia ($\Omega_m$)', color='blue')
    ax1.plot(z[mask], (rho_psi/rho_tot)[mask], label=r'Fondo Dinámico ($\Omega_\Psi$)', color='red', linewidth=2)
    ax1.plot(z[mask], (rho_r/rho_tot)[mask], label=r'Radiación ($\Omega_r$)', color='orange', linestyle='--')
    
    ax1.set_xlim(5, -0.5) # Eje invertido (Pasado -> Futuro)
    ax1.set_xlabel('Redshift (z)')
    ax1.set_ylabel('Parámetro de Densidad ($\Omega$)')
    ax1.set_title('Historia Cósmica: La Era del Fondo Dinámico')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfico 2: Ecuación de Estado w(z)
    ax2.plot(z[mask], w_psi[mask], color='purple', linewidth=2)
    ax2.axhline(-1, color='black', linestyle='--', label='Constante Cosmológica ($w=-1$)')
    ax2.axhline(-1/3, color='gray', linestyle=':', label='Límite de Aceleración')
    
    ax2.set_xlim(5, -0.5)
    ax2.set_ylim(-1.2, 1.0)
    ax2.set_xlabel('Redshift (z)')
    ax2.set_ylabel('Ecuación de Estado ($w$)')
    ax2.set_title('Dinámica de la Energía Oscura ($w(z)$)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Detectar Phantom Crossing
    if np.any(w_psi < -1):
        print("ALERTA: Se detectó cruce al régimen Phantom (w < -1).")
    
    plt.tight_layout()
    plt.show()

simulate_cosmic_history()