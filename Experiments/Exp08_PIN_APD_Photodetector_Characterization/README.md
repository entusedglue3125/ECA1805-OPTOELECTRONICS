# Experiment 8: Characterization of PIN and APD Photodetectors

## 1. Objective & Syllabus Linkage
**Objective**: To determine the dark current, photocurrent, responsivity ($R$), quantum efficiency ($\eta$), and avalanche gain ($M$) of PIN and APD photodetectors under variable incident optical power.

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
The primary photocurrent generated in a photodetector is:

$$I_p = R \cdot P_{\text{opt}} = \left(\frac{\eta q}{h\nu}\right) P_{\text{opt}} = \left(\frac{\eta q \lambda}{h c}\right) P_{\text{opt}}$$

For an Avalanche Photodiode (APD), internal carrier multiplication provides gain $M$:

$$I_{\text{APD}} = M \cdot (I_p + I_{\text{dark}}) = M \cdot R \cdot P_{\text{opt}} + I_d$$

where $M = 1$ for PIN photodiodes and $M \ge 10$ for APDs.

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    Source["Optical Source (850 nm)"] --> VOA["Variable Optical Attenuator (0 - 80 µW)"]
    VOA --> Splitter["1x2 Optical Splitter (50:50)"]
    Splitter --> PIN["PIN Photodiode (M = 1)"]
    Splitter --> APD["APD Photodiode (M = 10, Bias = -30 V)"]
    PIN --> MeterPIN["Ammeter / Power Meter (IPIN)"]
    APD --> MeterAPD["Ammeter / Power Meter (IAPD)"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp08_PIN_APD_Photodetector_Characterization.osd`](./Exp08_PIN_APD_Photodetector_Characterization.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **CW Optical Source** | Transmitters Library | Wavelength 850 nm, Launch power 100 µW |
| **Variable Optical Attenuator** | Passives Library | Attenuates power from 0 to 80 µW |
| **PIN Photodetector** | Receivers Library | Responsivity 0.85 A/W, Dark current 1 nA, Gain M = 1 |
| **APD Photodetector** | Receivers Library | Responsivity 0.85 A/W, Avalanche gain M = 10, Dark current 5 nA |
| **Dual Electrical Meters** | Visualizers Library | Measures photocurrents simultaneously |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Optical Wavelength | **850** | nm |
| Incident Power Range | **0 to 80** | µW |
| PIN Responsivity (R) | **0.85** | A/W |
| APD Gain (M) | **10** | Dimensionless |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp08_PIN_APD_Photodetector_Characterization.osd`](./Exp08_PIN_APD_Photodetector_Characterization.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Incident Power | PIN Photocurrent | APD Photocurrent | Performance Observation |
| --- | --- | --- | --- |
| Pin = 0 µW (Dark) | 1.0 nA | 5.0 nA | Dark current leakage floor |
| Pin = 20 µW | 17.0 µA | 170.0 µA | Linear response, APD 10x higher |
| Pin = 40 µW | 34.0 µA | 340.1 µA | Linear responsivity confirmed |
| Pin = 60 µW | 51.0 µA | 510.1 µA | High linearity, no saturation |
| Pin = 80 µW | 68.0 µA | 680.1 µA | Full range measurement |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp08_PIN_APD_Comparison.png)

---

## 7. Engineering Analysis & Conclusion
The APD generates exactly 10-fold higher photocurrent than the PIN photodiode across the entire power range due to impact ionization avalanche gain ($M = 10$). This multiplication provides enhanced receiver sensitivity for detecting weak optical signals.

The simulation successfully validated the core physical principles of **Characterization of PIN and APD Photodetectors** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp08_PIN_APD_Comparison.png](./Exp08_PIN_APD_Comparison.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp08_Screenshot.png](./Exp08_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp08_PIN_APD_Photodetector_Characterization.osd`](./Exp08_PIN_APD_Photodetector_Characterization.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
