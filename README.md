# The Dynamic Background Hypothesis (DBH) v4.0 Beta
## A Unified Pre-Geometric Theory of Gravity, Matter, and Homeostatic Cosmology

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17714833.svg)](https://doi.org/10.5281/zenodo.17714833)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

### 1. Overview
The **Dynamic Background Hypothesis (DBH)** is a unified field theory that models the physical vacuum as a **relativistic nematic superfluid substrate**. Unlike standard models that treat spacetime as a passive stage, the DBH derives geometry, matter, and forces as collective excitations of this active medium.

The v4.0 Alpha release marks a paradigm shift from force-based dynamics to **stability-based homeostasis**.

The **v4.0 Beta** release completes the unification of the electromagnetic and thermodynamic sectors, providing a self-consistent explanation for the "Dark Sector", the origin of fermionic matter, and the vector nature of light without free parameters.

---

### 2. Key Breakthroughs (v4.0 Beta Update)
*   **Unified Action v4:** Analytical derivation of the MOND scale ($a_0$) from vacuum rheology.
*   **Emergent Electromagnetism:** Proof of Maxwell’s equations as the topological vorticity of the vacuum flow.
*   **Photon Polarization:** Symbolic proof of the **vector nature of light** (two transverse modes) derived from nematic director oscillations.
*   **Lorentz Invariance as Equilibrium:** Derivation of the Minkowski metric as the minimum energy state of the substrate.
*   **Homeostatic Cosmology:** Discovery of a stable attractor in the matter-background phase space.
*   **Zero-Point Energy Derivation:** Elimination of the last free parameter ($S$) by deriving vacuum injection from **Bogoliubov quantum fluctuations**.

---

### 3. Repository Structure
The validation of the hypothesis is performed through symbolic tensor calculus (`SymPy`) and numerical simulations (`NumPy/SciPy`). The source code is organized by physical domain:

*   **`/src`**: Python scripts for numerical and symbolic validation.
    *   `01_materia/`: Vortex stability simulations (GPE).
    *   `02_interaccion/`: Vortex pair dynamics.
    *   `03_gravedad/`: Gravitational lensing and acoustic metric.
    *   `04_cosmologia/`: Cosmic history and Dark Energy equation of state.
    *   `05_topologia_3d/`: 3D Hopfion structures.
    *   `06_cuantica/`: Double-slit interference (Pilot Wave).
    *   `07_matematica/`: Symbolic derivation of the Einstein Tensor.
    *   `13_fermiones_topologicos/`: Berry Phase and Spin-1/2 emergence.
    *   `14_Tensor-Energía-Momento/`: Derivation of Action v4 and MOND scale ($a_0$).
    *   `17_gauge_emergence/`: Emergence of Maxwell's equations from vorticity.
    *   `20_lorentz_restoration/`: Lorentz restoration mechanism.
    *   `21_termodinamica_homeostatica/`: Global attractor and gravitational genesis simulations.
    *   `22_photon_polarization/`: **[NEW]** Validation of transverse oscillation modes.
    *   `23_zero_point_energy/`: **[NEW]** Analytical derivation of the $S$ injection term.

*   **`/docs`**: Theoretical documentation.
    *   `DBH_v4.0_Beta_Manifesto.pdf`: The definitive paper.
    *   `Addendum_Tecnico_Validacion.md`: Detailed technical report.

*   **`/results`**: Generated plots and output logs for all simulations.

---

### 4. Quick Start
To replicate the results, ensure you have Python 3.10+ installed with the following dependencies:
```bash
pip install numpy matplotlib scipy sympy
```
Run the core stability test:
```bash
python3 src/21_termodinamica_homeostatica/sim_21a_Homeostasis.py
```

---

### 5. Documentation & Paper
*   **Full Paper (v4.0 Beta):** Available on [Zenodo](https://doi.org/10.5281/zenodo.17714833).
*   **Research Hub:** Interactive notebooks and detailed theory at [lab.raulchiclano.es](https://lab.raulchiclano.es).

---

### 6. Citation
If you use this work, please cite the Zenodo record for the analytical foundation:
> Chiclano Bleda, R. (2025). *The Dynamic Background Hypothesis v4.0 Beta: A Unified Pre-Geometric Theory of Gravity, Matter, and Homeostatic Cosmology*. Zenodo. https://doi.org/10.5281/zenodo.17714833

---

### 7. License
This work is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.
The source code is provided for scientific validation and reproducibility purposes.

**Author:** Raúl Chiclano Bleda  
**Contact:** raulchiclano@protonmail.com
