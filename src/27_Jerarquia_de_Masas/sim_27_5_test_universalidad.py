import numpy as np

# 1. FUNCIÓN DE INTEGRACIÓN COMPATIBLE
try: integrate = np.trapezoid
except AttributeError: integrate = np.trapz

# 2. CONFIGURACIÓN DEL BARRIDO (Reducido a 3x3 para velocidad, manteniendo el rango)
beta_vals = [1.6, 2.0, 2.4]  
sigma_vals = [0.08, 0.1, 0.12] 
dr = 0.02
r = np.arange(dr/2, 8.0, dr) + dr/2

def get_ratio(b, s):
    # Calibración del vacío real para cada par (b, s)
    u = (-s + np.sqrt(s**2 + 8*b)) / (4*b)
    rho_t = u**2
    v_t = -1.0*rho_t + 0.5*b*rho_t**2 + (2/3)*s*rho_t**1.5
    v_lim = abs(v_t)

    def solve_soliton(dim):
        psi = np.sqrt(rho_t) * np.tanh(r)
        dt = 0.0001
        for _ in range(8000):
            dpsi = np.gradient(psi, dr)
            d2psi = np.gradient(dpsi, dr)
            lap = d2psi + (dim - 1) / r * dpsi
            rho = psi**2
            dv = 2*(-1.0)*psi + 2*b*rho*psi + 3*s*np.sqrt(rho + 1e-10)*psi
            psi += (lap - dv) * dt
            psi[0], psi[-1] = 0, np.sqrt(rho_t)
        return psi

    p0d = solve_soliton(3)
    p1d = solve_soliton(2)

    def e_cont(p, dim):
        rho = p**2
        grad = np.gradient(p, dr)
        h = 0.5*grad**2 + (-1.0*rho + 0.5*b*rho**2 + (2/3)*s*rho**1.5 - v_t)
        deuda = np.maximum(0, h - v_lim)
        if dim == 3: return integrate(deuda * 4 * np.pi * r**2, r)
        else: return integrate(deuda * 2 * np.pi * r, r)

    e0 = e_cont(p0d, 3)
    t1 = e_cont(p1d, 2)
    # Ratio final con factor de forma L=14.98
    return (t1 * 14.98) / e0 

print("--- SIMULACIÓN 27_5: TEST DE UNIVERSALIDAD (FIXED) ---")
results = []

for b in beta_vals:
    for s in sigma_vals:
        r_val = get_ratio(b, s)
        results.append(r_val)
        print(f"Beta={b:.1f}, Sigma={s:.2f} -> Ratio={r_val:.2f}")

# 3. ANÁLISIS DE SENSIBILIDAD
results = np.array(results)
mean_ratio = np.mean(results)
std_ratio = np.std(results)
sensitivity = (std_ratio / mean_ratio) * 100

print(f"\n--- RESULTADO DE UNIVERSALIDAD ---")
print(f"Ratio Medio: {mean_ratio:.2f}")
print(f"Desviación Estándar: {std_ratio:.2f}")
print(f"SENSIBILIDAD PARAMÉTRICA: {sensitivity:.2f}%")

if sensitivity < 5.0:
    print("VERDICTO: INVARIANTE ESTRUCTURAL CONFIRMADO. El ratio es una propiedad de la Acción v4.")
else:
    print("VERDICTO: DEPENDENCIA DETECTADA. El ratio no es universal.")