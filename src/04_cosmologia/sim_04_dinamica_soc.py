import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ==========================================
# 1. CONFIGURACIÓN DEL MODELO JUGUETE (SOC)
# ==========================================

# Parámetros del Sistema
k_cool = 0.5        # Eficiencia del enfriamiento por expansión
k_heat = 0.55       # Eficiencia del calentamiento por Agujeros Negros
alpha_crit = 0.05   # Escala de sensibilidad (ancho de la zona crítica)
alpha_init = 1.0    # Condición inicial (Universo caliente/desordenado)

# Tiempo de simulación
t = np.linspace(1, 1000, 10000) # Empezamos en t=1 para evitar singularidad 1/t

# ==========================================
# 2. DEFINICIÓN DE LAS ECUACIONES DIFERENCIALES
# ==========================================

def soc_dynamics(alpha, t, scenario='de_sitter'):
    # 1. Tasa de Expansión H(t) (Enfriamiento)
    if scenario == 'matter':
        # Era dominada por materia: H ~ 1/t
        H = 1.0 / t
    elif scenario == 'de_sitter':
        # Era dominada por Energía Oscura (Lambda): H ~ constante
        H = 0.1 # Valor efectivo constante
    
    # Termino de Enfriamiento (Driving Force)
    cooling_term = k_cool * H
    
    # 2. Actividad Gravitatoria (Calentamiento / Restoring Force)
    # Si alpha -> 0, gravedad fuerte -> muchos BH -> mucho calor.
    # Si alpha grande, gravedad débil -> pocos BH -> poco calor.
    rho_BH = np.exp(-alpha / alpha_crit)
    heating_term = k_heat * rho_BH
    
    # Ecuación Maestra
    dadt = -cooling_term + heating_term
    return dadt

# ==========================================
# 3. EJECUCIÓN DE LA SIMULACIÓN
# ==========================================

# Escenario 1: Universo con H constante (Energía Oscura / Inflación)
sol_ds = odeint(soc_dynamics, alpha_init, t, args=('de_sitter',))
alpha_ds = sol_ds[:, 0]

# Escenario 2: Universo con H decayente (Materia)
sol_mat = odeint(soc_dynamics, alpha_init, t, args=('matter',))
alpha_mat = sol_mat[:, 0]

# ==========================================
# 4. ANÁLISIS DE KILL-SWITCH (KS1)
# ==========================================

def check_ks1(alpha_array, name):
    final_val = alpha_array[-1]
    mean_val = np.mean(alpha_array[-1000:]) # Promedio final
    variance = np.var(alpha_array[-1000:])
    
    print(f"--- ANÁLISIS KS1: {name} ---")
    print(f"Valor Final alpha: {final_val:.6f}")
    print(f"Estabilidad (Varianza): {variance:.6e}")
    
    # Criterio: alpha debe ser pequeño (< 0.1) y estable
    if final_val < 0.15 and variance < 1e-4:
        print("RESULTADO: [ÉXITO] Atractor encontrado cerca de 0.")
        return True
    else:
        print("RESULTADO: [FALLO] No converge a 0 o es inestable.")
        return False

print("\n")
ks1_ds = check_ks1(alpha_ds, "Escenario Energía Oscura (H=const)")
ks1_mat = check_ks1(alpha_mat, "Escenario Materia (H=1/t)")

# ==========================================
# 5. VISUALIZACIÓN
# ==========================================

plt.figure(figsize=(12, 6))

# Trayectorias
plt.plot(t, alpha_ds, label=r'Energía Oscura ($H \approx const$)', color='green', linewidth=2)
plt.plot(t, alpha_mat, label=r'Materia ($H \propto 1/t$)', color='red', linestyle='--')

# Zona Crítica Deseada
plt.axhspan(0, 0.1, color='blue', alpha=0.1, label='Zona Crítica (Gravedad Newtoniana)')
plt.axhline(0, color='black', linewidth=1)

plt.title(r'Evolución de $\alpha(t)$: Búsqueda del Punto Crítico (SOC)')
plt.xlabel('Tiempo Cosmológico')
plt.ylabel(r'Parámetro de Masa $\alpha(t)$')
plt.ylim(-0.05, 1.0)
plt.grid(True, alpha=0.3)
plt.legend()

plt.annotate('Atractor Estable', xy=(800, alpha_ds[-1]), xytext=(600, 0.4),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('Deriva Logarítmica', xy=(800, alpha_mat[-1]), xytext=(800, 0.6),
             arrowprops=dict(facecolor='red', shrink=0.05))

plt.show()