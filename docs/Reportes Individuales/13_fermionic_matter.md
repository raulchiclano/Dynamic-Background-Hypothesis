# REPORTE TÉCNICO: SIMULACIÓN 13
## Emergencia de Estadística Fermiónica (Espín 1/2) en el Fondo Dinámico

**Fecha:** 21/12/2025
**Tipo:** Validación Microfísica Avanzada (Fase 3)
**Código Fuente:** `sim_13a`, `sim_13b`, `sim_13c`

---

### 1. OBJETIVO DEL EXPERIMENTO
Determinar si los defectos topológicos del Fondo Dinámico pueden exhibir estadísticas fermiónicas (cambio de signo de la función de onda bajo rotación de $360^\circ$, fase de Berry $\pi$), superando la limitación bosónica de los campos escalares simples.

### 2. METODOLOGÍA
Se realizaron tres experimentos numéricos progresivos:
1.  **13a (Hopfión Escalar):** Rotación adiabática de un solitón toroidal en un campo escalar simple.
2.  **13b (Espinor Rígido):** Rotación de un defecto tipo Skyrmion en un campo espinorial sin estructura interna.
3.  **13c (Aharonov-Bohm Dual):** Transporte de un paquete de ondas alrededor de un defecto con carga fraccionaria ($Q=1/2$), posible solo si el vacío posee simetría nemática ($Z_2$).

### 3. RESULTADOS OBTENIDOS
1.  **Hopfión Escalar:** La fase acumulada fue $2\pi$. El defecto se comporta como un **Bosón** (espín entero).
2.  **Espinor Rígido:** La fase acumulada fue $\approx 1.88\pi$. No se logró el comportamiento fermiónico puro debido al acoplamiento rígido.
3.  **Vórtice de Medio Cuanto (HQV):** La fase acumulada fue exactamente **$\pi$**.
    *   Esto implica que la función de onda cambia de signo ($\Psi \to -\Psi$) al completar una vuelta.
    *   Este comportamiento es la firma definitoria de un **Fermión (Espín 1/2)**.

### 4. CONCLUSIÓN E IMPLICACIONES
La simulación demuestra que la materia fermiónica puede emerger del Fondo Dinámico **si y solo si** el vacío posee una estructura **Nemática** (simetría de inversión).
*   Los fermiones fundamentales se identifican con defectos de carga $Q=1/2$.
*   Los bosones gauge se interpretan como estados compuestos de pares de fermiones ($1/2 + 1/2 = 1$).