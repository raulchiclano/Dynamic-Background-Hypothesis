# Unified Emergent Gravity, Dark Energy, and Matter from a Relativistic Nematic Superfluid: The Dynamic Background Hypothesis (DBH)

[![Paper DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17714833.svg)](https://doi.org/10.5281/zenodo.17714833)
[![Version](https://img.shields.io/badge/Version-3.5--Technical--Update-gold)](https://doi.org/10.5281/zenodo.17990700)
[![Latest Research](https://img.shields.io/badge/Latest-v4.0--Alpha--Research-red)](https://github.com/raulchiclano/Dynamic-Background-Hypothesis)

**Official repository for numerical and symbolic validation of the DBH framework.**

The **Dynamic Background Hypothesis (DBH)** is a pre-geometric theory where spacetime, matter, and the dark sector emerge from the hydrodynamics of a relativistic nematic superfluid vacuum ($\Psi$).

---

## **Milestone v3.5: The Analytical Foundation (Published)**
*This version provides the mathematical closure for the gravitational and matter sectors.*

*   **Analytical Closure of MOND:** Derivation of the transition density $\rho_c = \sigma^2/4\beta^2$, proving that the MOND acceleration scale $a_0$ is an emergent property of vacuum rheology, not a free parameter.
*   **Topological Origin of Fermions:** Proof that $Q=1/2$ nematic defects acquire a **Berry Phase of $\pi$** under rotation, deriving Fermi-Dirac statistics from a scalar sustrate.
*   **Logarithmic Confinement:** Energy stability analysis confirming that fermionic defects follow an $E \sim \ln(R)$ profile, explaining particle stability and charge neutrality.

---

## **Current Frontier: v4.0 Alpha (The Unified Field)**
*Ongoing research focused on the emergence of gauge fields and spacetime structure.*

*   **Emergent Electromagnetism (Sim 17):** Derivation of **Maxwell's Equations** from vacuum vorticity. The field tensor $F_{\mu\nu}$ and the Bianchi Identity emerge as topological necessities of the fluid flow.
*   **Lorentz Restoration (Sim 19-20):** Proof that **Lorentz Invariance** is the minimum energy state of the vacuum. We derive the speed of light $c$ from vacuum compressibility and quantify the "Spacetime Stiffness" ($K_L$) that prevents Lorentz violations.
*   **Spacetime Skeleton (Sim 18):** Emergence of the 4D Minkowski metric from the local alignment of nematic directors (Tetrads).

---

## **Technical Validation Suite**

| Milestone | Script | Objective | Result |
| :--- | :--- | :--- | :--- |
| **v3.5** | `15_mond_scale.py` | Algebraic Solver for $a_0$ | $\rho_c = \sigma^2/4\beta^2$ |
| **v3.5** | `16_berry_phase.py` | Topological Rotation | $\pi$ phase (Fermionic Spin) |
| **v4.0** | `17_gauge_emergence.py` | Maxwell Derivation | Bianchi Identity = 0 |
| **v4.0** | `19_dispersion.py` | Speed of Light Derivation | $\omega = ck$ (IR Limit) |
| **v4.0** | `20_lorentz_stiffness.py` | Lorentz Stability | Restoration Module $K_L$ |

---

## **Repository Structure**

The repository is organized to mirror the **DBH Roadmap** and the [Interactive Simulation Lab](https://lab.raulchiclano.es):

*   **`simulations/`**: Core interactive notebooks (`.ipynb`) categorized by research pillar:
    *   **Part I (Microphysics):** Topological defects and fermionic emergence (Sim 16).
    *   **Part II (Gravity & MOND):** Action v4 and galactic scale derivations (Sim 14, 15).
    *   **Part III (Cosmology):** FLRW dynamics and parameter space scans (Sim 12).
    *   **Part IV (Spacetime & Gauge):** Maxwell emergence and Lorentz restoration (Sim 17-20).
*   **`docs/`**: Official academic papers, including the **Original Paper (v3.0)** and the **Technical Update (v3.5)**.
*   **`requirements.txt`**: Python dependencies for symbolic and numerical validation.

---

## **Citation**
If you use this work, please cite the Zenodo record for the analytical foundation:
> Chiclano Bleda, R. (2025). *Unified Emergent Gravity, Dark Energy, and Matter from a Relativistic Nematic Superfluid: The Dynamic Background Hypothesis (v3.5)*. Zenodo. https://doi.org/10.5281/zenodo.17714833

---

## **License**
This work is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.
The source code is provided for scientific validation and reproducibility purposes.

**Author:** Raúl Chiclano Bleda  
**Contact:** raulchiclano@protonmail.com
```
