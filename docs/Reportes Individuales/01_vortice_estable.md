# REPORTE TÉCNICO: SIMULACIÓN 01
## Estabilidad de Defectos Topológicos en el Fondo Dinámico

**Fecha:** 23/11/2025
**Tipo:** Validación Microfísica (Fase 2)
**Código Fuente:** `sim_01_vortice_estable.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Verificar computacionalmente si el **Fondo Dinámico** (modelado como un superfluido mediante la ecuación de Gross-Pitaevskii) es capaz de sostener estructuras localizadas estables ("partículas") sin que se disipen en el medio.

### 2. METODOLOGÍA
*   **Modelo Matemático:** Ecuación de Gross-Pitaevskii (GPE) adimensional con término de interacción no lineal ($g|\Psi|^2$).
*   **Método Numérico:** Split-Step Fourier (Espectral) para garantizar la conservación de la norma y la estabilidad.
*   **Técnica de Estabilización:** Se aplicó una evolución en **Tiempo Imaginario** ($t \to -it$) inicial para enfriar el sistema y encontrar el estado fundamental numérico, eliminando ondas de choque espurias.
*   **Condición Inicial:** Un vórtice con carga topológica $Q=1$ (Ansatz de fase singular).

### 3. RESULTADOS OBSERVADOS (Ver `fig_01_densidad_fase.png`)
1.  **Densidad (Panel Izquierdo):** Se observa un "agujero" o núcleo de densidad cero perfectamente definido y estable en el centro del fluido. No hay difusión ni colapso de la estructura.
2.  **Fase (Panel Derecho):** Se observa un patrón de gradiente de fase azimutal ("molinillo") que converge en una singularidad central. Esto confirma la naturaleza topológica del defecto.

### 4. CONCLUSIÓN E IMPLICACIONES
La simulación demuestra que **la materia puede emerger como un defecto topológico estable** (solitón) dentro del Fondo Dinámico. Esto valida el **Postulado 2.1** del Documento Maestro: la materia no necesita ser introducida como un cuerpo externo, sino que es una configuración anudada del propio vacío.