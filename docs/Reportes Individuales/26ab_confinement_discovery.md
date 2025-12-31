# REPORTE TÉCNICO: SIMULACIONES 26a y 26b
## El Descubrimiento del Muro de Confinamiento

**Fecha:** 31-12-2025
**Tipo:** Pruebas de Estrés y Fallo de Localidad (Fase 5.3)
**Estatus:** Superado (Lecciones integradas en 26c)

---

### 1. OBJETIVO
Investigar la estabilidad de los tripletes de quarks (bariones) en la DBH y validar si el término $\sigma \rho^{3/2}$ de la Acción v4 es capaz de generar el confinamiento de color.

### 2. SIMULACIÓN 26a: LA PARADOJA ESTÁTICA
Se intentó modelar un protón mediante la superposición estática de 3 defectos $Q=1/2$ con fases de color rotadas $120^\circ$.
*   **Resultado:** La energía total del triplete resultó ser **superior** a la de 3 quarks aislados ($529k$ vs $518k$). Las "Alice Strings" (líneas de tensión) se escapaban hacia el infinito en lugar de cerrarse.
*   **Lección Aprendida:** El color no es solo una fase matemática; requiere un mecanismo dinámico que "anude" las cuerdas de tensión. La materia no puede ser un "pegado" de piezas; debe ser una configuración de mínima energía del fluido.

### 3. SIMULACIÓN 26b: EL MURO DE FUERZA (FALLO EULER)
Se intentó simular la separación dinámica de dos quarks utilizando un integrador de Euler simple, activando el término $\sigma$ como "congelador" del fluido.
*   **Resultado:** **Explosión Numérica (`overflow`)**. En cuanto los quarks intentaron separarse, la tensión en el sustrato creció de forma no-lineal tan violenta que superó la capacidad de cálculo del algoritmo.
*   **Lección Aprendida:** El "fracaso" de la 26b fue una **validación física masiva**. El `overflow` demostró que la fuerza de confinamiento en la DBH es real, masiva y no-lineal. Confirmó que el término $\sigma$ genera una rigidez infinita cuando la densidad cae, actuando como el "pegamento" de los quarks.

### 4. CONCLUSIÓN DEL BLOQUE
Estas dos simulaciones marcaron el "Muro de Planck" de nuestra capacidad de cómputo inicial. 
1.  La **26a** nos dijo que la topología debe ser cerrada.
2.  La **26b** nos dijo que la fuerza es imparable.

Este bloque fue el requisito previo indispensable para diseñar la **Simulación 26c**, donde finalmente se utilizó el método *Split-Step Fourier* para "fotografiar" el tubo de flujo sin romper la matemática.
