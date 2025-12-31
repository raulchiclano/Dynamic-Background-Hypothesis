import numpy as np
import matplotlib.pyplot as plt

# 1. CONFIGURACIÓN
N = 128
L = 10.0
dx = L/N
dt = 0.005
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)

# 2. POTENCIAL ACCIÓN v4 (El motor del confinamiento)
alpha = -1.0
beta = 1.0
sigma = 2.0 # Aumentamos sigma para ver el efecto de "congelación"

# 3. ESTADO INICIAL: Dos Quarks (Q=1/2)
def get_pair(d):
    theta1 = np.arctan2(Y, X - d)
    theta2 = np.arctan2(Y, X + d)
    return np.exp(1j * 0.5 * theta1) * np.exp(1j * -0.5 * theta2)

psi = get_pair(0.5)

print("--- SIMULACIÓN 26b: TRANSICIÓN DE FASE Y CONFINAMIENTO ---")

# 4. EVOLUCIÓN DINÁMICA (GPE)
for i in range(500):
    mag_sq = np.abs(psi)**2
    
    # Laplaciano (Energía Cinética)
    psi_lap = (np.roll(psi, 1, axis=0) + np.roll(psi, -1, axis=0) +
               np.roll(psi, 1, axis=1) + np.roll(psi, -1, axis=1) - 4*psi) / dx**2
    
    # Potencial v4 con el término sigma "congelante"
    dV = alpha * psi + beta * mag_sq * psi + sigma * np.sqrt(mag_sq + 1e-6) * psi
    
    # Evolución
    psi += 1j * (0.5 * psi_lap - dV) * dt
    
    # Forzamos la separación lenta de los quarks (Simulando tensión)
    if i % 10 == 0:
        d_current = 0.5 + i*0.002
        # (Opcional: podrías dejar que la propia dinámica decida, 
        # pero aquí forzamos para ver la respuesta del fluido)

# 5. VISUALIZACIÓN DEL TUBO DE FLUJO
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(np.abs(psi)**2, cmap='viridis')
plt.title("Densidad del Fluido (Buscando el Tubo)")

plt.subplot(1, 2, 2)
plt.imshow(np.angle(psi), cmap='hsv')
plt.title("Fase (Alice Strings)")
plt.show()