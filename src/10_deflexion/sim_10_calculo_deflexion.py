import sympy as sp

def check_light_deflection_magnitude():
    print("--- TEST DE DEFLEXIÓN DE LUZ (MAGNITUD DE CORRECCIÓN) ---")
    
    # 1. PARÁMETROS FÍSICOS (Sistema Solar)
    # -------------------------------------
    # G = 1, c = 1 (Unidades naturales)
    # Masa del Sol M ~ 1.5 km (Radio de Schwarzschild / 2)
    # Radio del Sol R ~ 700,000 km
    # Potencial en la superficie: Phi ~ M/R ~ 10^-6
    # Gradiente al cuadrado: X = (grad Phi)^2 ~ (M/R^2)^2
    
    M = 1.5e3  # Metros (aprox)
    R = 7.0e8  # Metros
    X_solar = (M / R**2)**2
    
    print(f"Gradiente gravitatorio al cuadrado en el Sol (X_solar): {X_solar:.2e} m^-2")
    
    # 2. PARÁMETROS DE LA TEORÍA (Estimación)
    # ---------------------------------------
    # Del ajuste fino de la Fase 2 (Cosmología), sabemos que alpha es minúsculo (~10^-60 en Planck).
    # Pero aquí estamos en metros.
    # Vamos a dejar alpha y beta como simbólicos y ver la relación.
    
    X = sp.Symbol('X')
    alpha = sp.Symbol('alpha')
    beta = sp.Symbol('beta') # Factor global 1/beta se cancela en la métrica relativa
    
    # Lagrangiano derivado: L ~ 1/16 X^2 + alpha/4 X
    # (Ignoramos beta global y constante alpha^2)
    
    L = (1/16)*X**2 + (alpha/4)*X
    
    L_X = sp.diff(L, X)
    L_XX = sp.diff(L, X, 2)
    
    print(f"\nDerivada L_X  (Gravedad Newtoniana): {L_X}")
    print(f"Derivada L_XX (Corrección No Lineal): {L_XX}")
    
    # 3. RATIO DE CORRECCIÓN
    # ----------------------
    # La métrica efectiva es g_mn ~ L_X * eta_mn + L_XX * d_m phi d_n phi
    # El término newtoniano es L_X.
    # El término de corrección es L_XX * X (orden de magnitud).
    
    # Ratio = (Término Corrección) / (Término Newtoniano)
    # Ratio = (L_XX * X) / L_X
    
    ratio = (L_XX * X) / L_X
    print(f"Ratio de Corrección Algebraico: {ratio}")
    
    # 4. EVALUACIÓN NUMÉRICA
    # ----------------------
    # Si alpha domina (régimen newtoniano): Ratio -> 0
    # Si X domina (régimen no lineal): Ratio -> 1
    
    # Para que Einstein sea correcto, necesitamos Ratio << 1 en el Sol.
    # Esto implica alpha/4 >> 1/8 X_solar
    # alpha >> 0.5 * X_solar
    
    limit_alpha = 0.5 * X_solar
    print(f"\n--- CONDICIÓN DE ÉXITO ---")
    print(f"Para recuperar GR en el Sol, alpha debe ser mayor que: {limit_alpha:.2e}")
    print(f"(Recordemos: X_solar es muy pequeño, ~10^-11. Alpha debe ser mayor que eso).")
    
    return limit_alpha

# Ejecutar
limit = check_light_deflection_magnitude()