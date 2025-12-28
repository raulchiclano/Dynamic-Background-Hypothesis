import sympy
from sympy import symbols, Function, diff, simplify, sqrt

# Definimos las variables simbólicas
# g_inv es el tensor métrico contravariante g^{mu nu}
# psi es el campo escalar
# rho es la densidad psi**2
g_inv = symbols('g_inv') # Representación escalar para la variación
det_g = symbols('det_g')
psi = Function('Psi')(symbols('x'))
alpha, beta, sigma = symbols('alpha beta sigma')

# Definimos la densidad de Lagrangiana L
# Nota: Usamos la derivada de psi como 'd_psi'
d_psi = symbols('d_psi')
rho = psi**2
V = alpha * rho + beta * rho**2 + sigma * rho**(sympy.Rational(3, 2))

# L = -1/2 * g^{mu nu} * d_mu psi * d_nu psi - V(rho)
L = -sympy.Rational(1, 2) * g_inv * d_psi**2 - V

# La variación de sqrt(-g) respecto a g^{mu nu} es -1/2 * sqrt(-g) * g_{mu nu}
# Pero trabajaremos directamente con la definición de T_mu_nu
# T_mu_nu = 2 * dL/dg^{mu nu} - g_mu_nu * L

# 1. Derivada de L respecto a g^{mu nu}
dL_dg_inv = diff(L, g_inv)

# 2. Construcción de T_mu_nu (en forma simbólica general)
# T_mu_nu = d_mu psi * d_nu psi - g_mu_nu * (1/2 * g^{alpha beta} d_alpha psi d_beta psi + V)
T_mu_nu_kin = d_psi**2 # Término cinético
T_mu_nu_pot = L        # Término de la métrica por la Lagrangiana

print("--- DERIVACIÓN SIMBÓLICA T_mu_nu ---")
print(f"Derivada cinemática (dL/dg^inv): {dL_dg_inv}")
print(f"Lagrangiana completa (L): {simplify(L)}")

# Verificación de la Ecuación de Movimiento (Klein-Gordon modificada)
# dL/dpsi - d_mu(dL/d(d_mu psi)) = 0
dV_dpsi = diff(V, psi)
print(f"Término de fuente (dV/dPsi): {simplify(dV_dpsi)}")