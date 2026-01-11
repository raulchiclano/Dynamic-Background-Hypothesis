import numpy as np

# 1. CONFIGURACIÓN ESPACIAL 3D
N = 64
L = 10.0
dx = L / N
x = np.linspace(-L/2, L/2, N)
X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

# 2. GEOMETRÍA DEL ANILLO (Vortex Ring)
R_ring = 2.5
a = 0.8
rho_cyl = np.sqrt(X**2 + Y**2)
dist_to_core = np.sqrt((rho_cyl - R_ring)**2 + Z**2)

# Corriente toroidal (el flujo que da la vuelta al anillo)
# Este flujo tiene componentes en X, Y y Z debido a la curvatura
j_mag = np.exp(-dist_to_core**2 / (2 * a**2))
jx = -Y / (rho_cyl + 1e-12) * j_mag
jy =  X / (rho_cyl + 1e-12) * j_mag
jz = (Z / (dist_to_core + 1e-12)) * j_mag # Componente poloidal (torsión)

# 3. ROTACIONAL: CAMPO GAUGE (B = curl j)
def curl(jx, jy, jz):
    djz_dy = np.gradient(jz, dx, axis=1)
    djy_dz = np.gradient(jy, dx, axis=2)
    djx_dz = np.gradient(jx, dx, axis=2)
    djz_dx = np.gradient(jz, dx, axis=0)
    djy_dx = np.gradient(jy, dx, axis=0)
    djx_dy = np.gradient(jx, dx, axis=1)
    return djz_dy - djy_dz, djx_dz - djz_dx, djy_dx - djx_dy

Bx, By, Bz = curl(jx, jy, jz)

# 4. ENERGÍAS DE CAMPO
E_Bx = np.sum(Bx**2)
E_By = np.sum(By**2)
E_Bz = np.sum(Bz**2)
E_gauge_total = E_Bx + E_By + E_Bz

# 5. EL RATIO EMERGENTE
# Comparamos la energía total del campo frente a la componente principal
ratio = np.sqrt(E_gauge_total / E_Bz)

print("\n--- SIM 27_6: TEST DE VESTIDO GAUGE (GEOMETRÍA 3D) ---")
print(f"Energía Bx: {E_Bx:.4f}, By: {E_By:.4f}, Bz: {E_Bz:.4f}")
print(f"Ratio emergente (sqrt(Total/Principal)): {ratio:.4f}")
print(f"Objetivo geométrico: sqrt(3) = {np.sqrt(3):.4f}")

# 6. PREDICCIÓN DE LA MASA VESTIDA
E_elastic = 79.0 
alpha_inv_pred = E_elastic * ratio
print(f"\nMasa vestida predicha: {alpha_inv_pred:.4f}")
print(f"Valor real (1/alpha): 137.0360")