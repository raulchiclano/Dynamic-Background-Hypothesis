import numpy as np
import matplotlib.pyplot as plt

# 1. CONFIGURACIÓN
alpha, beta, sigma = -1.0, 2.0, 0.1 # Parámetros v5.0 Beta

# 2. FUNCIÓN DE ENERGÍA (Acción v4)
def calculate_energy_density(rho, grad_sq):
    e_kin = 0.5 * grad_sq
    e_pot = alpha * rho + 0.5 * beta * rho**2 + (2/3) * sigma * rho**1.5
    # Restamos la densidad de vacío para renormalizar (rho_vac = 0.5)
    e_vac = (alpha * 0.5 + 0.5 * beta * 0.5**2 + (2/3) * sigma * 0.5**1.5)
    return e_kin + e_pot - e_vac

# 3. MODELO 0D: EL ELECTRÓN (Vértice de estrés)
# Energía concentrada en una esfera de radio r_p (escala de Planck)
r = np.linspace(0.01, 1.0, 500)
dr = r[1] - r[0]
rho_0d = 0.5 * np.tanh(r)
grad_0d = (0.5 / (r**2 + 0.01))**2
# Integración esférica: 4*pi*r^2
energy_0d_dens = calculate_energy_density(rho_0d, grad_0d) * 4 * np.pi * r**2
E_0D = np.trapezoid(energy_0d_dens, r)

# 4. MODELO 1D: EL PROTÓN (Arista de estrés)
# Energía distribuida en una línea (tubo de flujo)
# Calculamos la tensión de la cuerda (energía por unidad de longitud)
rho_1d = 0.1 # Densidad de confinamiento
grad_1d = 1.5 # Tensión elástica de la cuerda
E_per_unit_length = calculate_energy_density(rho_1d, grad_1d)

# El protón es una red de cuerdas. Su longitud efectiva en unidades de Planck
# es el ratio de aspecto del vacío nemático.
L_effective = 18.36 * 10.0 # Longitud de la cicatriz hadrónica
E_1D = E_per_unit_length * L_effective

print("--- SIMULACIÓN 28: TRANSICIÓN DE DIMENSIONALIDAD ---")
print(f"Energía del Atractor 0D (Vértice/Electrón): {E_0D:.6f}")
print(f"Energía del Atractor 1D (Arista/Protón): {E_1D:.6f}")

ratio = E_1D / E_0D
print(f"\nRATIO DIMENSIONAL (1D / 0D): {ratio:.4f}")

# 5. VISUALIZACIÓN
plt.figure(figsize=(8, 6))
plt.bar(['Electrón (0D)', 'Protón (1D)'], [E_0D, E_1D], color=['#3498db', '#e74c3c'])
plt.yscale('log')
plt.ylabel("Energía (Escala Logarítmica)")
plt.title("Masa como Salto de Dimensión del Estrés")
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.show()