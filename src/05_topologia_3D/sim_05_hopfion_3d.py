import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage import measure

# ==========================================
# 1. CONFIGURACIÓN DEL ESPACIO 3D
# ==========================================

N = 64              # Resolución (Cubo 64^3)
L = 10.0            # Tamaño de la caja
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
z = np.linspace(-L/2, L/2, N)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Coordenada radial esférica
R_sq = X**2 + Y**2 + Z**2

# ==========================================
# 2. CONSTRUCCIÓN DEL HOPFIÓN (FIBRACIÓN DE HOPF)
# ==========================================
# Usamos la proyección estereográfica inversa para mapear R^3 -> S^3
# y luego el mapa de Hopf S^3 -> S^2 (Campo complejo).

print("Generando estructura topológica del Hopfión...")

# Escala del nudo
R0 = 2.0 

# Coordenadas proyectadas (Mapa de Hopf racional)
# Psi ~ (2(x + iy)) / (2z + i(r^2 - 1))
# Esto crea una estructura donde las líneas de fase constante son círculos de Villarceau.

Numerator = 2 * (X + 1j * Y)
Denominator = 2 * Z + 1j * (R_sq - R0**2)

# El campo escalar Psi
Psi = Numerator / Denominator

# Normalización y perfil de densidad
# El núcleo del vórtice está donde Psi -> 0 o Psi -> infinito (singularidades).
# En este mapa, el núcleo es un anillo en el plano XY con radio R0.
# Aplicamos una función de densidad suave para que sea físico.

rho_0 = 1.0
# La densidad debe caer en la singularidad (el anillo del nudo)
# Usamos una aproximación basada en la magnitud del mapa proyectado
Mag = np.abs(Psi)
Density = rho_0 * (Mag**2 / (1 + Mag**2)) # Perfil tipo Skyrmion suave

# Reconstruimos el campo completo
Psi_field = np.sqrt(Density) * np.exp(1j * np.angle(Psi))

# ==========================================
# 3. VISUALIZACIÓN VOLUMÉTRICA (ISOSUPERFICIE)
# ==========================================

print("Calculando isosuperficie del núcleo...")

# Buscamos la región donde la densidad es baja (el "tubo" del nudo)
# Umbral: 30% de la densidad máxima
level = 0.3 * np.max(Density)

# Algoritmo Marching Cubes para obtener la malla 3D
verts, faces, normals, values = measure.marching_cubes(Density, level)

# Ajustar vértices a las coordenadas físicas
verts = verts * (L/N) - L/2

# --- PLOT ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear la malla poligonal
triangles = [verts[face] for face in faces]
mesh = Poly3DCollection(triangles, alpha=0.7)
mesh.set_edgecolor('k')
mesh.set_linewidth(0.1)

# Colorear el nudo según la FASE local (Esto revela la topología)
# Interpolamos la fase en los vértices de la malla
# (Truco rápido: usamos la posición de los vértices para recalcular la fase)
verts_indices = (verts + L/2) * (N/L)
verts_indices = verts_indices.astype(int)
# Clampeamos índices para evitar errores de borde
verts_indices = np.clip(verts_indices, 0, N-1)

# Extraemos la fase en cada vértice de la superficie
phases = np.angle(Psi_field[verts_indices[:,0], verts_indices[:,1], verts_indices[:,2]])

# Mapeamos fase a color (Colormap cíclico hsv)
# Normalizamos fase de -pi,pi a 0,1
colors = plt.cm.hsv((phases + np.pi) / (2*np.pi))
mesh.set_facecolor(colors)

ax.add_collection3d(mesh)

# Ajustes de la cámara
ax.set_xlim(-L/2, L/2)
ax.set_ylim(-L/2, L/2)
ax.set_zlim(-L/2, L/2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title(f"Estructura del Hopfión (Carga Q=1)\nIsosuperficie de Densidad coloreada por Fase")

# Vista inicial
ax.view_init(elev=30, azim=45)

print("Mostrando visualización. Busca un anillo retorcido (Toro).")
plt.tight_layout()
plt.show()