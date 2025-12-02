# REPORTE TÉCNICO: SIMULACIÓN 06
## Emergencia de Fenómenos Cuánticos: Experimento de Doble Rendija

**Fecha:** 23/11/2025
**Tipo:** Validación Microfísica (Fase 3)
**Código Fuente:** `sim_06_doble_rendija.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Verificar si la dinámica clásica de un fluido (Fondo Dinámico) es capaz de reproducir fenómenos de interferencia ondulatoria característicos de la mecánica cuántica, validando la interpretación de "Onda Piloto" o hidrodinámica cuántica.

### 2. METODOLOGÍA
*   **Escenario:** Se construyó una barrera de potencial con dos rendijas gaussianas separadas.
*   **Partícula:** Se inyectó un paquete de ondas gaussiano (representando una partícula deslocalizada o su onda piloto asociada) dirigido hacia la barrera.
*   **Evolución:** Se utilizó la ecuación GPE para simular la propagación y difracción del campo a través de las rendijas.

### 3. RESULTADOS OBSERVADOS (Ver `fig_06_interferencia_cuantica.png`)
1.  **Difracción:** El paquete de ondas se divide al pasar por las rendijas, actuando cada una como una nueva fuente puntual (Principio de Huygens).
2.  **Interferencia:** En la región posterior a la barrera ($x > 5$), los frentes de onda provenientes de ambas rendijas se superponen.
3.  **Patrón de Franjas:** Se observa claramente la formación de máximos (zonas brillantes) y mínimos (zonas oscuras) de densidad. Este patrón de interferencia constructiva y destructiva es idéntico al predicho por la ecuación de Schrödinger lineal.

### 4. CONCLUSIÓN E IMPLICACIONES
La simulación demuestra que **la estadística cuántica emerge de la dinámica ondulatoria del Fondo**. Una partícula (vórtice) que viaje "surfeando" estas ondas será guiada preferentemente hacia las zonas de máxima densidad, reproduciendo la distribución de probabilidad cuántica sin necesidad de postular el colapso de la función de onda como un proceso mágico.