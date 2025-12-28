import sympy
from sympy import symbols, diff, simplify, solve, sqrt, pprint

# 1. Variables del fluido (No asumimos relatividad)
rho = symbols('rho', positive=True)
alpha, beta, sigma = symbols('alpha beta sigma', positive=True)
m = symbols('m', positive=True) # Masa constituyente del fluido (escala microscópica)

# 2. Definimos la Presión P(rho) a partir de nuestro potencial V(rho)
# P = rho * V' - V
V = alpha * rho + beta * rho**2 + sigma * rho**(sympy.Rational(3, 2))
P = simplify(rho * diff(V, rho) - V)

# 3. Calculamos la Compresibilidad (K) y la Velocidad del Sonido (cs)
# En hidrodinámica, cs^2 = dP / d_rho_masa
# Donde rho_masa = m * rho
cs_cuadrado = diff(P, rho) / m

print("--- SIMULACIÓN 19: DERIVACIÓN DE LA MÉTRICA ACÚSTICA ---")
print("\n1. Velocidad del sonido al cuadrado (cs^2) en el vacío:")
pprint(simplify(cs_cuadrado))

# 4. RELACIÓN DE DISPERSIÓN (Bogoliubov)
# Para un superfluido, la relación es: omega^2 = cs^2 * k^2 + (hbar^2 * k^4 / 4*m^2)
# El segundo término es la "Presión Cuántica" (Escala de Planck).
k, hbar = symbols('k hbar', positive=True)
omega_cuadrado = cs_cuadrado * k**2 + (hbar**2 * k**4 / (4 * m**2))

print("\n2. Relación de Dispersión Completa (omega^2):")
pprint(omega_cuadrado)

# 5. LÍMITE DE BAJA ENERGÍA (IR): k -> 0
# En este límite, el término k^4 desaparece.
omega_IR = sqrt(cs_cuadrado * k**2)

print("\n3. Límite de Baja Energía (Ondas de luz/gravedad):")
pprint(simplify(omega_IR))