# Experiment 5: Analysis of Bending Loss in Optical Fiber

## 1. Objective & Syllabus Linkage
**Objective**: To investigate the effect of macroscopic fiber bending on optical power loss across various bend radii and turn counts using an optical simulation model.

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
Macrobending loss occurs when the bend radius $R$ is small enough that the evanescent field tail in the cladding exceeds the local speed of light and radiates away:

$$\alpha_{\text{bend}} = c_1 \exp(-c_2 R)$$

Total macrobending attenuation increases linearly with the number of turns $N$:

$$A_{\text{bend}} (\text{dB}) = N \cdot \Delta P_{\text{turn}}(R)$$

Tight bends below the critical bend radius $R_c = \frac{3 n_1^2 \lambda}{4\pi(n_1^2 - n_2^2)^{3/2}}$ cause severe power leakage.

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    Source["Optical Source (1 kHz Sine Modulated, 850 nm)"] --> AttenBend["Optical Fiber with Macro-bending / Variable Attenuator"]
    AttenBend --> PowerMeter["Optical Power Meter"]
    AttenBend --> Scope["Electrical Oscilloscope / Visualizer"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp05_Fiber_Bending_Loss_Analysis.osd`](./Exp05_Fiber_Bending_Loss_Analysis.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **Sine Generator + CW Source** | Transmitters Library | Frequency 1 kHz, 1 V p-p, Wavelength 850 nm |
| **Optical Fiber (Bend Model)** | Optical Fibers Library | Macro-bend parameters (Radius 1-10 cm, Turns 1-5) |
| **Optical Power Meter** | Visualizers Library | Measures optical output power across bending tests |
| **Electrical Oscilloscope** | Visualizers Library | Observes sine-wave signal amplitude reduction |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Modulation Frequency | **1.0** | kHz |
| Operating Wavelength | **850** | nm |
| Bend Radii Tested | **1.0, 2.0, 3.0, 5.0, 10.0** | cm |
| Turn Counts (N) | **1, 2, 3, 5** | Turns |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp05_Fiber_Bending_Loss_Analysis.osd`](./Exp05_Fiber_Bending_Loss_Analysis.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Bending Condition | Optical Loss (dB) | Received Amplitude | Observation |
| --- | --- | --- | --- |
| Baseline (Straight) | 0.00 dB | 0.98 V p-p | Minimal intrinsic fiber loss |
| R = 10 cm, 1 Turn | 0.06 dB | 0.95 V p-p | Imperceptible macrobend loss |
| R = 5 cm, 1 Turn | 0.47 dB | 0.88 V p-p | Moderate bending loss |
| R = 2 cm, 1 Turn | 1.57 dB | 0.68 V p-p | Significant radiative leakage |
| R = 1 cm, 1 Turn | 2.35 dB | 0.57 V p-p | Severe radiation loss exceeding critical radius |
| R = 1 cm, 3 Turns | 7.05 dB | 0.19 V p-p | Substantial attenuation (~7 dB drop) |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp05_Bending_Loss.png)

---

## 7. Engineering Analysis & Conclusion
Measurements confirm an exponential decay of bending loss as bend radius expands. For high-density routing and patch panels, bend-insensitive fibers conforming to ITU-T G.657.A/B are essential to withstand radii down to 7.5-10 mm without signal degradation.

The simulation successfully validated the core physical principles of **Analysis of Bending Loss in Optical Fiber** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp05_Bending_Loss.png](./Exp05_Bending_Loss.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp05_Screenshot.png](./Exp05_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp05_Fiber_Bending_Loss_Analysis.osd`](./Exp05_Fiber_Bending_Loss_Analysis.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
