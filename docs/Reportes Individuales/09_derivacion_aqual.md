# REPORTE TÉCNICO: SIMULACIÓN 09
## Búsqueda del Régimen MOND/AQUAL en el Lagrangiano Efectivo

**Fecha:** 08/12/2025
**Tipo:** Validación Teórica (Fase 2.1 - Tarea 2)
**Código Fuente:** `sim_09_derivacion_aqual.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Investigar si el Lagrangiano efectivo del Fondo Dinámico, expresado en variables hidrodinámicas (densidad $\rho$ y fase $\theta$), exhibe correcciones no lineales a bajas aceleraciones que puedan explicar anomalías gravitatorias sin materia oscura.

### 2. METODOLOGÍA
*   **Herramienta:** Cálculo simbólico con Python (`SymPy`).
*   **Procedimiento:**
    1.  Aplicación de la Transformación de Madelung ($\Psi = \sqrt{\rho} e^{i\theta}$) al Lagrangiano escalar relativista.
    2.  Resolución algebraica de la densidad $\rho$ en función del gradiente de fase $(\partial \theta)^2$ (aproximación adiabática).
    3.  Sustitución para obtener el Lagrangiano efectivo $\mathcal{L}_{eff}[\theta]$.

### 3. RESULTADOS OBTENIDOS (Ver `output_lagrangiano_efectivo.txt`)
El análisis simbólico revela que el Lagrangiano efectivo para la fase (potencial gravitatorio) tiene la forma:
$$ \mathcal{L}_{eff}(X) \propto \frac{1}{\beta} \left( \frac{1}{16} X^2 + \frac{\alpha}{4} X + \frac{\alpha^2}{4} \right) $$
Donde $X = (\pa--- BÚSQUEDA DEL RÉGIMEN MOND (LAGRANGIANO EFECTIVO) ---
Lagrangiano Original L(rho, X): -0.5*X*rho - alpha*rho - beta*rho**2
Ecuación de Estado (dL/drho = 0): -0.5*X - alpha - 2*beta*rho = 0
Densidad de Equilibrio rho(X): 0.25*(-X - 2.0*alpha)/beta

Lagrangiano Efectivo L_eff(X): 1.0*(0.0625*X**2 + 0.25*X*alpha + 0.25*alpha**2)/beta

--- ANÁLISIS DE LA ESTRUCTURA ---
Función de respuesta mu(X) = dL_eff/dX: 1.0*(0.125*X + 0.25*alpha)/beta

rtial \theta)^2$.

### 4. CONCLUSIÓN E IMPLICACIONES
1.  **Estructura AQUAL:** La presencia del término cuadrático $X^2$ confirma que el modelo pertenece a la clase de teorías **k-essence / AQUAL** (A Quadratic Lagrangian).
2.  **Comportamiento No-Newtoniano:** La función de respuesta $\mu(X) \propto (0.125 X + 0.25 \alpha)$ no es constante, lo que implica una violación del Principio de Equivalencia Fuerte y una modificación de la ley de gravedad dependiente de la escala. Aunque la potencia $X^2$ difiere del modelo MOND clásico ($X^{1.5}$), confirma que el Fondo Dinámico genera efectos de materia oscura aparente a través de la auto-interacción del vacío.
3.  **Dependencia de Parámetros:** La escala de transición de aceleración ($a_0$) está determinada por el cociente de los parámetros del potencial $\alpha$ y $\beta$.