import numpy as np

# ==========================================
# CONFIGURACIÓN: DATOS DE TU SIMULACIÓN ANTERIOR
# ==========================================

# Valor de equilibrio obtenido (Línea Verde)
# Usamos el valor final de tu ejecución exitosa
alpha_eq = 0.125  # Aproximado de tu gráfica/output
beta = 1.0        # Asumimos beta de orden 1 (saturación natural)

# ==========================================
# CÁLCULOS DE OBSERVABLES FÍSICOS
# ==========================================

def check_precision_physics(alpha, beta):
    print(f"--- ANÁLISIS DE PRECISIÓN (KS2 & KS3) para alpha = {alpha:.4f} ---")
    
    # 1. CÁLCULO DE LA CONSTANTE COSMOLÓGICA (KS2)
    # En unidades de Planck, la rho_vac observada es ~ 1e-123.
    # En tu modelo: rho_vac ~ alpha^2 / 4beta
    
    rho_vac_model = (alpha**2) / (4 * beta)
    rho_vac_obs = 1e-123
    
    print(f"\n[KS2] Energía del Vacío (Lambda):")
    print(f"  - Valor Modelo (Unidades Naturales): {rho_vac_model:.4e}")
    print(f"  - Valor Observado (Planck):          {rho_vac_obs:.1e}")
    
    # El "Problema de la Jerarquía": ¿Cuántos órdenes de magnitud fallamos?
    magnitude_error = np.log10(rho_vac_model) - np.log10(rho_vac_obs)
    print(f"  - Error de Magnitud: {magnitude_error:.1f} órdenes de magnitud.")
    
    if magnitude_error > 120:
        print("  -> RESULTADO KS2: [FALLO CATASTRÓFICO]")
        print("     (El vacío es demasiado denso, el universo colapsaría en microsegundos)")
    elif magnitude_error > 50:
        print("  -> RESULTADO KS2: [FALLO GRAVE]")
    else:
        print("  -> RESULTADO KS2: [ÉXITO/AJUSTABLE]")

    # 2. CÁLCULO DE VIOLACIÓN DE LORENTZ (KS3)
    # La violación delta_c suele escalar con alpha (la masa del modo Higgs).
    # Límites actuales (Fermi/LIGO): delta_c < 1e-15
    
    delta_c_model = alpha # Asunción de primer orden: acoplamiento directo
    delta_c_limit = 1e-15
    
    print(f"\n[KS3] Violación de Lorentz (delta_c):")
    print(f"  - Valor Modelo: {delta_c_model:.4e}")
    print(f"  - Límite Experimental: {delta_c_limit:.1e}")
    
    if delta_c_model > delta_c_limit:
        print("  -> RESULTADO KS3: [FALLO]")
        print("     (La luz de diferentes colores viajaría a velocidades muy distintas)")
    else:
        print("  -> RESULTADO KS3: [ÉXITO]")

# Ejecutar Test
check_precision_physics(alpha_eq, beta)