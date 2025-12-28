# REPORTE TÉCNICO: SIMULACIÓN 02
## Dinámica de Interacción entre Defectos Topológicos

**Fecha:** 23/11/2025
**Tipo:** Validación Microfísica (Fase 2)
**Código Fuente:** `sim_02_interaccion_pares.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Investigar si dos defectos topológicos ("partículas") inmersos en el Fondo Dinámico interactúan entre sí de forma espontánea, sin introducir potenciales de fuerza externos (como Coulomb o Newton).

### 2. METODOLOGÍA
*   **Configuración:** Se inicializó el campo $\Psi$ con dos vórtices de carga topológica idéntica ($Q_1=1, Q_2=1$) separados por una distancia $d=3.0$ unidades.
*   **Ansatz de Producto:** La función de onda inicial se construyó multiplicando los perfiles de densidad ($\tanh(r_1)\tanh(r_2)$) y sumando las fases ($\theta_1 + \theta_2$) para conservar la carga total $Q_{tot}=2$.
*   **Evolución:** Se aplicó relajación en tiempo imaginario para encontrar el estado fundamental de la configuración de dos cuerpos, seguido de evolución temporal real.

### 3. RESULTADOS OBSERVADOS (Ver `fig_02_dinamica_orbital.png`)
1.  **Densidad (Panel Izquierdo):** Se observan dos núcleos de densidad cero distintos. No se han fusionado en un solo defecto gigante, lo que confirma la repulsión a corto alcance o la estabilidad individual.
2.  **Fase (Panel Derecho):** El campo de fase muestra una estructura dipolar compleja. Las líneas de fase conectan ambos centros, indicando un flujo de velocidad compartido.
3.  **Dinámica:** La estructura de fase implica una velocidad tangencial no nula en la posición de cada vórtice inducida por el otro. Esto predice una rotación orbital mutua (interacción hidrodinámica).

### 4. CONCLUSIÓN E IMPLICACIONES
La simulación demuestra que **las fuerzas emergen de la hidrodinámica del medio**. No es necesario postular una "fuerza de gravedad" o "eléctrica" aparte; la simple presencia de dos defectos en un superfluido genera un campo de velocidades que los mueve. Esto valida el **Postulado 2.2** (Fuerzas como modos colectivos).