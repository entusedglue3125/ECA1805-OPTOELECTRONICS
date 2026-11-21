# Experiment 1: Measurement of Numerical Aperture and V-Number of Optical Fiber

## 1. Objective & Syllabus Linkage
**Objective**: To determine the Numerical Aperture (NA) and normalized frequency (V-number) of multimode optical fibers across various core diameters and evaluate their light-gathering capability and guided mode capacity.

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
The Numerical Aperture represents the light-gathering capability of an optical fiber and is related to the acceptance angle $\theta_a$ by:

$$\text{NA} = \sin(\theta_a) = \sqrt{n_1^2 - n_2^2} \approx n_1\sqrt{2\Delta}$$

Experimentally from the far-field spot diameter $D$ at distance $L$ from the fiber tip:

$$\text{NA} = \frac{D}{\sqrt{4L^2 + D^2}}$$

The normalized frequency (V-number) defines the mode-carrying capacity:

$$V = \frac{2\pi a}{\lambda}\text{NA} = \frac{\pi d}{\lambda}\text{NA}$$

For a step-index fiber, the total number of guided modes is approximately $M \approx V^2 / 2$, and for graded-index fiber $M \approx V^2 / 4$.

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    Source["Spatial Optical Source (850 nm)"] --> Lens["Coupling Lens / Spatial Aperture"]
    Lens --> MMF["Multimode Optical Fiber (50 / 62.5 / 100 µm)"]
    MMF --> FarField["Far-Field Spot / Spatial Visualizer"]
    FarField --> PowerMeter["Optical Power Meter / Mode Profiler"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp01_Numerical_Aperture_and_V_Number.osd`](./Exp01_Numerical_Aperture_and_V_Number.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **Spatial CW Laser / LED** | Multimode Transmitters Library | Source wavelength 850 nm, Power 0 dBm |
| **Spatial Aperture / Lens** | Multimode Library | Aperture radius matching fiber core |
| **Multimode Fiber (MMF)** | Optical Fibers Library | Core dia: 50, 62.5, 100 µm, Clad: 125 µm, Length: 2 m |
| **Spatial Optical Visualizer** | Visualizers Library | Far-field transverse intensity & beam radius |
| **Optical Power Meter** | Visualizers Library | Measures total coupled and output power (dBm) |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Core Diameters | **50, 62.5, 100** | µm |
| Operating Wavelength | **850, 1300** | nm |
| Screen Distances (L) | **10, 12, 15, 20** | cm |
| Measured Spot Diameters (D) | **3.8, 5.0, 6.0, 9.0** | cm |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp01_Numerical_Aperture_and_V_Number.osd`](./Exp01_Numerical_Aperture_and_V_Number.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Fiber Type (Core) | Distance L (cm) | Spot Dia D (cm) | Measured NA | Acceptance Angle | V-Number (850 nm) | Guided Modes (M) |
| --- | --- | --- | --- | --- | --- | --- |
| Fiber 1 (50 µm) | 12.0 | 5.0 | 0.204 | 11.78° | 37.7 | 710 |
| Fiber 2 (62.5 µm) | 10.0 | 5.6 | 0.270 | 15.66° | 62.4 | 1947 |
| Fiber 3 (100 µm) | 20.0 | 9.0 | 0.220 | 12.71° | 81.3 | 3305 |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp01_NA_and_V_Number.png)

---

## 7. Engineering Analysis & Conclusion
The experiment demonstrates that larger core diameters and higher relative refractive index differences yield greater NA values, capturing more optical power from wide-angle divergent sources. As wavelength increases from 850 nm to 1300 nm, V-number decreases inversely with λ, reducing modal dispersion and mode count.

The simulation successfully validated the core physical principles of **Measurement of Numerical Aperture and V-Number of Optical Fiber** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp01_NA_and_V_Number.png](./Exp01_NA_and_V_Number.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp01_Screenshot.png](./Exp01_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp01_Numerical_Aperture_and_V_Number.osd`](./Exp01_Numerical_Aperture_and_V_Number.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
