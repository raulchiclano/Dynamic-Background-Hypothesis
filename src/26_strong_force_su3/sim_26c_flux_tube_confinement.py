import numpy as np
import matplotlib.pyplot as plt

# 1. CONFIGURACIÓN DE ALTA PRECISIÓN
N = 128
L = 10.0
dx = L/N
dt = 0.002 # Paso muy fino
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)

# Espacio de Fourier (Momentos k)
k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
kx, ky = np.meshgrid(k, k)
k_sq = kx**2 + ky**2

# 2. PARÁMETROS DE LA ACCIÓN v4 (Ajustados para ver la cuerda)
alpha = -1.0
beta = 1.0
sigma = 1.5 # El "pegamento" de los quarks

# 3. ESTADO INICIAL: Dos Quarks (Q=1/2)
def get_pair(d):
    theta1 = np.arctan2(Y, X - d)
    theta2 = np.arctan2(Y, X + d)
    # Añadimos un pequeño núcleo para evitar el cero absoluto inicial
    return np.exp(1j * 0.5 * theta1) * np.exp(1j * -0.5 * theta2)

psi = get_pair(1.0)

print("--- EJECUTANDO MISIÓN 26c: EL TUBO DE FLUJO (SPLIT-STEP) ---")

for i in range(1000):
    # --- PASO 1: Evolución en Espacio Real (Potencial v4) ---
    mag_sq = np.abs(psi)**2
    # V = alpha + beta*rho + sigma*sqrt(rho)
    V_eff = alpha + beta * mag_sq + sigma * np.sqrt(mag_sq + 1e-4)
    
    # Evolución por fase (Imposible que explote)
    psi *= np.exp(-1j * V_eff * dt)
    
    # --- PASO 2: Evolución en Espacio de Fourier (Cinética) ---
    psi_k = np.fft.fft2(psi)
    psi_k *= np.exp(-0.5j * k_sq * dt)
    psi = np.fft.ifft2(psi_k)
    
    if i % 200 == 0:
        print(f"Paso {i} completado...")

# 4. VISUALIZACIÓN DEL RESULTADO
plt.figure(figsize=(12, 5))

# Mapa de Densidad: Buscamos la "Cuerda" entre los quarks
plt.subplot(1, 2, 1)
plt.imshow(np.abs(psi)**2, cmap='magma', extent=[-L/2, L/2, -L/2, L/2])
plt.title("Densidad del Vacío (Tubo de Flujo)")
plt.colorbar(label="Densidad rho")

# Mapa de Fase: Buscamos las Alice Strings
plt.subplot(1, 2, 2)
plt.imshow(np.angle(psi), cmap='hsv', extent=[-L/2, L/2, -L/2, L/2])
plt.title("Fase Nemática (Alice Strings)")
plt.colorbar(label="Fase")

plt.show()