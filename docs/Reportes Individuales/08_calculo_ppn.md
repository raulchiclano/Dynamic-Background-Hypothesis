# REPORTE TÉCNICO: SIMULACIÓN 08
## Cálculo del Parámetro Post-Newtoniano Gamma ($\gamma$)

**Fecha:** 08/12/2025
**Tipo:** Validación Analítica (Fase 2.1)
**Código Fuente:** `sim_08_calculo_ppn.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Determinar si la métrica acústica derivada del Fondo Dinámico es compatible con las pruebas de precisión de la Relatividad General en el Sistema Solar (deflexión de la luz). El criterio de éxito es obtener un valor para el parámetro PPN $\gamma$ cercano a 1.

### 2. METODOLOGÍA
*   **Herramienta:** Cálculo simbólico con Python (`SymPy`).
*   **Métrica de Entrada:** Métrica acústica efectiva $g_{\mu\nu}$ dependiente de la densidad $\rho$ y la velocidad del sonido $c_s$.
*   **Procedimiento:**
    1.  Expansión en serie de Taylor de los componentes $g_{00}$ y $g_{rr}$ en función del potencial gravitatorio adimensional $\epsilon \sim GM/r$.
    2.  Normalización de los coeficientes para recuperar el límite de campo débil.
    3.  Cálculo del ratio $\gamma = \frac{g_{rr}^{(1)}}{g_{00}^{(1)}}$.

### 3. RESULTADOS OBTENIDOS (Ver `output_gamma_1.txt`)
El cálculo simbólico arrojó el siguiente resultado exacto:
$$ \gamma = 1 $$

### 4. CONCLUSIÓN E IMPLICACIONES
El resultado $\gamma = 1$ indica que la teoría predice la **misma curvatura espacial por unidad de masa** que la Relatividad General de Einstein.
*   Esto garantiza que el modelo pasa los tests clásicos: deflexión de la luz, retraso de Shapiro y precesión del perihelio (a primer orden).
*   Valida la viabilidad del Fondo Dinámico como teoría gravitatoria en el régimen del Sistema Solar.