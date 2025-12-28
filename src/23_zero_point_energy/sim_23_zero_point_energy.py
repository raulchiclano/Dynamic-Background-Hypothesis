import sympy
from sympy import symbols, sqrt, integrate, pi, simplify, limit

# 1. Definimos las constantes físicas
k = symbols('k', positive=True) # Vector de onda (frecuencia espacial)
hbar = symbols('hbar', positive=True)
m = symbols('m', positive=True) # Masa constituyente del fluido
cs = symbols('c_s', positive=True) # Velocidad del sonido (Luz)
k_P = symbols('k_P', positive=True) # Corte de Planck (Límite UV)

# 2. Relación de Dispersión de Bogoliubov (Derivada en Sim 19)
# omega = sqrt( cs^2 * k^2 + (hbar * k^2 / 2m)^2 )
omega_k = sqrt(cs**2 * k**2 + (hbar * k**2 / (2 * m))**2)

# 3. Energía de Punto Cero por modo: E = 1/2 * hbar * omega
E_zpe_k = (hbar * omega_k) / 2

# 4. Densidad de Energía Total S (Integral en 3D: 4*pi*k^2 dk)
# S = integral de 0 a k_P de (E_zpe_k * k^2)
# Para simplificar la integral y ver la dependencia, analizamos el límite IR y UV
S_integral_expr = E_zpe_k * k**2

print("--- SIMULACIÓN 23: DERIVACIÓN DE LA INYECCIÓN S ---")
print("\n1. Expresión del integrando (Densidad espectral de S):")
sympy.pprint(simplify(S_integral_expr))

# 5. Cálculo del límite de alta energía (UV - Escala de Planck)
# En el límite k -> grande, domina el término k^2 de la presión cuántica
S_UV_approx = limit(S_integral_expr / k**4, k, sympy.oo)
print(f"\n2. Comportamiento en la Escala de Planck: S escala como k^4")

# 6. RELACIÓN CON LA ACCIÓN v4
# Sabemos que cs^2 es proporcional a beta * rho (Sim 19)
beta, rho = symbols('beta rho', positive=True)
cs_sq_val = (2 * beta * rho) / m

# Sustituimos para ver la dependencia final de S con la rigidez beta
S_final_dependence = simplify(S_UV_approx * k_P**5 / 5) # Aproximación de la integral
print("\n3. Dependencia fundamental de la inyección S:")
print(f"S es proporcional a (hbar^2 / m) * k_P^5")