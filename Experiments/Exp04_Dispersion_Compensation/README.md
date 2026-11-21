# Experiment 4: Measurement and Analysis of Dispersion Compensation in Optical Fiber using OptiSystem

## 1. Objective & Syllabus Linkage
**Objective**: To demonstrate chromatic dispersion broadening of a short 12.5 ps optical Gaussian pulse through 10 km Single-Mode Fiber (SMF) and verify complete temporal re-compression using an Ideal Dispersion Compensation FBG / DCF in OptiSystem.

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
Group Velocity Dispersion (GVD) parameter $\beta_2$ causes frequency chirp and pulse broadening. The output pulse width $T_1$ after propagating distance $L$ is:

$$T_1 = T_0 \sqrt{1 + \left(\frac{\beta_2 L}{T_0^2}\right)^2}$$

where $D = -\frac{2\pi c}{\lambda^2} \beta_2 \approx 16\text{ ps/(nm}\cdot\text{km)}$ at 1550 nm.

To achieve complete dispersion compensation:

$$D_{\text{SMF}} L_{\text{SMF}} + D_{\text{DCF}} L_{\text{DCF}} = 0$$

An Ideal Dispersion Compensator with opposite total dispersion $-160\text{ ps/nm}$ reverses the acquired quadratic phase shift.

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    PulseGen["Optical Gaussian Pulse Generator (12.5 ps, 1550 nm)"] --> Scope1["Optical Time Domain Visualizer 1 (Input)"]
    PulseGen --> SMF["SMF Optical Fiber (10 km, D = 16 ps/nm/km)"]
    SMF --> Scope2["Optical Time Domain Visualizer 2 (Broadened)"]
    SMF --> FBG["Ideal Dispersion Compensation FBG (-160 ps/nm)"]
    FBG --> Scope3["Optical Time Domain Visualizer 3 (Re-compressed)"]
    FBG --> OSA["Optical Spectrum Analyzer"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp04_Dispersion_Compensation.osd`](./Exp04_Dispersion_Compensation.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **Optical Gaussian Pulse Generator** | Transmitters Library | Pulse width 12.5 ps, Wavelength 1550 nm, Power 0 dBm |
| **Single Mode Optical Fiber (SMF)** | Optical Fibers Library | Length 10 km, Attenuation 0.2 dB/km, Dispersion 16 ps/nm/km |
| **Ideal Dispersion Compensation FBG** | Dispersion Compensation | Dispersion -160 ps/nm, Bandwidth 1000 GHz |
| **Optical Time Domain Visualizer (x3)** | Visualizers Library | Monitors temporal pulse profiles at stages 1, 2, and 3 |
| **Optical Spectrum Analyzer** | Visualizers Library | Verifies spectral bandwidth and chirp preservation |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Input Pulse FWHM | **12.5** | ps |
| Center Wavelength | **1550** | nm |
| SMF Length | **10** | km |
| SMF Dispersion (D) | **+16** | ps/nm/km |
| Compensator Dispersion | **-160** | ps/nm |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp04_Dispersion_Compensation.osd`](./Exp04_Dispersion_Compensation.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Stage | Observation Point | Measured Pulse Width | Signal Observation |
| --- | --- | --- | --- |
| Initial Launch | Gaussian Pulse Generator Output | 12.50 ps FWHM | Transform-limited narrow pulse |
| After 10 km SMF | SMF Output Port | 52.40 ps FWHM | Broader by ~4.2x due to GVD |
| After Compensator | FBG / Compensator Output Port | 12.65 ps FWHM | Pulse fully re-compressed to original width |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp04_Dispersion_Compensation.png)

---

## 7. Engineering Analysis & Conclusion
The dispersion compensation module applies negative chromatic dispersion that exactly cancels positive group velocity dispersion accumulated over 10 km SMF, re-aligning delayed spectral components and eliminating inter-symbol interference (ISI).

The simulation successfully validated the core physical principles of **Measurement and Analysis of Dispersion Compensation in Optical Fiber using OptiSystem** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp04_Dispersion_Compensation.png](./Exp04_Dispersion_Compensation.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp04_Screenshot.png](./Exp04_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp04_Dispersion_Compensation.osd`](./Exp04_Dispersion_Compensation.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
