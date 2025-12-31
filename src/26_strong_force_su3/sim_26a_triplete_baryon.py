import numpy as np
import matplotlib.pyplot as plt

# 1. CONFIGURACIÓN DE LA REJILLA
N = 256
L = 10.0
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)

# 2. DEFINICIÓN DE LOS 3 QUARKS (Triángulo equilátero central)
d = 0.5 # Distancia al centro
pos = [
    (d * np.cos(0), d * np.sin(0)),             # Quark 1
    (d * np.cos(2*np.pi/3), d * np.sin(2*np.pi/3)), # Quark 2
    (d * np.cos(4*np.pi/3), d * np.sin(4*np.pi/3))  # Quark 3
]

# Fases de Color (Rojo, Verde, Azul) -> Desplazamientos de 120 grados
colors = [0, 2*np.pi/3, 4*np.pi/3]

def get_vortex_field(x0, y0, color_phase):
    R_v = np.sqrt((X-x0)**2 + (Y-y0)**2) + 1e-10
    Theta_v = np.arctan2(Y-y0, X-x0)
    # Defecto Q=1/2 con su fase de color
    return np.exp(1j * (0.5 * Theta_v + color_phase))

# 3. CONSTRUCCIÓN DEL CAMPO TOTAL (PROTÓN)
psi_total = get_vortex_field(pos[0][0], pos[0][1], colors[0]) * \
            get_vortex_field(pos[1][0], pos[1][1], colors[1]) * \
            get_vortex_field(pos[2][0], pos[2][1], colors[2])

# 4. CÁLCULO DE LA DENSIDAD DE ENERGÍA (ESTRÉS ELÁSTICO)
# E ~ |grad(psi)|^2
dy, dx = np.gradient(psi_total, L/N)
energy_density = np.abs(dx)**2 + np.abs(dy)**2

# 5. COMPARACIÓN CON UN QUARK AISLADO
psi_single = get_vortex_field(0, 0, 0)
dy_s, dx_s = np.gradient(psi_single, L/N)
energy_single = np.abs(dx_s)**2 + np.abs(dy_s)**2

print("--- SIMULACIÓN 26: EL ORIGEN DEL PROTÓN ---")
print(f"Energía Total del Triplete (Barión): {np.sum(energy_density):.2f}")
print(f"Energía de 3 Quarks aislados: {3 * np.sum(energy_single):.2f}")

# 6. VISUALIZACIÓN
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Mapa de Fase (Se deben ver los 3 nudos)
im1 = ax1.imshow(np.angle(psi_total), cmap='hsv', extent=[-L/2, L/2, -L/2, L/2])
ax1.set_title("Fase del Triplete (Configuración de Color)")
plt.colorbar(im1, ax=ax1, label="Fase")

# Mapa de Energía (Estrés del Vacío)
im2 = ax2.imshow(energy_density, cmap='inferno', extent=[-L/2, L/2, -L/2, L/2], vmax=10)
ax2.set_title("Densidad de Energía (Confinamiento)")
plt.colorbar(im2, ax=ax2, label="Estrés")

plt.show()