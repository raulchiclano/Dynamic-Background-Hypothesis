#!/usr/bin/env python3
# ppn_gamma_corrected.py
# Cálculo simbólico del parámetro PPN gamma a partir de la métrica acústica efectiva.
# Método: expandir en epsilon, extraer coeficientes constantes A,C y lineales B,D, 
# luego normalizar con factores independientes de tiempo y espacio:
#   g00_norm = -1 + (B*s_t)*epsilon
#   grr_norm =  1 + (D*s_x)*epsilon
# y gamma = (D*s_x) / |B*s_t|
#
# Evita division por cero y avisa si hay degeneraciones de parámetros.

import sympy as sp

def calculate_ppn_gamma_corrected():
    print("--- INICIANDO CÁLCULO PPN (GAMMA) - VERSIÓN CORREGIDA ---")

    # Símbolos
    r = sp.Symbol('r', positive=True)
    epsilon = sp.Symbol('epsilon', real=True)       # potencial débil (proporcional a GM/r)
    rho_0 = sp.Symbol('rho_0', positive=True)       # densidad de fondo > 0
    c_s = sp.Symbol('c_s', positive=True)           # velocidad de sonido local (>0)

    # Modelo de densidad perturbada (lineal en epsilon)
    # rho = rho_0 * (1 + 2*epsilon)  (como en tu planteamiento)
    rho = rho_0 * (1 + 2*epsilon)

    # Factor conforme Omega = rho / c_s (como en el ejemplo original)
    Omega = rho / c_s

    # Construcción de la métrica acústica simplificada (solo g00 y grr relevantes)
    # g00 = Omega * (c_s^-2 - 2)   (según el esquema previo)
    # grr = Omega * 1
    g00 = Omega * (c_s**(-2) - 2)
    grr = Omega * 1

    # Expandir en serie en epsilon hasta término lineal
    g00_series = sp.series(g00, epsilon, 0, 2).removeO().expand()
    grr_series = sp.series(grr, epsilon, 0, 2).removeO().expand()

    print(f"\nExpansiones (hasta O(epsilon)):\n g00 = {g00_series}\n grr = {grr_series}")

    # Obtener términos constantes (A,C) y lineales en epsilon (B,D)
    A = sp.simplify(sp.expand(sp.series(g00, epsilon, 0, 1).removeO()))
    C = sp.simplify(sp.expand(sp.series(grr, epsilon, 0, 1).removeO()))

    # Coeficientes lineales: extraer coeficiente de epsilon
    B = sp.simplify(sp.expand(g00_series).coeff(epsilon, 1))
    D = sp.simplify(sp.expand(grr_series).coeff(epsilon, 1))

    print(f"\nCoeficientes encontrados:")
    print(f" A = g00(0) = {A}")
    print(f" B = coef g00 (epsilon) = {B}")
    print(f" C = grr(0)  = {C}")
    print(f" D = coef grr (epsilon) = {D}")

    # Comprobaciones y normalizaciones:
    # Evitamos dividir por cero: A y C deben ser distintos de 0 para poder normalizar.
    # Si cualquiera es 0, damos mensaje y devolvemos símbolo que indica degeneración.
    zero = sp.Integer(0)

    if sp.simplify(A) == zero:
        print("\nERROR: A = g00(epsilon=0) es cero. No se puede normalizar temporalmente.")
        print("Sugerencia: revisar el valor simbólico de c_s (evitar c_s^2 = 1/2) o elegir otro gauge.")
        return sp.nan

    if sp.simplify(C) == zero:
        print("\nERROR: C = grr(epsilon=0) es cero. No se puede normalizar espacialmente.")
        print("Sugerencia: revisar parámetros del fondo.")
        return sp.nan

    # Normalización independiente:
    # s_t : factor para normalizar g00 constante a -1  => s_t = -1 / A
    # s_x : factor para normalizar grr constante a +1  => s_x =  1 / C
    s_t = sp.simplify(-1 / A)
    s_x = sp.simplify(1 / C)

    print(f"\nFactores de normalización:\n s_t (temporal) = {s_t}\n s_x (espacial) = {s_x}")

    # Coeficientes normalizados lineales:
    B_norm = sp.simplify(B * s_t)
    D_norm = sp.simplify(D * s_x)

    print(f"\nCoeficientes lineales normalizados:\n B_norm = {B_norm}\n D_norm = {D_norm}")

    # PPN identifica: g00 = -1 + 2 U  => coef temporal debería ser +2 (si epsilon = U)
    # y g_rr =  1 + 2 gamma U => gamma = (D_norm) / (2)  if B_norm == 2
    # Pero mejor: gamma = (D_norm) / |B_norm|  (proporcionalidad general)
    gamma = sp.simplify(D_norm / sp.Abs(B_norm))

    # Simplificar resultado
    gamma_simpl = sp.simplify(sp.together(sp.factor(gamma)))

    print(f"\nRESULTADO simbólico para gamma:\n gamma = {gamma_simpl}")

    # Evaluación: si gamma_simpl se puede simplificar a 1 por identidades algebraicas
    # devolvemos forma simplificada.
    return gamma_simpl

if __name__ == "__main__":
    gamma_val = calculate_ppn_gamma_corrected()
    print("\n========================================")
    print(f"RESULTADO FINAL (simbólico): GAMMA = {gamma_val}")
    print("========================================")
    