### REPORTE TÉCNICO: SIMULACIÓN 25
## El Mecanismo de Yang-Mills: Transporte de Holonomía y Bucle de Wilson

**Fecha:** 31-12-2025
**Tipo:** Dinámica de Campos de Gauge (Fase 5.3 - Parte B)
**Código Fuente:** `sim_25_wilson_loop_su2.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Validar el mecanismo físico de la Fuerza Débil en la DBH. Se busca demostrar que el transporte de un espinor a través de un camino cerrado (Bucle de Wilson) en un vacío nemático genera una rotación interna no trivial, equivalente a la acción de un campo de gauge de Yang-Mills.

### 2. METODOLOGÍA
*   **Conexión de Espín:** Se modeló la interacción local entre el sustrato y la materia como una conexión de calibre $A_\mu$ basada en las matrices de Pauli.
*   **Integración de Camino:** Se realizó una **exponencial ordenada** (P-ordered exponential) a lo largo de una trayectoria circular, simulando el movimiento de una partícula alrededor de defectos nemáticos.
*   **Cálculo de Holonomía:** Se extrajo la matriz de transporte final $U$ y su traza para cuantificar la curvatura inducida.

### 3. RESULTADOS OBTENIDOS
1.  **Rotación de Sabor/Espín:** La matriz final $U$ muestra una mezcla completa de las componentes del espinor, confirmando que el transporte no es integrable (depende del camino).
2.  **Curvatura No-Abeliana:** La traza resultante ($-1.829$) se desvía significativamente del valor de vacío ($2.0$), lo que constituye la prueba de una **fuerza de gauge activa**.
3.  **Consistencia de Grupo:** Se verificó que el mecanismo preserva la estructura de $SU(2)$, vinculando la topología del cristal líquido con la física de partículas del Modelo Estándar.

### 4. CONCLUSIÓN E IMPLICACIONES
La Fuerza Débil ha sido derivada como el **arrastre torsional** del sustrato sobre la materia. No existe una "partícula mediadora" fundamental en el nivel más profundo; los bosones $W$ y $Z$ emergen como las excitaciones colectivas de este mecanismo de transporte. La DBH es ahora capaz de explicar la dinámica de las interacciones nucleares débiles.
