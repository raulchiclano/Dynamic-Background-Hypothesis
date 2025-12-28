import sympy
from sympy import symbols, Matrix, diff, simplify, cos, sin, pprint

# 1. Definimos las coordenadas y el tiempo
t, z = symbols('t z')
k, omega = symbols('k omega')

# 2. Definimos el Director Nemático n
# En equilibrio, el vacío está alineado con el eje Z: n0 = (0, 0, 1)
# Introducimos pequeñas perturbaciones nx, ny (oscilaciones de la luz)
nx = symbols('n_x')
ny = symbols('n_y')

# El director debe ser un vector unitario. Para pequeñas oscilaciones:
# n = (nx, ny, sqrt(1 - nx**2 - ny**2))
n = Matrix([nx, ny, sympy.sqrt(1 - nx**2 - ny**2)])

print("--- SIMULACIÓN 22: POLARIZACIÓN DE LA LUZ ---")
print("\n1. Director Nemático perturbado (n):")
pprint(n)

# 3. Verificación de Transversalidad
# Si la onda viaja en Z, la dirección de propagación es k_vec = (0, 0, 1)
k_vec = Matrix([0, 0, 1])

# Los modos de oscilación son las derivadas de n respecto a las perturbaciones
modo_x = n.diff(nx).subs({nx: 0, ny: 0})
modo_y = n.diff(ny).subs({nx: 0, ny: 0})

print("\n2. Modos de oscilación detectados:")
print("Modo 1 (Polarización X):")
pprint(modo_x)
print("Modo 2 (Polarización Y):")
pprint(modo_y)

# 4. PRUEBA DE FUEGO: ¿Son perpendiculares a la propagación?
dot_x = modo_x.dot(k_vec)
dot_y = modo_y.dot(k_vec)

print("\n3. Verificación de Transversalidad (Producto escalar con k):")
print(f"Modo X . k = {dot_x}")
print(f"Modo Y . k = {dot_y}")

if dot_x == 0 and dot_y == 0:
    print("\nÉXITO: Se han derivado 2 estados de polarización transversal pura.")
else:
    print("\nFALLO: Los modos tienen componentes longitudinales.")