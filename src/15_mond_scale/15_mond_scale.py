import sympy
from sympy import symbols, diff, simplify, solve

# Definimos las constantes como variables abstractas (sin valores numéricos)
rho = symbols('rho', positive=True)
alpha, beta, sigma = symbols('alpha beta sigma', positive=True)

# 1. Definimos el Potencial v4 (Nuestra hipótesis)
V = alpha * rho + beta * rho**2 + sigma * rho**(sympy.Rational(3, 2))

# 2. Derivamos la Presión P (La fuerza física real)
# P = rho * V' - V
P = simplify(rho * diff(V, rho) - V)

# 3. Separamos los términos de la presión para ver quién manda
# El término de Newton/Einstein (Relatividad General)
P_GR = beta * rho**2 
# El término de MOND (Corrección de galaxias)
P_MOND = (sigma/2) * rho**(sympy.Rational(3, 2))

# 4. EL MOMENTO DE LA VERDAD: 
# Le pedimos a Python que encuentre el punto exacto donde P_GR y P_MOND 
# tienen la misma fuerza. Esto define la escala de transición a0.
rho_transicion = solve(P_GR - P_MOND, rho)

print("--- RESULTADO DEL SOLVER ALGEBRAICO ---")
print(f"La presión total derivada es: {P}")
print(f"El punto de transición (rho_c) calculado es: {rho_transicion}")