## Hipótesis del Fondo Dinámico (Dynamic Background Hypothesis)

[![Paper DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17714833.svg)](https://doi.org/10.5281/zenodo.17714833)

[![Software DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17800468.svg)](https://doi.org/10.5281/zenodo.17800468)

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

**Repositorio oficial de validación numérica y simbólica.**

Este repositorio contiene el código fuente, simulaciones y derivaciones matemáticas que acompañan a la propuesta teórica: *"Una unificación emergente de la Gravedad, la Mecánica Cuántica y la Cosmología a través de la Hidrodinámica del Vacío"*.

> **Note for international researchers:** An interactive English version of the results and simulations is available at [**lab.raulchiclano.es**](https://lab.raulchiclano.es).

## **Abstract**

We present the **Dynamic Background Hypothesis**, an effective field theory (EFT) framework where spacetime geometry, matter, and dark energy emerge from the hydrodynamics of a single relativistic complex scalar field $\Psi$. By modeling the vacuum as a superfluid condensate with nonlinear saturation, we demonstrate that the acoustic metric of the fluctuations naturally reproduces the phenomenology of General Relativity in the weak-field limit.

Analytic derivation of the Post-Newtonian parameters confirms that the model satisfies Solar System constraints with $\gamma_{PPN} = 1$, avoiding the need for screening mechanisms due to the high rigidity of the vacuum background ($\alpha \gg 10^{-30} \text{m}^{-2}$). Furthermore, we show that the effective Lagrangian exhibits a transition to a modified gravity regime (AQUAL-like) at low accelerations, offering a natural explanation for galactic rotation curves without particulate dark matter.

Numerical simulations of the Gross-Pitaevskii equation validate the stability of topological defects (vortices/Hopfions) as matter candidates and reproduce quantum interference phenomena via pilot-wave dynamics. Finally, a cosmological parameter space scan reveals that the model predicts a *thawing quintessence* equation of state ($w_0 \gtrsim -1, w_a < 0$), consistent with Planck 2018 constraints on Dark Energy. This framework provides a parsimonious unification of the dark sector and gravity within a scalar field ontology.

***

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
