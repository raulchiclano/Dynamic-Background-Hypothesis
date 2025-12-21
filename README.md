# Unified Emergent Gravity, Dark Energy, and Matter from a Relativistic Nematic Superfluid: The Dynamic Background Hypothesis (DBH)

[![Paper DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17714833.svg)](https://doi.org/10.5281/zenodo.17714833)
[![Version](https://img.shields.io/badge/Version-3.5--Technical--Update-gold)](https://doi.org/10.5281/zenodo.17990700)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

**Official repository for numerical and symbolic validation of the DBH framework.**

This repository contains the source code, simulations, and mathematical derivations for the **Dynamic Background Hypothesis**, a pre-geometric theory where spacetime, matter, and the dark sector emerge from the hydrodynamics of a relativistic nematic superfluid.

> **Note for international researchers:** An interactive English version of the results and simulations is available at [**lab.raulchiclano.es**](https://lab.raulchiclano.es).

---

## **Abstract (v3.5 Update)**

The **Dynamic Background Hypothesis (DBH)** proposes that the physical vacuum is a relativistic superfluid condensate described by a complex scalar field $\Psi$ with **nematic $Z_2$ symmetry** ($\Psi \equiv -\Psi$). 

In this framework:
1.  **Gravity** emerges as the acoustic metric of vacuum fluctuations. We provide an analytical derivation of the **MOND acceleration scale** $a_0 \propto (\sigma/\beta)^2$ from the vacuum's constitutive parameters, recovering General Relativity in the high-acceleration limit and AQUAL-like dynamics in the low-acceleration regime.
2.  **Matter** is identified as stable topological defects. We demonstrate that $Q=1/2$ defects (Half-Quantum Vortices) acquire a **Berry Phase of $\pi$** under rotation, providing a purely topological origin for fermionic spin-1/2 statistics.
3.  **Dark Energy** is the internal thermodynamic pressure of the condensate, predicting a *thawing quintessence* equation of state ($w_0 \gtrsim -1, w_a < 0$) consistent with Planck 2018 data.

---

## **Key Breakthroughs in v3.5**

*   **Analytical Closure of MOND:** Derivation of the transition density $\rho_c = \sigma^2/4\beta^2$, eliminating $a_0$ as a free parameter.
*   **Fermionic Emergence:** Proof of $\Psi \to -\Psi$ inversion under $2\pi$ rotation for nematic defects, bridging the gap between scalar fields and Fermi-Dirac statistics.
*   **Logarithmic Confinement:** Energy stability analysis confirming that $Q=1/2$ defects follow a $E \sim \ln(R)$ profile, providing a geometric basis for particle confinement and charge neutrality.

---

## **Repository Structure**

*   `/src/01_foundations`: Core symbolic derivations (Tensor $T_{\mu\nu}$, Field Equations).
*   `/src/02_gravity`: MOND scale derivation and PPN parameter validation.
*   `/src/03_matter`: Topological defect simulations and Berry Phase calculations.
*   `/src/04_cosmology`: CPL parameter space scans and FLRW dynamics.
*   `/docs`: Original Paper (v3.0) and the **Technical Update (v3.5)**.

---

## **Technical Validation Suite**

To reproduce the latest breakthroughs, run the following scripts:

| Script | Objective | Result |
| :--- | :--- | :--- |
| `14a_tensor_deriv.py` | Field Equations Variation | Validates $T_{\mu\nu}$ conservation. |
| `15_mond_scale.py` | Algebraic Solver for $a_0$ | Derives $\rho_c = \sigma^2/4\beta^2$. |
| `16_berry_phase.py` | Topological Rotation | Confirms $\pi$ phase (Fermionic Spin). |
| `16b_stability.py` | Energy Integration | Confirms Logarithmic Confinement. |

---

## **Installation**

```bash
git clone https://github.com/raulchiclano/Dynamic-Background-Hypothesis.git
cd Dynamic-Background-Hypothesis
pip install -r requirements.txt

```

## **Citation**
If you use this work or the provided code, please cite the Zenodo record:
> Chiclano Bleda, R. (2025). *Unified Emergent Gravity, Dark Energy, and Matter from a Relativistic Nematic Superfluid: The Dynamic Background Hypothesis (v3.5)*. Zenodo. https://doi.org/10.5281/zenodo.17714833

## **License**
This work is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.
The source code is provided for scientific validation and reproducibility purposes.

**Author:** Raúl Chiclano Bleda  
**Contact:** raulchiclano@protonmail.com
```

