import sympy
from sympy import symbols, Matrix, pi, simplify, pprint

# 1. Definimos las rotaciones de holonomía para defectos Q=1/2
# Un defecto Q=1/2 induce una rotación de PI (180 grados) en el espacio del director
# cuando completamos una vuelta de 2*PI en el espacio real.

def rotation_matrix(axis, angle):
    if axis == 'x':
        return Matrix([[1, 0, 0],
                       [0, sympy.cos(angle), -sympy.sin(angle)],
                       [0, sympy.sin(angle), sympy.cos(angle)]])
    if axis == 'y':
        return Matrix([[sympy.cos(angle), 0, sympy.sin(angle)],
                       [0, 1, 0],
                       [-sympy.sin(angle), 0, sympy.cos(angle)]])
    if axis == 'z':
        return Matrix([[sympy.cos(angle), -sympy.sin(angle), 0],
                       [sympy.sin(angle), sympy.cos(angle), 0],
                       [0, 0, 1]])

# 2. Operadores de Holonomía (Vuelta completa alrededor de cada defecto)
# Defecto A: Eje de rotación X
# Defecto B: Eje de rotación Y
U_A = rotation_matrix('x', pi)
U_B = rotation_matrix('y', pi)

print("--- SIMULACIÓN 24: HOLONOMÍA NO-ABELIANA ---")
print("\n1. Matriz de Holonomía Defecto A (Giro PI en X):")
pprint(U_A)

print("\n2. Matriz de Holonomía Defecto B (Giro PI en Y):")
pprint(U_B)

# 3. EL TEST DE NO-ABELIANISMO (Path Ordering)
# Camino 1: Primero A, luego B
U_AB = simplify(U_B * U_A)
# Camino 2: Primero B, luego A
U_BA = simplify(U_A * U_B)

print("\n3. Resultado Camino AB (Primero A, luego B):")
pprint(U_AB)

print("\n4. Resultado Camino BA (Primero B, luego A):")
pprint(U_BA)

# 4. VEREDICTO
if U_AB != U_BA:
    print("\nÉXITO: Holonomía No-Abeliana detectada.")
    print("El orden de interacción con los defectos altera el estado final.")
    print("Esto es la firma geométrica de la Fuerza Débil SU(2).")
    
    # Verificamos si la diferencia es una rotación en el tercer eje (Z)
    # El conmutador de rotaciones en X e Y genera una rotación en Z.
    diff = simplify(U_AB * U_BA.inv())
    print("\n5. Curvatura de Gauge Resultante (Rotación neta inducida):")
    pprint(diff)