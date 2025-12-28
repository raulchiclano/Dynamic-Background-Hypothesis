import sympy
from sympy import symbols, diff, simplify, Matrix, pprint

# 1. Definimos las rigideces (et: temporal, es: espacial)
et, es = symbols('e_t e_s', positive=True)
alpha, beta = symbols('alpha beta', positive=True)

# 2. Métrica emergente y Densidad rho
# rho es la traza de la métrica en el sustrato
rho = -et**2 + 3*es**2

# 3. Potencial v4 (Límite de vacío)
V = alpha*rho + beta*rho**2

# 4. Derivamos las Presiones (Componentes del Tensor Energía-Momento)
# En el vacío, la presión es la derivada de la energía respecto al volumen (escala)
P_temporal = diff(V, et) / (2*et)
P_espacial = diff(V, es) / (2*es)

print("--- SIMULACIÓN 18c (REVISADA): EQUILIBRIO DE PRESIONES ---")

print("\n1. Presión en el eje Temporal (P_t):")
pprint(simplify(P_temporal))

print("\n2. Presión en el eje Espacial (P_s):")
pprint(simplify(P_espacial))

# 5. LA PRUEBA DE FUEGO:
# Para que el vacío sea Lorentz-Invariante, P_t debe ser igual a -P_s 
# (Condición de fluido perfecto w = -1)
balance = simplify(P_temporal + P_espacial)

print("\n3. Balance de Presiones (P_t + P_s):")
pprint(balance)

# 6. Buscamos la condición para que el balance sea cero
condicion_c = sympy.solve(balance, es/et)
print("\n4. Relación es/et requerida para el equilibrio (Velocidad de la luz c):")
pprint(condicion_c)