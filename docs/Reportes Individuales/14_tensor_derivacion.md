# REPORTE TÉCNICO: SIMULACIÓN 14
## Derivación Dinámica del Tensor Energía-Momento y Ecuaciones de Campo v4

**Fecha:** 20/12/2025
**Tipo:** Validación de Consistencia Dinámica (Fase 1.1)
**Código Fuente:** `14a_Tensor_Energia_Momento.py`

---

### 1. OBJETIVO DEL EXPERIMENTO
Extraer formalmente el Tensor Energía-Momento ($T_{\mu\nu}$) y la Ecuación de Movimiento (EOM) a partir de la **Acción v4**. El objetivo es asegurar que la introducción del término MOND ($\sigma \rho^{3/2}$) no rompa la conservación de la energía ni la simetría fundamental del sistema.

### 2. METODOLOGÍA
*   **Variación Funcional:** Se aplicó el formalismo de Euler-Lagrange sobre la densidad lagrangiana $\mathcal{L} = -\frac{1}{2} \partial_\mu \Psi \partial^\mu \Psi - V(\Psi)$.
*   **Potencial v4:** Se utilizó la forma unificada $V(\Psi) = \alpha \Psi^2 + \beta \Psi^4 + \sigma |\Psi|^3$.
*   **Cálculo Simbólico:** Uso de `sympy` para derivar el término de fuente $dV/d\Psi$ y la estructura de $T_{\mu\nu}$.

### 3. RESULTADOS OBTENIDOS
1.  **Tensor Energía-Momento:** Se confirmó la estructura:
    $$ T_{\mu\nu} = \partial_\mu \Psi \partial_\nu \Psi - g_{\mu\nu} \mathcal{L} $$
    Este resultado garantiza que el campo $\Psi$ se comporta como un fluido perfecto con presión y densidad bien definidas.
2.  **Ecuación de Campo (Klein-Gordon Modificada):**
    $$ \Box \Psi = 2\alpha\Psi + 4\beta\Psi^3 + 3\sigma\Psi|\Psi| $$
3.  **Preservación de Simetría:** El término de fuente es una función impar, lo que significa que la teoría es invariante bajo la transformación nemática $\Psi \to -\Psi$.

### 4. CONCLUSIÓN E IMPLICACIONES
La **Acción v4** es matemáticamente robusta. La dinámica derivada permite que el sistema transicione entre regímenes (Newton vs MOND) de forma suave. Se ha verificado que no existen singularidades matemáticas en el término de fuerza para $\Psi \neq 0$.
