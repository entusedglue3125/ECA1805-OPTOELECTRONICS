# Experiment 3: Observation of Lower-Order LP Modes in Optical Fiber

## 1. Objective & Syllabus Linkage
**Objective**: To examine Linearly Polarized (LP) mode patterns (LP01, LP11, LP21, LP02) and spatial intensity distributions in multimode step-index optical fibers.

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
Under the weakly guiding approximation ($n_1 \approx n_2$), electromagnetic guided waves form Linearly Polarized modes designated $LP_{\ell m}$:

$$\psi(r, \phi) = J_\ell(u r / a) \cos(\ell \phi)$$

- $\ell = 0$ corresponds to circular symmetric modes ($LP_{01}$ fundamental mode, equivalent to $HE_{11}$).
- $\ell = 1$ yields two-lobe azimuthal patterns ($LP_{11}$, superpositions of $TE_{01}, TM_{01}, HE_{21}$).
- The cutoff condition occurs when the normalized transverse wavevector $u = V$.

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    Laser["Spatial CW Laser (He-Ne / 632.8 nm or 850 nm)"] --> InputField["Transverse Gaussian Beam"]
    InputField --> MMF["Multimode Step-Index Fiber (V > 2.405)"]
    MMF --> SpatialVis["Spatial Optical Visualizer"]
    SpatialVis --> ModeProfiler["Transverse Intensity Distribution (LP01, LP11)"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp03_Observation_Lower_Order_LP_Modes.osd`](./Exp03_Observation_Lower_Order_LP_Modes.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **Spatial CW Laser** | Multimode Transmitters | Wavelength 632.8 / 850 nm, Mode TEM00 |
| **Spatial Aperture / Offset** | Multimode Library | Transverse offset to excite higher-order LP modes |
| **Multimode Optical Fiber** | Optical Fibers Library | Core radius 25 µm, NA 0.20, V-number > 3.0 |
| **Spatial Optical Visualizer** | Visualizers Library | 2D/3D Intensity profile & beam diameter |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Core Radius (a) | **25** | µm |
| Relative Index Diff (Δ) | **0.01** | Dimensionless |
| V-number Range | **2.405 to 5.5** | Multimode excitation |
| Excited Modes | **LP01, LP11, LP21, LP02** | Weakly guiding modes |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp03_Observation_Lower_Order_LP_Modes.osd`](./Exp03_Observation_Lower_Order_LP_Modes.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| LP Mode Designation | Cutoff V-Number | Observed Spatial Pattern | Physical Characteristic |
| --- | --- | --- | --- |
| LP01 | 0.0 | Single central circular spot (bell curve) | Fundamental mode, no cutoff |
| LP11 | 2.405 | Two symmetrical intensity lobes with null line | First higher-order mode |
| LP21 | 3.832 | Four quadrant lobes with 90° symmetry | Degenerate quad mode |
| LP02 | 3.832 | Central circular core with outer concentric ring | Second radial symmetric mode |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp03_LP_Modes.png)

---

## 7. Engineering Analysis & Conclusion
Spatial visualizer contours confirm that selective spatial launch and beam offset couple optical energy into non-zero azimuthal order modes. Controlling V below 2.405 enforces strictly single-mode $LP_{01}$ propagation, eliminating intermodal dispersion.

The simulation successfully validated the core physical principles of **Observation of Lower-Order LP Modes in Optical Fiber** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp03_LP_Modes.png](./Exp03_LP_Modes.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp03_Screenshot.png](./Exp03_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp03_Observation_Lower_Order_LP_Modes.osd`](./Exp03_Observation_Lower_Order_LP_Modes.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
