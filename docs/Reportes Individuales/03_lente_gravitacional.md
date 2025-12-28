# REPORTE TÉCNICO: SIMULACIÓN 03
## Gravedad Emergente y Lentes Gravitacionales

**Fecha:** 23/11/2025
**Tipo:** Validación Macrofísica (Fase 2)
**Código Fuente:** `sim_03_lente_gravitacional.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Demostrar que la gravedad no requiere una curvatura geométrica fundamental, sino que puede explicarse como un fenómeno de **refracción hidrodinámica** en un medio de densidad variable. Se busca reproducir la desviación de la luz (Lente Gravitacional) predicha por la Relatividad General.

### 2. METODOLOGÍA
*   **Métrica de Fondo:** Se creó una región de baja densidad en el centro del fluido mediante un potencial externo estático ($V_{ext}$), simulando la presencia de una masa compacta (estrella/agujero negro).
*   **El Fotón:** Se inyectó un paquete de ondas gaussiano con momento lineal alto ($k$) pasando a una distancia de impacto $b$ del centro.
*   **Dinámica:** Se observó la evolución del paquete de ondas al atravesar el gradiente de densidad.

### 3. RESULTADOS OBSERVADOS (Ver secuencia de imágenes)
1.  **Panel Izquierdo (Métrica):** Muestra el "pozo" de densidad. Según la teoría ($c \propto \sqrt{\rho}$), la velocidad de propagación es menor en la zona oscura.
2.  **Panel Derecho (Trayectoria):**
    *   Al aproximarse al pozo, la parte del frente de onda más cercana al centro se ralentiza.
    *   Esto provoca un giro en el frente de onda (principio de Huygens).
    *   La trayectoria global del paquete se curva hacia la masa atractora, desviándose de la línea recta newtoniana (línea punteada).

### 4. CONCLUSIÓN E IMPLICACIONES
La simulación valida el **Postulado 2.3** (Gravedad como Hidrodinámica). La "atracción gravitatoria" sobre la luz es indistinguible de la refracción en un medio con índice de refracción variable. Esto confirma que la métrica acústica del Fondo Dinámico reproduce efectos relativistas clave.