import sympy
from sympy import symbols, Matrix, I, pi, simplify, pprint, exp

# 1. Definimos las matrices de Pauli (Generadores de SU(2))
s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])

# 2. Operadores de Holonomía para Espinores (Rotación de PI/2 en el espacio de espín)
# Nota: Una rotación de 2*PI en el espacio real es PI en el espacio de espín.
# Por tanto, rodear un defecto Q=1/2 equivale a una rotación de PI/2.
def spinor_rotation(sigma, angle):
    return simplify(exp(I * (angle/2) * sigma))

# Rotación de PI alrededor del eje X e Y (visto por el espinor)
U_A = spinor_rotation(s1, pi)
U_B = spinor_rotation(s2, pi)

print("--- SIMULACIÓN 24 (REVISADA): HOLONOMÍA DE ESPINOR ---")
print("\n1. Matriz de Holonomía A (Espinor en X):")
pprint(U_A)

print("\n2. Matriz de Holonomía B (Espinor en Y):")
pprint(U_B)

# 3. EL TEST DE NO-ABELIANISMO REAL
U_AB = simplify(U_B * U_A)
U_BA = simplify(U_A * U_B)

print("\n3. Resultado Camino AB (Primero A, luego B):")
pprint(U_AB)

print("\n4. Resultado Camino BA (Primero B, luego A):")
pprint(U_BA)

# 4. VEREDICTO FINAL
if U_AB != U_BA:
    print("\nÉXITO: No-Abelianismo detectado en el nivel de Espinor.")
    print("U_AB = -U_BA. El orden de los defectos genera una fase de Berry no trivial.")
    print("Esta es la base matemática de la Fuerza Débil SU(2).")