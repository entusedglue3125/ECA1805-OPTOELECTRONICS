# Experiment 17: Eye Diagram Analysis of Optical Communication Link using OptiSystem (Fiber Length Variation)

## 1. Objective & Syllabus Linkage
**Objective**: To design an optical communication link in OptiSystem and analyze the degrading effects of fiber transmission distance (25 km to 150 km) on signal attenuation, chromatic dispersion, eye closure, and BER.

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
As fiber transmission length $L$ increases, signals suffer two primary degradation mechanisms:
1. Exponential power attenuation: $P(L) = P_0 10^{-\alpha L / 10}$
2. Chromatic dispersion broadening: $\Delta\tau = D \cdot L \cdot \Delta\lambda$

When temporal pulse broadening $\Delta\tau$ exceeds a significant fraction of the bit period $T_b = 1/R_b$, pulses overlap into adjacent time slots, causing severe Inter-Symbol Interference (ISI), closing the eye opening and causing $Q \rightarrow 0$.

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    Tx["10 Gbps Optical Transmitter (1550 nm, 5 dBm)"] --> Fiber["Optical Fiber (25, 50, 75, 100, 125, 150 km)"]
    Fiber --> Rx["PIN Photodetector + Low Pass Filter"]
    Rx --> Regen["3R Regenerator"]
    Regen --> BER["BER & Eye Diagram Analyzer"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp17_Eye_Diagram_Fiber_Length_Variation.osd`](./Exp17_Eye_Diagram_Fiber_Length_Variation.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **CW Laser Source** | Transmitters Library | Wavelength 1550 nm (193.1 THz), Power 5 dBm |
| **PRBS + NRZ Generator** | Transmitters Library | Bit rate 10 Gbps ($T_b = 100\text{ ps}$) |
| **Mach-Zehnder Modulator** | Modulators Library | Extinction ratio 30 dB |
| **Optical Fiber (Variable Length)** | Optical Fibers Library | Length swept: 25, 50, 75, 100, 125, 150 km, α = 0.2 dB/km, D = 16 ps/nm/km |
| **PIN Receiver + 3R Regenerator** | Receivers Library | Responsivity 1.0 A/W, Decision circuit |
| **BER Analyzer** | Visualizers Library | Eye diagram, Q-factor, and BER vs distance |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Bit Rate | **10.0** | Gbps |
| Laser Power | **+5.0** | dBm |
| Operating Wavelength | **1550** | nm |
| Fiber Lengths Tested | **25, 50, 75, 100, 125, 150** | km |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp17_Eye_Diagram_Fiber_Length_Variation.osd`](./Exp17_Eye_Diagram_Fiber_Length_Variation.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Fiber Length | Max Q-Factor | Min BER | Eye Opening Condition | System Performance |
| --- | --- | --- | --- | --- |
| 25 km | 15.260 | 7.065 × 10^-53 | Wide open, perfect eye | Virtually error-free transmission |
| 50 km | 8.018 | 5.263 × 10^-16 | Clean eye opening | Exceeds telecommunication standard (BER < 10^-9) |
| 75 km | 4.891 | 5.004 × 10^-7 | Partially closed eye | Approaching dispersion-limited boundary |
| 100 km | 0.000 | 1.000 (Failure) | Completely collapsed eye | Severe ISI closure, unrecoverable |
| 125 km | 0.000 | 1.000 (Failure) | Fully closed | Excessive dispersion & attenuation |
| 150 km | 0.000 | 1.000 (Failure) | Fully closed | Link failure without optical repeater/DCF |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp17_BER_vs_Length.png)

---

## 7. Engineering Analysis & Conclusion
At $10\text{ Gbps}$, chromatic dispersion ($16\text{ ps/nm/km}$) restricts uncompensated standard single-mode fiber links to approximately $75-80\text{ km}$. Beyond $100\text{ km}$, pulse broadening induces total eye closure, mandating dispersion compensation (FBG or DCF) and optical amplification.

The simulation successfully validated the core physical principles of **Eye Diagram Analysis of Optical Communication Link using OptiSystem (Fiber Length Variation)** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp17_BER_vs_Length.png](./Exp17_BER_vs_Length.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp17_Screenshot.png](./Exp17_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp17_Eye_Diagram_Fiber_Length_Variation.osd`](./Exp17_Eye_Diagram_Fiber_Length_Variation.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
