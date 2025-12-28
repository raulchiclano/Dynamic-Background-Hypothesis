import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def parameter_space_scan():
    print("--- ESCANEO DE ESPACIO DE PARÁMETROS (Fase 2.2 Refinada) ---")
    
    # 1. CONFIGURACIÓN DEL BARRIDO
    # ----------------------------
    # Variamos alpha (curvatura del potencial) y psi_init (desplazamiento inicial)
    # Beta se fija porque solo escala la amplitud global, no la forma dinámica relativa.
    
    alphas = np.linspace(-20, -5, 15)  # Rango de masas (negativas para sombrero mexicano)
    psi_inits = np.linspace(0.01, 0.5, 15) # Desplazamiento desde el origen
    beta = 10.0
    
    # Almacenamiento de resultados
    results_w0 = np.zeros((len(alphas), len(psi_inits)))
    results_wa = np.zeros((len(alphas), len(psi_inits)))
    
    # 2. BUCLE DE SIMULACIÓN
    # ----------------------
    print(f"Simulando {len(alphas)*len(psi_inits)} universos...")
    
    for i, alpha in enumerate(alphas):
        for j, psi0 in enumerate(psi_inits):
            
            # Configuración del Potencial para este universo
            psi_min = np.sqrt(-alpha / (2*beta))
            V_min_raw = alpha * psi_min**2 + beta * psi_min**4
            target_DE = 0.7
            V_shift = target_DE - V_min_raw
            
            def Potential(p): return alpha * p**2 + beta * p**4 + V_shift
            def dV_dpsi(p): return 2 * alpha * p + 4 * beta * p**3
            
            # Dinámica
            def dynamics(y, t):
                a, psi, pi = y
                if a < 1e-5: a = 1e-5
                rho_r = 1e-4 / a**4
                rho_m = 0.3 / a**3
                rho_psi = 0.5 * pi**2 + Potential(psi)
                H = np.sqrt(rho_r + rho_m + rho_psi)
                return [a*H, pi, -3*H*pi - dV_dpsi(psi)]
            
            # Integrar hasta hoy (t ~ 1.0 en unidades Hubble)
            # Empezamos en z=1000 (a=1e-3)
            y0 = [1e-3, psi0, 0.0]
            t = np.linspace(0, 1.0, 200)
            sol = odeint(dynamics, y0, t)
            
            # Extraer valores HOY (último paso)
            a_now = sol[-1, 0]
            psi_now = sol[-1, 1]
            pi_now = sol[-1, 2]
            
            # Calcular w(z) hoy (z=0)
            rho_now = 0.5 * pi_now**2 + Potential(psi_now)
            P_now = 0.5 * pi_now**2 - Potential(psi_now)
            w0 = P_now / rho_now
            
            # Calcular wa = -dw/da * a (aprox numérica)
            # Usamos el paso anterior
            a_prev = sol[-2, 0]
            psi_prev = sol[-2, 1]
            pi_prev = sol[-2, 2]
            rho_prev = 0.5 * pi_prev**2 + Potential(psi_prev)
            P_prev = 0.5 * pi_prev**2 - Potential(psi_prev)
            w_prev = P_prev / rho_prev
            
            dw_da = (w0 - w_prev) / (a_now - a_prev)
            wa = -dw_da * a_now # Definición CPL: w(a) = w0 + wa(1-a)
            
            results_w0[i, j] = w0
            results_wa[i, j] = wa

    # 3. VISUALIZACIÓN (Espacio de Fases CPL)
    # ---------------------------------------
    plt.figure(figsize=(10, 8))
    
    # Puntos del modelo
    # Aplanamos los arrays para scatter plot
    X = results_w0.flatten()
    Y = results_wa.flatten()
    
    # Colorear por alpha (masa)
    Colors = np.repeat(alphas, len(psi_inits))
    
    sc = plt.scatter(X, Y, c=Colors, cmap='viridis', s=50, alpha=0.8, label='Modelos Fondo Dinámico')
    plt.colorbar(sc, label=r'Parámetro de Masa $\alpha$')
    
    # Zona de Observación (Planck + BAO + SNIa aprox)
    # w0 ~ -1.0 +/- 0.05, wa ~ 0.0 +/- 0.3
    plt.errorbar(-1.0, 0.0, xerr=0.05, yerr=0.3, fmt='o', color='red', label='Datos Observacionales (Planck 2018)', capsize=5)
    
    # Líneas de referencia
    plt.axvline(-1, color='k', linestyle='--', alpha=0.5)
    plt.axhline(0, color='k', linestyle='--', alpha=0.5)
    
    # Región "Thawing" (w0 > -1, wa < 0 generalmente para thawing simple)
    # Región "Freezing" (w0 > -1, wa > 0)
    
    plt.xlabel(r'Ecuación de Estado Actual ($w_0$)')
    plt.ylabel(r'Evolución ($w_a$)')
    plt.title('Predicciones del Fondo Dinámico vs Observaciones (Plano CPL)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Límites del gráfico para centrar en la acción
    plt.xlim(-1.02, -0.8)
    plt.ylim(-1.0, 0.5)
    
    plt.show()

parameter_space_scan()