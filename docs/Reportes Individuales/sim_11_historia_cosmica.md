# REPORTE TÉCNICO: SIMULACIÓN 11
## Dinámica Cosmológica FLRW y Ecuación de Estado de la Energía Oscura

**Fecha:** 08/12/2025
**Tipo:** Validación Macrofísica (Fase 2.2 - Tarea 2)
**Código Fuente:** `sim_11_historia_cosmica.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Simular la evolución del factor de escala del universo $a(t)$ bajo la influencia del Fondo Dinámico. El objetivo es determinar si la presión del fluido ($\Psi$) emerge naturalmente como una Energía Oscura viable y caracterizar su Ecuación de Estado ($w = P/\rho$), parámetro crítico para confrontar el modelo con las observaciones de Supernovas y CMB.

### 2. METODOLOGÍA
*   **Modelo:** Ecuaciones de Friedmann acopladas a la ecuación de Klein-Gordon para un campo escalar con potencial de doble pozo ($V = \alpha \psi^2 + \beta \psi^4$) en un universo plano.
*   **Condiciones Iniciales:** Universo temprano ($z \approx 1000$) dominado por radiación y materia, con el campo $\Psi$ en régimen de "congelamiento por fricción de Hubble" (*Hubble friction*), desplazado ligeramente de su mínimo.
*   **Integración:** Resolución numérica del sistema de ecuaciones diferenciales ordinarias (ODEs) para obtener las densidades relativas $\Omega_i(z)$ y la evolución de $w(z)$.

### 3. RESULTADOS OBTENIDOS (Ver `fig_11_dinamica_energia_oscura.png`)
1.  **Historia Cósmica (Panel Izquierdo):** El modelo reproduce fielmente la secuencia cosmológica estándar: una larga era dominada por materia ($\Omega_m \approx 1$) seguida de una transición suave a la dominación del Fondo Dinámico ($\Omega_\Psi \to 1$) en tiempos cosmológicos recientes ($z < 0.7$).
2.  **Dinámica de $w$ (Panel Derecho):**
    *   **Régimen Asintótico ($z > 1$):** El campo permanece congelado, comportándose indistinguiblemente de una Constante Cosmológica ($w \approx -1$). Esto garantiza la compatibilidad con la Nucleosíntesis y el CMB.
    *   **Régimen Actual ($z \approx 0$):** Se observa un comportamiento de **"Thawing Quintessence"** (Quintaesencia descongelándose). El campo comienza a rodar por el potencial, elevando $w$ hacia valores menos negativos ($w > -1$).

### 4. CONCLUSIÓN E IMPLICACIONES
La simulación confirma que el Fondo Dinámico no es una constante estática, sino una **Energía Oscura Dinámica**.
*   **Viabilidad:** El modelo satisface las restricciones observacionales básicas de la expansión cósmica.
*   **Predictibilidad:** La desviación reciente de $w=-1$ es una firma observacional específica del modelo.
*   **Relevancia:** Al introducir una dinámica en la tasa de expansión reciente, el modelo ofrece grados de libertad adicionales necesarios para abordar anomalías como la **Tensión de Hubble**, rompiendo la rigidez del modelo $\Lambda$CDM estándar.

***

**ESTADO:** APROBADO PARA INCLUSIÓN EN EL DOCUMENTO MAESTRO v1.2.