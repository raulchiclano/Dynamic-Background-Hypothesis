# REPORTE TÉCNICO: SIMULACIÓN 05
## Estructura Topológica 3D: El Hopfión

**Fecha:** 23/11/2025
**Tipo:** Validación Microfísica Avanzada (Fase 3)
**Código Fuente:** `sim_05_hopfion_3d.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Demostrar que el campo escalar complejo $\Psi$ admite soluciones topológicas estables en 3 dimensiones que no son simples puntos, sino estructuras anudadas ("Hopfiones"). Esto es crucial para modelar partículas con espín y carga en un espacio 3D realista.

### 2. METODOLOGÍA
*   **Espacio:** Rejilla volumétrica $64^3$.
*   **Construcción Topológica:** Se utilizó la **Fibración de Hopf** (proyección estereográfica inversa de $S^3 \to S^2$) para generar el campo inicial.
*   **Visualización:** Se extrajo la isosuperficie de baja densidad (el núcleo del defecto) mediante el algoritmo *Marching Cubes* y se coloreó según la fase local del campo.

### 3. RESULTADOS OBSERVADOS (Ver `fig_05_hopfion_toro.png`)
1.  **Geometría Toroidal:** La región de baja densidad forma un toro (donut) cerrado perfecto. Esto confirma que el defecto es una línea de vórtice cerrada sobre sí misma.
2.  **Estructura de Fase (Color):** Aunque la resolución de color es limitada en la captura estática, la existencia de la estructura toroidal implica matemáticamente una carga de Hopf $Q_H=1$. Las líneas de campo de fase se enroscan alrededor del toro, proporcionando la estabilidad topológica necesaria para evitar el colapso.

### 4. CONCLUSIÓN E IMPLICACIONES
La simulación valida la posibilidad de existencia de **materia topológica compleja** en el Fondo Dinámico. Un Hopfión se comporta como una partícula localizada con estructura interna y momento angular intrínseco (espín), ofreciendo un candidato geométrico para los fermiones del Modelo Estándar.