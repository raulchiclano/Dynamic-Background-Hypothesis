import sympy as sp

def derive_mond_lagrangian():
    print("--- BÚSQUEDA DEL RÉGIMEN MOND (LAGRANGIANO EFECTIVO) ---")
    
    # 1. DEFINICIÓN DE CAMPOS Y PARÁMETROS
    # ------------------------------------
    # rho: Densidad del fluido
    # X: Término cinético de la fase X = (grad theta)^2 ~ (velocidad)^2 ~ (grad Phi)^2
    # alpha, beta: Parámetros del potencial (alpha < 0 para condensación, beta > 0 estabilidad)
    
    rho = sp.Symbol('rho', positive=True)
    X = sp.Symbol('X', positive=True) # X = (partial theta)^2
    alpha = sp.Symbol('alpha', real=True) # Asumiremos negativo después
    beta = sp.Symbol('beta', positive=True)
    
    # 2. LAGRANGIANO DE GROSS-PITAEVSKII (Representación Hidrodinámica)
    # -----------------------------------------------------------------
    # L = -1/2 (partial Psi)^2 - V(Psi)
    # En variables rho, theta:
    # L ~ -1/2 rho (partial theta)^2 - V(rho) - (términos gradiente rho despreciables en MOND)
    # Nota: El término cinético es rho * X.
    
    # Potencial V(rho) = alpha * rho + beta * rho^2
    V = alpha * rho + beta * rho**2
    
    # Lagrangiano Densidad
    L = -0.5 * rho * X - V
    
    print(f"Lagrangiano Original L(rho, X): {L}")
    
    # 3. ECUACIÓN DE MOVIMIENTO PARA RHO (Equilibrio Local)
    # -----------------------------------------------------
    # dL/drho = 0  (El fluido ajusta su densidad para minimizar acción)
    # -0.5 * X - dV/drho = 0
    
    dL_drho = sp.diff(L, rho)
    print(f"Ecuación de Estado (dL/drho = 0): {dL_drho} = 0")
    
    # Resolvemos para rho en función de X (velocidad/gravedad)
    rho_sol = sp.solve(dL_drho, rho)[0]
    print(f"Densidad de Equilibrio rho(X): {rho_sol}")
    
    # 4. LAGRANGIANO EFECTIVO L_eff(X)
    # --------------------------------
    # Sustituimos rho_sol en L para obtener una teoría solo para X (AQUAL)
    
    L_eff = L.subs(rho, rho_sol)
    L_eff = sp.simplify(L_eff)
    
    print(f"\nLagrangiano Efectivo L_eff(X): {L_eff}")
    
    # 5. ANÁLISIS DE COMPORTAMIENTO (Newton vs MOND)
    # ----------------------------------------------
    # Newtoniano: L ~ X (lineal en X, cuadrático en gradiente)
    # MOND profundo: L ~ X^1.5 (para dar fuerza 1/r)
    
    # Expandimos L_eff alrededor de X=0 (Baja aceleración? No, X es velocidad^2)
    # Ojo: En MOND, la transición ocurre a baja aceleración (gradiente de X).
    # Aquí buscamos la forma funcional.
    
    print("\n--- ANÁLISIS DE LA ESTRUCTURA ---")
    # L_eff tiene la forma A * (X + B)^2
    # Vamos a ver los términos.
    
    # Derivada dL_eff / dX (Esto es la "función dieléctrica" mu en MOND)
    # En Newton, dL/dX = constante.
    # En MOND, dL/dX depende de X.
    
    mu_function = sp.diff(L_eff, X)
    print(f"Función de respuesta mu(X) = dL_eff/dX: {mu_function}")
    
    return L_eff, mu_function

# Ejecutar
L_mond, mu_mond = derive_mond_lagrangian()