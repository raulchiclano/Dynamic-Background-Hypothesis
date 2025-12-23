# REPORTE TÉCNICO: SIMULACIÓN 12
## Mapeo del Espacio de Parámetros de Energía Oscura (Plano CPL)

**Fecha:** 21/12/2025
**Tipo:** Validación Observacional (Fase 2.2 - Tarea 3)
**Código Fuente:** `sim_12_parameter_scan.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Determinar qué región del espacio de parámetros del Fondo Dinámico ($\alpha, \Psi_{init}$) es compatible con las observaciones cosmológicas actuales. Se utiliza la parametrización CPL ($w(a) = w_0 + w_a(1-a)$) para comparar las predicciones del modelo con los límites de confianza de Planck 2018 + BAO + SNe.

### 2. METODOLOGÍA
*   **Barrido de Parámetros:** Se simularon 225 universos variando la masa del campo ($\alpha$) y la condición inicial ($\Psi_{init}$).
*   **Extracción de Observables:** Para cada universo, se calculó la ecuación de estado actual $w_0$ y su tasa de evolución $w_a$.
*   **Confrontación:** Se graficaron los resultados en el plano $w_0 - w_a$ junto con las elipses de error observacionales.

### 3. RESULTADOS OBTENIDOS (Ver `fig_12_plano_cpl.png`)
1.  **Región Thawing:** Todos los modelos caen en la región de *Thawing Quintessence* ($w_0 \ge -1$), confirmando la estabilidad del vacío ($\beta > 0$).
2. **Compatibilidad:** Existe un subconjunto de parámetros (puntos oscuros/púrpuras, correspondientes a potenciales más rígidos $\alpha \lesssim -15$) que caen dentro de las barras de error de Planck ($w_0 \approx -1, w_a \approx 0$). Los puntos más claros (amarillos) representan la predicción de desviación para potenciales más suaves.
3.  **Huella Dactilar:** El modelo predice una correlación específica: desviaciones de $w_0 > -1$ van acompañadas de $w_a < 0$.

### 4. CONCLUSIÓN E IMPLICACIONES
El modelo del Fondo Dinámico es **observacionalmente viable**. No requiere ajustes finos extremos para coincidir con $\Lambda$CDM, pero predice desviaciones específicas que serán testables por misiones futuras como Euclid o DESI. Si se detectara $w < -1$ (Phantom) o $w_a > 0$ con $w_0 > -1$ (Freezing), el modelo en su forma actual quedaría descartado.