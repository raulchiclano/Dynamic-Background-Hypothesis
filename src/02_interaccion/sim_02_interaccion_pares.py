import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ==========================================
# 1. CONFIGURACIÓN ROBUSTA
# ==========================================

# Parámetros Físicos
N = 128             # Resolución (128x128 es más rápido y estable para pruebas)
L = 30.0            # Caja más grande para alejar los bordes
dt = 0.005          # Paso de tiempo reducido (Real)
dt_im = 0.005       # Paso de tiempo imaginario (Relajación)
g = 2.0             # Interacción más suave (aumenta el tamaño del vórtice)
rho_0 = 1.0         # Densidad base

# Rejilla
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)
dx = x[1] - x[0]

# Espacio de Momentos (k-space)
k = 2 * np.pi * np.fft.fftfreq(N, d=dx)
KX, KY = np.meshgrid(k, k)
K2 = KX**2 + KY**2

# Potencial de Trampa (Opcional: Suaviza los bordes para evitar ruido FFT)
# V = 0 en el centro, sube suavemente en los bordes
R_grid = np.sqrt(X**2 + Y**2)
V_trap = 0.5 * (R_grid / (0.45*L))**10  # "Caja suave"
V_trap[V_trap > 100] = 100

# ==========================================
# 2. CONDICIONES INICIALES (INTERACCIÓN DE 2 VÓRTICES)
# ==========================================

# Posiciones de los vórtices (Separación media)
d_sep = 3.0
x1, y1 = -d_sep, 0.0  # Vórtice 1 (Izquierda)
x2, y2 = +d_sep, 0.0  # Vórtice 2 (Derecha)

# Coordenadas relativas al Vórtice 1
X1 = X - x1
Y1 = Y - y1
R1 = np.sqrt(X1**2 + Y1**2)
Theta1 = np.arctan2(Y1, X1)

# Coordenadas relativas al Vórtice 2
X2 = X - x2
Y2 = Y - y2
R2 = np.sqrt(X2**2 + Y2**2)
Theta2 = np.arctan2(Y2, X2)

# Longitud de sanación teórica
xi = 1.0 / np.sqrt(g * rho_0)
xi_scale = 2.0 * xi # Escala inicial para el núcleo

# --- CONSTRUCCIÓN DEL ANSATZ DE PRODUCTO ---
# Densidad: Multiplicamos las tanh para crear "agujeros" en ambas posiciones.
# Fase: Sumamos las fases (Theta1 + Theta2) en el exponente complejo.
# Esto conserva la carga topológica total Q_total = 1 + 1 = 2.

Psi_0 = np.sqrt(rho_0) * \
        np.tanh(R1 / xi_scale) * np.tanh(R2 / xi_scale) * \
        np.exp(1j * (Theta1 + Theta2))

# IMPORTANTE: Actualizamos la variable de referencia 'Theta' para la Relajación.
# La rutina de tiempo imaginario necesita saber que la topología correcta
# ahora incluye DOS singularidades, o intentará borrar una.
Theta = np.angle(np.exp(1j * (Theta1 + Theta2))) 

# Inicialización
Psi = Psi_0.copy()

print(f"Sistema inicializado con 2 Vórtices en x={-d_sep} y x={+d_sep}")

# Operador cinético para ITE (exponencial real decreciente)
U_kin_im = np.exp(-(K2 / 2.0) * dt_im)

for i in range(200): # 200 pasos de enfriamiento
    # 1. Paso de Potencial + Interacción (en espacio real)
    # En ITE, la norma decae, así que hay que renormalizar para mantener la densidad.
    # Usamos un método simplificado: mantener la fase fija y relajar la densidad.
    
    density = np.abs(Psi)**2
    # Operador potencial en tiempo imaginario
    Psi = Psi * np.exp(-(V_trap + g * density) * (dt_im / 2))
    
    # 2. Paso Cinético (FFT)
    Psi_k = np.fft.fft2(Psi)
    Psi_k *= U_kin_im
    Psi = np.fft.ifft2(Psi_k)
    
    # 3. Paso de Potencial (segunda mitad)
    density = np.abs(Psi)**2
    Psi = Psi * np.exp(-(V_trap + g * density) * (dt_im / 2))
    
    # 4. Renormalización (Crucial en ITE para no ir a cero)
    # Forzamos que la densidad lejos del centro tienda a rho_0
    norm_factor = np.sqrt(rho_0) / np.max(np.abs(Psi))
    Psi *= norm_factor
    
    # 5. Re-imponer la topología (Truco sucio pero efectivo para ITE simple)
    # Esto evita que el vórtice se disipe durante el enfriamiento
    Psi = np.abs(Psi) * np.exp(1j * Theta)

print("Relajación completada. Estado fundamental del vórtice encontrado.")

# ==========================================
# 4. EVOLUCIÓN EN TIEMPO REAL
# ==========================================

# Operador cinético Real (Unitario)
U_kin_real = np.exp(-1j * (K2 / 2.0) * dt)

def evolution_step_real(psi_in):
    # Split-Step Fourier Method estándar
    
    # Potencial + No linealidad
    psi_mod = psi_in * np.exp(-1j * (V_trap + g * np.abs(psi_in)**2) * (dt / 2))
    
    # Cinética
    psi_k = np.fft.fft2(psi_mod)
    psi_k *= U_kin_real
    psi_mod = np.fft.ifft2(psi_k)
    
    # Potencial + No linealidad
    psi_out = psi_mod * np.exp(-1j * (V_trap + g * np.abs(psi_mod)**2) * (dt / 2))
    
    return psi_out

# ==========================================
# 5. VISUALIZACIÓN
# ==========================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
plt.suptitle(f"Fondo Dinámico: Vórtice Estable (Post-Relajación)")

# Límites de color fijos para evitar parpadeo
im1 = ax1.imshow(np.abs(Psi)**2, extent=[-L/2, L/2, -L/2, L/2], 
                 cmap='inferno', origin='lower', vmin=0, vmax=1.1*rho_0)
ax1.set_title(r"Densidad $|\Psi|^2$")
plt.colorbar(im1, ax=ax1)

im2 = ax2.imshow(np.angle(Psi), extent=[-L/2, L/2, -L/2, L/2], 
                 cmap='hsv', origin='lower', vmin=-np.pi, vmax=np.pi)
ax2.set_title(r"Fase $\theta$")
plt.colorbar(im2, ax=ax2)

def update(frame):
    global Psi
    # 5 pasos de física por cada frame de video
    for _ in range(5):
        Psi = evolution_step_real(Psi)
    
    im1.set_data(np.abs(Psi)**2)
    im2.set_data(np.angle(Psi))
    return im1, im2

ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=True)
plt.show()
