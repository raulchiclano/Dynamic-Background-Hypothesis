import sympy as sp

def derive_einstein_tensor():
    # 1. CONFIGURACIÓN DE COORDENADAS Y CAMPOS
    # -----------------------------------------
    # Coordenadas (t, x, y, z)
    t, x, y, z = sp.symbols('t x y z')
    coords = [t, x, y, z]
    
    # Parámetros del Fondo
    # Asumimos límite estático: rho depende solo de la posición (x,y,z)
    # c_s (velocidad del sonido) lo tratamos como constante para ver el efecto de la densidad pura
    rho = sp.Function('rho')(x, y, z)
    c_s = sp.Symbol('c_s', positive=True) 
    
    # Factor Conforme: Omega = rho / c_s
    Omega = rho / c_s
    
    # Vector velocidad del fluido (Estático)
    # En firma Mostly Plus (-1, 1, 1, 1), la cuadrivelocidad en reposo es u = (1, 0, 0, 0)
    # Covariante u_mu = (-1, 0, 0, 0)
    v_mu = [-1, 0, 0, 0]
    
    # Métrica de Minkowski (Mostly Plus)
    eta = sp.diag(-1, 1, 1, 1)
    
    # 2. CONSTRUCCIÓN DE LA MÉTRICA ACÚSTICA
    # --------------------------------------
    # g_mn = Omega * [ eta_mn + (c_s^2 - 1) * v_m * v_n ]
    
    g = sp.zeros(4, 4)
    g_inv = sp.zeros(4, 4) # Necesitaremos la inversa para Christoffel
    
    print("Construyendo Tensor Métrico...")
    for mu in range(4):
        for nu in range(4):
            # Término delta (Minkowski)
            term_eta = eta[mu, nu]
            
            # Término velocidad
            term_v = (c_s**2 - 1) * v_mu[mu] * v_mu[nu]
            
            # Métrica completa
            g[mu, nu] = Omega * (term_eta + term_v)
            
    # Simplificación específica para g_00 y g_ii
    # g_00 = (rho/c_s) * (-1 + (c_s^2 - 1)*(-1)*(-1)) = (rho/c_s) * (c_s^2 - 2)
    # g_ii = (rho/c_s) * (1)
    
    # Inversa (Diagonal en este caso estático)
    for mu in range(4):
        g_inv[mu, mu] = 1 / g[mu, mu]

    # 3. CÁLCULO DE CURVATURA (FUERZA BRUTA)
    # --------------------------------------
    print("Calculando Símbolos de Christoffel (Gamma)...")
    # Gamma^k_ij = 0.5 * g^kl * (d_j g_il + d_i g_jl - d_l g_ij)
    Gamma = [sp.zeros(4, 4) for _ in range(4)]
    
    for rho_idx in range(4):
        for mu in range(4):
            for nu in range(4):
                res = 0
                for sigma in range(4):
                    term = sp.diff(g[nu, sigma], coords[mu]) + \
                           sp.diff(g[mu, sigma], coords[nu]) - \
                           sp.diff(g[mu, nu], coords[sigma])
                    res += 0.5 * g_inv[rho_idx, sigma] * term
                Gamma[rho_idx][mu, nu] = sp.simplify(res)

    print("Calculando Tensor de Ricci (R_mn)...")
    # R_mn = d_rho Gamma^rho_mn - d_nu Gamma^rho_mrho + ...
    Ricci = sp.zeros(4, 4)
    
    for mu in range(4):
        for nu in range(4):
            res = 0
            # Contracción del Riemann R^rho_m rho n
            for rho_idx in range(4):
                # Términos derivadas
                t1 = sp.diff(Gamma[rho_idx][mu, nu], coords[rho_idx])
                t2 = sp.diff(Gamma[rho_idx][mu, rho_idx], coords[nu])
                
                # Términos cuadráticos
                t3 = 0
                t4 = 0
                for lambda_idx in range(4):
                    t3 += Gamma[lambda_idx][mu, nu] * Gamma[rho_idx][rho_idx, lambda_idx]
                    t4 += Gamma[lambda_idx][mu, rho_idx] * Gamma[rho_idx][nu, lambda_idx]
                
                res += t1 - t2 + t3 - t4
            Ricci[mu, nu] = sp.simplify(res)

    print("Calculando Escalar de Ricci (R)...")
    R_scalar = 0
    for mu in range(4):
        for nu in range(4):
            R_scalar += g_inv[mu, nu] * Ricci[mu, nu]
    R_scalar = sp.simplify(R_scalar)
    
    print("Calculando Tensor de Einstein (G_00)...")
    # G_mn = R_mn - 0.5 * R * g_mn
    # Nos interesa G_00 para el límite newtoniano (Poisson)
    
    G_00 = Ricci[0, 0] - 0.5 * R_scalar * g[0, 0]
    G_00 = sp.simplify(G_00)
    
    return G_00, rho

# Ejecutar derivación
G_00_result, rho_sym = derive_einstein_tensor()

print("\n--- RESULTADO ANALÍTICO: COMPONENTE G_00 ---")
# Para mostrarlo limpio, sustituimos las derivadas parciales por Nabla
print("G_00 (proporcional a la densidad de energía efectiva):")
sp.pprint(G_00_result)