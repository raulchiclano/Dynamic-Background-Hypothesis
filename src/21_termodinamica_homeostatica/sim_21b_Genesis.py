import numpy as np
import matplotlib.pyplot as plt

# 1. CONFIGURACIÓN DE LA REJILLA
N = 128
L = 20.0
dx = L/N
dt = 0.01
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)

# Espacio de Fourier
k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
kx, ky = np.meshgrid(k, k)
k_sq = kx**2 + ky**2
k_sq[0, 0] = 1e-10 # Evitar división por cero

# 2. PARÁMETROS DE LA MISIÓN
alpha = -1.0
beta = 1.0
G_const = 0.5    # FUERZA DE LA GRAVEDAD (El Catalizador)
S_noise = 0.3    # Ruido del sustrato
gamma_H = 0.1    # Expansión (3H)

# 3. ESTADO INICIAL: Vacío casi perfecto
psi = np.ones((N, N), dtype=complex) * np.sqrt(-alpha/beta)
rho_0 = np.abs(psi)**2

vortex_history = []

print("--- EJECUTANDO MISIÓN 33: GÉNESIS ASISTIDO POR GRAVEDAD ---")

for i in range(2000):
    mag_sq = np.abs(psi)**2
    
    # --- PASO 1: SOLVER DE POISSON (Gravedad) ---
    # Calculamos la fluctuación de densidad: delta_rho = rho - rho_0
    delta_rho = mag_sq - np.mean(mag_sq)
    rho_k = np.fft.fft2(delta_rho)
    # V_grav en k es -4*pi*G * rho_k / k^2
    V_grav_k = -4 * np.pi * G_const * rho_k / k_sq
    V_grav = np.real(np.fft.ifft2(V_grav_k))
    
    # --- PASO 2: EVOLUCIÓN NO LINEAL (Potencial + Gravedad + Ruido) ---
    # El potencial total incluye la Acción v4 y la Gravedad
    dV = (alpha + beta * mag_sq + V_grav)
    psi *= np.exp(-1j * dV * dt - gamma_H * dt)
    
    # Inyección de ruido (S)
    noise = S_noise * (np.random.randn(N, N) + 1j * np.random.randn(N, N))
    psi += noise * np.sqrt(dt)
    
    # --- PASO 3: EVOLUCIÓN CINÉTICA (Fourier) ---
    psi_k = np.fft.fft2(psi)
    psi_k *= np.exp(-0.5j * k_sq * dt)
    psi = np.fft.ifft2(psi_k)
    
    # --- CONTEO DE MATERIA ---
    if i % 50 == 0:
        phase = np.angle(psi)
        vortices = np.sum(np.abs(np.diff(phase, axis=0)) > np.pi) // 2
        vortex_history.append(vortices)
        if i % 500 == 0: print(f"Paso {i}: Vórtices (Materia) = {vortices}")

# 4. VISUALIZACIÓN
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

ax1.plot(vortex_history, color='green', lw=2)
ax1.set_title("Emergencia de Materia (Asistida por Gravedad)")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Número de Vórtices")

ax2.imshow(np.angle(psi), cmap='hsv')
ax2.set_title("Mapa de Fase: El Nacimiento de los Fermiones")

plt.show()