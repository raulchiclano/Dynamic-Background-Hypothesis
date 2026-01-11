import numpy as np

def run_honest_calibration(L_val):
    N = int(128 * (L_val / 15.0))
    dx = L_val / N
    dtau = 0.005
    x = np.linspace(-L_val/2, L_val/2, N)
    y = np.linspace(-L_val/2, L_val/2, N)
    X, Y = np.meshgrid(x, y)

    # Coordenadas de los nudos (índices en la matriz)
    d_sep = 2.0
    idx_p1 = (np.abs(x - d_sep).argmin(), np.abs(y).argmin())
    idx_p2 = (np.abs(x + d_sep).argmin(), np.abs(y).argmin())

    k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    kx, ky = np.meshgrid(k, k)
    k_sq = kx**2 + ky**2

    alpha, beta, sigma = -1.0, 2.0, 0.1

    def get_hamiltonian(p):
        mag_sq = np.abs(p)**2
        pk = np.fft.fft2(p)
        grad_x = np.fft.ifft2(1j * kx * pk)
        grad_y = np.fft.ifft2(1j * ky * pk)
        # SOLO Cinética + Potencial v4 (SIN ANCLA)
        E_kin = 0.5 * np.sum(np.abs(grad_x)**2 + np.abs(grad_y)**2)
        E_pot = np.sum(alpha * mag_sq + 0.5 * beta * mag_sq**2 + (2/3) * sigma * mag_sq**1.5)
        return (E_kin + E_pot) * dx**2

    def relax(initial_psi, is_dipole=False):
        p = initial_psi.copy()
        for i in range(2000):
            mag_sq = np.abs(p)**2
            V_eff = alpha + beta * mag_sq + sigma * np.sqrt(mag_sq + 1e-6)
            p *= np.exp(-V_eff * dtau)
            pk = np.fft.fft2(p)
            pk *= np.exp(-0.5 * k_sq * dtau)
            p = np.fft.ifft2(pk)
            
            # --- RESTRICCIÓN TOPOLÓGICA (El "Ancla Invisible") ---
            if is_dipole:
                p[idx_p1] = 0
                p[idx_p2] = 0
            
            # Normalización al vacío
            p *= np.sqrt(-alpha/beta) / (np.abs(p[0,0]) + 1e-6)
        return p

    # Ejecución
    psi_vac = relax(np.ones((N, N), dtype=complex) * np.sqrt(-alpha/beta))
    E_vac = get_hamiltonian(psi_vac)
    
    theta1, theta2 = np.arctan2(Y, X - d_sep), np.arctan2(Y, X + d_sep)
    psi_dip_init = np.sqrt(-alpha/beta) * np.exp(1j * 0.5 * theta1) * np.exp(-1j * 0.5 * theta2)
    psi_dip = relax(psi_dip_init, is_dipole=True)
    E_dip = get_hamiltonian(psi_dip)
    
    return (E_dip - E_vac) / 2

print("--- SIMULACIÓN 27a-HONESTA: MASA PURA (SIN POTENCIALES EXTERNOS) ---")
m15 = run_honest_calibration(15.0)
print(f"Masa en L=15: {m15:.6f}")
m20 = run_honest_calibration(20.0)
print(f"Masa en L=20: {m20:.6f}")

diff_pct = abs(m15 - m20) / m15 * 100
print(f"\nDesviación final: {diff_pct:.4f}%")