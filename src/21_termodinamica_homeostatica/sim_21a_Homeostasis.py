import numpy as np
import matplotlib.pyplot as plt

# 1. PARÁMETROS DEL ECOSISTEMA
Gamma = 0.1   # Tasa de Trituración (M -> L)
sigma = 0.05  # Tasa de Nucleación (L -> M)
S = 0.02      # Inyección Pre-geométrica (El "latido" del sustrato)
phi = (1 + np.sqrt(5)) / 2
dt = 0.05
steps = 10000

# 2. ESTADO INICIAL
M = 0.1      # Empezamos con poca materia
Lambda = 0.5 # Empezamos con un fondo activo
a = 1.0

history = {'t': [], 'M': [], 'L': [], 'H': [], 'a': []}

print("--- EJECUTANDO MISIÓN 30: EL ECOSISTEMA ETERNO ---")

for i in range(steps):
    H = np.sqrt(Lambda)
    
    # DINÁMICA DEL ECOSISTEMA
    # dM: Materia (Reciclaje + Creación)
    dM = (-Gamma * M + sigma * Lambda) * dt
    
    # dL: Fondo (Calentamiento + Enfriamiento + Inyección)
    dL = (Gamma * M - sigma * Lambda - (H * Lambda / (phi**2)) + S) * dt
    
    # da: Expansión
    da = a * H * dt
    
    M += dM
    Lambda += dL
    a += da
    
    history['t'].append(i * dt)
    history['M'].append(M)
    history['L'].append(Lambda)
    history['H'].append(H)
    history['a'].append(a)

# 3. VISUALIZACIÓN DE LA VIDA CÓSMICA
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: El Equilibrio Dinámico
ax1.plot(history['t'], history['M'], color='blue', lw=2, label="Materia (Vórtices)")
ax1.plot(history['t'], history['L'], color='red', lw=2, label="Energía Oscura (Fondo)")
ax1.set_title("Homeostasis Completa: El Ciclo Eterno")
ax1.set_xlabel("Tiempo Cósmico")
ax1.set_ylabel("Densidad")
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico 2: Espacio de Fase (M vs Lambda)
# Si hay un círculo o un punto fijo, hay un Atractor de Vida.
ax2.plot(history['M'], history['L'], color='purple', lw=1)
ax2.scatter(history['M'][0], history['L'][0], color='green', label="Inicio")
ax2.scatter(history['M'][-1], history['L'][-1], color='red', label="Estado Estacionario")
ax2.set_title("Espacio de Fase: El Atractor de la DBH")
ax2.set_xlabel("Materia (M)")
ax2.set_ylabel("Fondo (Lambda)")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Estado Final: M = {M:.4f}, Lambda = {Lambda:.4f}")