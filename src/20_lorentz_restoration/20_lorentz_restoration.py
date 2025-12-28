import sympy
from sympy import symbols, diff, simplify, series, pprint

# 1. Definimos las variables
et = symbols('e_t', positive=True)
epsilon = symbols('epsilon', real=True) # Desviación de Lorentz
alpha, beta, sigma = symbols('alpha beta sigma', positive=True)

# 2. Definimos la rigidez espacial con la desviación epsilon
es = et * (1 + epsilon)

# 3. Calculamos la densidad rho resultante
# rho = -et**2 + 3*es**2
rho = simplify(-et**2 + 3*es**2)

# 4. Potencial v4 completo
V = alpha*rho + beta*rho**2 + sigma*rho**(sympy.Rational(3, 2))

# 5. EXPANSIÓN DE TAYLOR (Análisis de pequeñas desviaciones)
# Queremos ver cómo aumenta la energía V cuando epsilon deja de ser 0.
# V(epsilon) = V(0) + V'(0)*epsilon + 1/2 * V''(0)*epsilon**2 + ...
V_series = series(V, epsilon, 0, 3).removeO()

print("--- SIMULACIÓN 20: COSTE ENERGÉTICO DE VIOLAR LORENTZ ---")
print("\n1. Densidad de energía V en función de la anisotropía (epsilon):")
pprint(simplify(V_series))

# 6. Cálculo del "Módulo de Restauración de Lorentz" (K_L)
# Es el coeficiente de epsilon**2. Si es positivo y grande, Lorentz es ultra-estable.
K_L = diff(V_series, epsilon, 2) / 2

print("\n2. Módulo de Restauración de Lorentz (Rigidez del Espaciotiempo):")
pprint(simplify(K_L))