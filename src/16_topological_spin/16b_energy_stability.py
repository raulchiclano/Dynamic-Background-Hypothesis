import sympy
from sympy import symbols, diff, integrate, pi, simplify, limit

r = symbols('r', positive=True)
R_cut = symbols('R_cut', positive=True) # Radio de la galaxia/celda
Q = sympy.Rational(1, 2)

# La energía de un vórtice (partícula) depende del gradiente de su fase
# E ~ integral ( (1/r * d_theta(Psi))**2 * r * dr * d_theta )
# Para un defecto topológico, el gradiente es Q/r

densidad_energia = (Q / r)**2

# Calculamos la energía total desde el núcleo (r=1) hasta el borde (R_cut)
energia_total = integrate(densidad_energia * r, (r, 1, R_cut)) * 2 * pi

print("--- TEST DE ESTABILIDAD DE LA MATERIA ---")
print(f"Energía total del defecto (Q=1/2): {simplify(energia_total)}")

# Verificación: ¿La energía diverge si el universo es infinito?
log_limit = limit(energia_total, R_cut, sympy.oo)
print(f"Comportamiento a larga distancia: {log_limit}")