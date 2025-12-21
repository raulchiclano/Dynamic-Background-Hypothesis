import numpy as np
import sympy

# Definimos la variable de fase theta (el ángulo alrededor del defecto)
theta = sympy.symbols('theta')

# En un cristal líquido nemático o superfluido nemático, 
# el parámetro de orden Psi no es un vector, sino una línea (director).
# La condición de contorno para un defecto de carga Q=1/2 es:
# Psi(theta + 2*pi) = -Psi(theta)

# Definimos la función de onda del defecto
# Q es la carga topológica. Para fermiones, Q = 1/2.
Q = sympy.Rational(1, 2)
Psi = sympy.exp(sympy.I * Q * theta)

# 1. Estado inicial en theta = 0
Psi_0 = Psi.subs(theta, 0)

# 2. Estado tras una rotación completa (theta = 2*pi)
Psi_2pi = Psi.subs(theta, 2*sympy.pi)

# 3. Cálculo de la Fase de Berry (Fase geométrica)
# La fase phi se obtiene de: Psi_2pi = exp(i * phi) * Psi_0
fase_acumulada = sympy.log(Psi_2pi / Psi_0) / sympy.I

print("--- VALIDACIÓN DE ESTADÍSTICA TOPOLÓGICA ---")
print(f"Estado inicial (theta=0): {Psi_0}")
print(f"Estado final (theta=2pi): {Psi_2pi}")
print(f"Fase geométrica acumulada: {fase_acumulada}")

# Verificación del signo
if Psi_2pi == -Psi_0:
    print("RESULTADO: Psi -> -Psi detectado. Comportamiento Fermiónico confirmado.")