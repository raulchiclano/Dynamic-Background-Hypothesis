import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label

# 1. CONFIGURACIÓN: CAJA ALARGADA (Ladrillo 10x5x5)
Nx, Ny, Nz = 64, 32, 32 
Lx, Ly, Lz = 10.0, 5.0, 5.0
dx = Lx/Nx
dt = 0.002
steps = 6000
x = np.linspace(-Lx/2, Lx/2, Nx)
y = np.linspace(-Ly/2, Ly/2, Ny)
z = np.linspace(-Lz/2, Lz/2, Nz)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Espacio de Fourier Anisótropo
kx = 2 * np.pi * np.fft.fftfreq(Nx, d=dx)
ky = 2 * np.pi * np.fft.fftfreq(Ny, d=dx)
kz = 2 * np.pi * np.fft.fftfreq(Nz, d=dx)
KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing='ij')
k_sq_3d = KX**2 + KY**2 + KZ**2

# 2. PARÁMETROS ACCIÓN v4 (IDÉNTICOS A 27f)
alpha, beta, sigma = -1.0, 2.0, 0.1
E_vac_dens = (alpha * 0.5 + 0.5 * beta * 0.5**2 + (2/3) * sigma * 0.5**1.5)

def run_geometry_test():
    # Estado inicial: Caos térmico
    psi = (np.random.randn(Nx,Ny,Nz) + 1j*np.random.randn(Nx,Ny,Nz)) * 0.8
    
    for i in range(steps):
        # Rampado Adiabático de S
        S_current = 0.2 * (1 - i/steps)
        gamma_current = 0.1 * (1 - i/steps)
        
        mag_sq = np.abs(psi)**2
        V_eff = alpha + beta * mag_sq + sigma * np.sqrt(mag_sq + 1e-6)
        
        # Evolución Split-Step
        psi *= np.exp(-1j * V_eff * dt - gamma_current * V_eff * dt)
        noise = S_current * psi * (np.random.randn(Nx,Ny,Nz) + 1j*np.random.randn(Nx,Ny,Nz)) * np.sqrt(dt)
        psi += noise
        
        psi_k = np.fft.fftn(psi)
        psi_k *= np.exp(-0.5j * k_sq_3d * dt)
        psi = np.fft.ifftn(psi_k)
        
    # Cálculo de Masa Neta Final
    dy_g, dx_g, dz_g = np.gradient(psi, dx)
    e_kin = 0.5 * (np.abs(dx_g)**2 + np.abs(dy_g)**2 + np.abs(dz_g)**2)
    e_pot = (alpha * np.abs(psi)**2 + 0.5 * beta * np.abs(psi)**4 + (2/3) * sigma * np.abs(psi)**3)
    m_total = np.sum(e_kin + e_pot - E_vac_dens) * dx**3
    return m_total

print("--- SIMULACIÓN 27b: EL TEST DE LA GEOMETRÍA ---")
print("Escenario: Caja Alargada (Volumen x2)")
m_final = run_geometry_test()

print(f"\n--- RESULTADO DEL JUICIO ---")
print(f"Masa detectada en Caja Alargada: {m_final:.6f}")
print(f"Masa previa (Caja Cúbica): ~3616.0")

ratio_cambio = m_final / 3616.0
print(f"Factor de escala de masa: {ratio_cambio:.4f}")

if 0.9 < ratio_cambio < 1.1:
    print("VERDICTO: INVARIANZA CONFIRMADA. El Unicornio es una partícula local.")
elif 1.8 < ratio_cambio < 2.2:
    print("VERDICTO: ARTEFACTO DETECTADO. La masa depende del volumen (Error de Escala).")
else:
    print("VERDICTO: TRANSICIÓN DE FASE. El sistema ha colapsado a un nuevo atractor.")