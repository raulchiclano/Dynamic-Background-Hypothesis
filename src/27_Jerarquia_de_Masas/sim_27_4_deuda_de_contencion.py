import numpy as np
import matplotlib.pyplot as plt

# 1. FUNCIÓN DE INTEGRACIÓN ROBUSTA
try: integrate = np.trapezoid
except AttributeError: integrate = np.trapz

# 2. PARÁMETROS ACCIÓN v4 (GRABADOS EN PIEDRA)
alpha, beta, sigma = -1.0, 2.0, 0.1
dr = 0.01
r = np.arange(dr/2, 8.0, dr) + dr/2

# --- CALIBRACIÓN DEL LÍMITE DE RUPTURA ---
u = (-0.1 + np.sqrt(0.01 + 8)) / 4 # sqrt(rho_true)
rho_true = u**2
V_true = alpha*rho_true + 0.5*beta*rho_true**2 + (2/3)*sigma*rho_true**1.5
V_limit = abs(V_true) # El umbral de fluencia del vacío

def solve_soliton(dim, steps=10000):
    psi = np.sqrt(rho_true) * np.tanh(r)
    dt = 0.0001
    for _ in range(steps):
        dpsi = np.gradient(psi, dr)
        d2psi = np.gradient(dpsi, dr)
        laplacian = d2psi + (dim - 1) / r * dpsi
        rho = psi**2
        dv_dpsi = 2*alpha*psi + 2*beta*rho*psi + 3*sigma*np.sqrt(rho + 1e-10)*psi
        psi += (laplacian - dv_dpsi) * dt
        psi[0] = 0
        psi[-1] = np.sqrt(rho_true)
    return psi

print("--- SIMULACIÓN 27-v4: VALIDACIÓN DE LA DEUDA DE CONTENCIÓN ---")

# 3. GENERACIÓN DE PERFILES
psi_0d = solve_soliton(dim=3) # Electrón
psi_1d = solve_soliton(dim=2) # Cuerda (Protón)

# 4. CÁLCULO DE LA ENERGÍA DE CONTENCIÓN (E_cont)
def get_containment_energy(p, dim):
    rho = p**2
    grad = np.gradient(p, dr)
    # Densidad Hamiltoniana (Estrés Total)
    h_dens = 0.5*grad**2 + (alpha*rho + 0.5*beta*rho**2 + (2/3)*sigma*rho**1.5 - V_true)
    
    # FILTRO DE DEUDA: Solo integramos lo que supera el V_limit
    deuda_dens = np.maximum(0, h_dens - V_limit)
    
    if dim == 3: # 0D - Esférico
        return integrate(deuda_dens * 4 * np.pi * r**2, r), np.max(h_dens)
    else: # 1D - Cilíndrico
        return integrate(deuda_dens * 2 * np.pi * r, r), np.max(h_dens)

E_cont_0d, peak_0d = get_containment_energy(psi_0d, 3)
T_cont_1d, peak_1d = get_containment_energy(psi_1d, 2)

# 5. RESULTADOS Y RATIO
# Aplicamos el factor de forma L=14.98 para la cuerda del protón
L_skeleton = 14.98
E_cont_1d = T_cont_1d * L_skeleton

ratio_picos = peak_0d / peak_1d
ratio_masas = E_cont_1d / E_cont_0d

print(f"\nLímite de Ruptura (V_limit): {V_limit:.6f}")
print(f"--- ELECTRÓN (0D) ---")
print(f"   Estrés de Pico: {peak_0d:.4f}")
print(f"   Energía de Contención (Masa): {E_cont_0d:.6f}")

print(f"\n--- PROTÓN (1D) ---")
print(f"   Estrés de Pico: {peak_1d:.4f}")
print(f"   Energía de Contención (Masa): {E_cont_1d:.6f}")

print(f"\n--- VERDICTO DE LA BALANZA ---")
print(f"Ratio de Picos (e/p): {ratio_picos:.2f} (El electrón pincha más)")
print(f"RATIO DE MASAS (p/e): {ratio_masas:.2f} (El protón pesa más)")
print(f"Objetivo Real: 1836.15")