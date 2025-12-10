## Hipótesis del Fondo Dinámico (Dynamic Background Hypothesis)

[![Paper DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17748410.svg)](https://doi.org/10.5281/zenodo.17714833)
[![Software DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17800468.svg)](https://doi.org/10.5281/zenodo.17800468)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

**Repositorio oficial de validación numérica y simbólica.**

Este repositorio contiene el código fuente, simulaciones y derivaciones matemáticas que acompañan a la propuesta teórica: *"Una unificación emergente de la Gravedad, la Mecánica Cuántica y la Cosmología a través de la Hidrodinámica del Vacío"*.

## Resumen del Proyecto

La **Hipótesis del Fondo Dinámico** postula que el espacio-tiempo no es una geometría vacía, sino un fluido físico (superfluido) en estado condensado. En este marco:
1.  **Materia:** Emerge como defectos topológicos (vórtices/nudos) estables.
2.  **Gravedad:** Emerge como gradientes de densidad/presión (métrica acústica).
3.  **Mecánica Cuántica:** Emerge de la hidrodinámica del medio (Onda Piloto).

Este repositorio presenta la **Prueba de Concepto (PoC)** computacional que valida la consistencia interna y fenomenológica del modelo.

**Current Version: v1.2 (Solar System Validated)**.

---

## Experimentos y Resultados

El proyecto se divide en 7 módulos de validación, utilizando la **Ecuación de Gross-Pitaevskii (GPE)** y cálculo tensorial simbólico.

### 1. Ontología de la Materia
*   **Simulación 01 (Estabilidad):** Se demuestra que un vórtice con carga topológica $Q=1$ es una solución estable y persistente en el Fondo, validando el modelo de "partícula como nudo".
*   **Simulación 02 (Interacción):** Dos vórtices interactúan dinámicamente generando fuerzas orbitales sin necesidad de potenciales externos.
*   **Simulación 05 (Topología 3D):** Generación exitosa de un **Hopfión** (estructura toroidal anudada) en 3D, candidato para modelar partículas con espín.

### 2. Gravedad Emergente
*   **Simulación 03 (Lente Gravitacional):** Se simula el paso de un fotón cerca de una región de baja densidad ("masa"). El resultado muestra la curvatura de la luz debido a la refracción hidrodinámica, reproduciendo cualitativamente la Relatividad General.
*   **Derivación 07 (Tensor de Einstein):** Cálculo simbólico (`SymPy`) que demuestra que la componente temporal del Tensor de Einstein derivado de la métrica acústica obedece a $G_{00} \propto \nabla^2 \rho$, recuperando la Ecuación de Poisson.

### 3. Mecánica Cuántica (Onda Piloto)
*   **Simulación 06 (Doble Rendija):** Reproducción del patrón de interferencia cuántica utilizando dinámica de fluidos clásica. La "partícula" es guiada por las ondas que ella misma genera al pasar por las rendijas.

### 4. Cosmología y Energía Oscura
*   **Simulación 04 (Criticalidad SOC):** Modelo dinámico que demuestra que la gravedad de largo alcance solo es estable en un universo con **Energía Oscura** (expansión acelerada). Se calcula el ajuste fino necesario ($\alpha \sim 10^{-62}$) para resolver el problema de la Constante Cosmológica.

---

## Estructura del Repositorio

*   `/docs`: Paper original (PDF) y Addendum Técnico detallado.
*   `/src`: Scripts de Python organizados por temática.
*   `/results`: Gráficas, capturas de simulación y salidas de texto.

## Instalación y Uso

Para reproducir las simulaciones, clone este repositorio e instale las dependencias:

```bash
git clone https://github.com/raulchiclano/Dynamic-Background-Hypothesis.git
cd Dynamic-Background-Hypothesis
pip install -r requirements.txt
```

* Ejemplo: Ejecutar la simulación de Lente Gravitacional:

```bash
python src/03_gravedad/sim_03_lente_gravitacional.py
```

## Citación
Si utiliza este material, por favor cite el trabajo original archivado en Zenodo:
>Chiclano Bleda, R. (2025). Hipótesis del Fondo Dinámico. Zenodo. https://doi.org/10.5281/zenodo.17714833

## Licencia y Derechos
Este trabajo está licenciado bajo Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0).
El código fuente se proporciona con fines de validación científica y reproducibilidad.
Autor: Raúl Chiclano Bleda
Contacto: raulchiclano@protonmail.com
