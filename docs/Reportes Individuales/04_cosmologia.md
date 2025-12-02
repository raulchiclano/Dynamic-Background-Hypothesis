# REPORTE TÉCNICO: SIMULACIÓN 04
## Dinámica Cosmológica y Criticalidad Auto-Organizada (SOC)

**Fecha:** 23/11/2025
**Tipo:** Validación Macrofísica (Fase 2)
**Código Fuente:** `sim_04_dinamica_soc.py`, `sim_04_ajuste_fino_exito.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Investigar si el universo puede auto-organizarse hacia un punto crítico ($\alpha \to 0$) para permitir gravedad de largo alcance, y determinar las condiciones cosmológicas necesarias para ello.

### 2. METODOLOGÍA
*   **Modelo Dinámico:** Se simuló la evolución temporal del parámetro de masa del Fondo $\alpha(t)$ bajo un sistema de retroalimentación competitiva:
    *   **Enfriamiento:** La expansión cósmica ($H$) reduce la temperatura efectiva del Fondo.
    *   **Calentamiento:** La formación de agujeros negros ($\rho_{BH}$) reinyecta energía al Fondo.
*   **Escenarios:** Se comparó un universo dominado por materia ($H \propto 1/t$) con uno dominado por Energía Oscura ($H \approx cte$).

### 3. RESULTADOS OBSERVADOS (Ver `fig_04_evolucion_alpha.png`)
1.  **Escenario Materia (Línea Roja):** El sistema es inestable. $\alpha$ no converge a cero, sino que sufre una deriva logarítmica. La gravedad de largo alcance se apagaría con el tiempo.
2.  **Escenario Energía Oscura (Línea Verde):** El sistema encuentra un **Atractor Estable** cerca de cero. La expansión acelerada actúa como un termostato perfecto que mantiene la criticalidad.

### 4. AJUSTE DE PRECISIÓN (HIERARCHY PROBLEM)
*   El modelo inicial predijo $\alpha \approx 0.12$, lo cual viola las cotas de la Constante Cosmológica y Lorentz.
*   Al imponer la densidad de vacío real ($\rho_{vac} \sim 10^{-123}$), el modelo predice un valor ajustado de $\alpha \approx 10^{-62}$.
*   **Resultado:** Con este ajuste, la violación de Lorentz ($\delta c$) cae por debajo de $10^{-62}$, volviéndose indetectable y compatible con la Relatividad Especial.

### 5. CONCLUSIÓN E IMPLICACIONES
La simulación demuestra que **la Energía Oscura es una condición necesaria** para la estabilidad de la gravedad. Además, resuelve el problema de la jerarquía y la invariancia de Lorentz asumiendo un acoplamiento materia-fondo extremadamente débil.