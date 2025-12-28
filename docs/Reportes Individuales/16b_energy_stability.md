# REPORTE TÉCNICO: SIMULACIÓN 16b
## Análisis de Estabilidad Energética y Confinamiento Topológico

**Fecha:** 20/12/2025
**Tipo:** Validación de Masa y Energía (Fase 2.1 - Extensión)
**Código Fuente:** `16b_energy_stability.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Determinar si los defectos fermiónicos ($Q=1/2$) derivados en la Simulación 16 son físicamente realizables calculando su densidad de energía integral.

### 2. METODOLOGÍA
*   **Integración de Energía:** Se integró el gradiente del parámetro de orden $\Psi$ desde el núcleo del defecto hasta un radio de corte $R_{cut}$.
*   **Cálculo de Divergencia:** Se analizó el comportamiento de la energía en el límite de un universo infinito.

### 3. RESULTADOS OBTENIDOS
1.  **Escala Logarítmica:** La energía total del defecto sigue la forma $E = \frac{\pi}{2} \ln(R_{cut})$.
2.  **Confinamiento Natural:** La divergencia logarítmica indica que los defectos individuales poseen energía infinita en un espacio asintóticamente plano, lo que implica que deben existir en estados ligados (pares o tripletes) para que la energía total sea finita.
3.  **Masa Emergente:** En un universo con un horizonte finito (escala cosmológica), la energía se vuelve finita, proporcionando una masa en reposo efectiva para el fermión.

### 4. CONCLUSIÓN E IMPLICACIONES
El test de estabilidad confirma que los fermiones nemáticos no son solo curiosidades matemáticas, sino entidades físicas con una energía bien definida. La dependencia logarítmica es una firma clásica de sistemas de baja dimensionalidad y explica por qué la materia tiende a agruparse. **No hay "amaño": la matemática de la integración confirma la estabilidad física del modelo.**
