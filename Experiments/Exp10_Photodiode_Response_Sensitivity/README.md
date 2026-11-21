# Experiment 10: Photodiode Response and Sensitivity Analysis using OptiSystem

## 1. Objective & Syllabus Linkage
**Objective**: To design and simulate an optical receiver in OptiSystem comparing PIN and APD photodetectors, and determine their receiver sensitivity for a target Bit Error Rate (BER) of 10^-9.

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
Receiver sensitivity is defined as the minimum received optical power $P_{\text{sens}}$ required to achieve a specified Bit Error Rate (typically $\text{BER} \le 10^{-9}$, corresponding to $Q \ge 6.0$):

$$\text{BER} = \frac{1}{2} \text{erfc}\left(\frac{Q}{\sqrt{2}}\right) \approx \frac{1}{\sqrt{2\pi} Q} \exp\left(-\frac{Q^2}{2}\right)$$

Because APDs provide internal avalanche gain $M$, they require fewer incident photons to overcome thermal noise, providing higher sensitivity ($3-6\text{ dB}$ improvement over PIN receivers).

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    Laser["CW Laser (193.1 THz, 0 dBm)"] --> MZM["Mach-Zehnder Modulator (PRBS 10 Gbps)"]
    MZM --> VOA["Optical Attenuator (Sweep 25 - 45 dB)"]
    VOA --> Split["50:50 Optical Splitter"]
    Split --> PINBranch["PIN Receiver + Bessel Filter"]
    Split --> APDBranch["APD Receiver + Bessel Filter"]
    PINBranch --> BER1["BER Analyzer 1 (PIN Sensitivity)"]
    APDBranch --> BER2["BER Analyzer 2 (APD Sensitivity)"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp10_Photodiode_Response_Sensitivity.osd`](./Exp10_Photodiode_Response_Sensitivity.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **CW Laser Source** | Transmitters Library | Frequency 193.1 THz (1552.5 nm), Power 0 dBm |
| **PRBS + NRZ + MZM** | Transmitters Library | Bit rate 10 Gbps, Extinction ratio 30 dB |
| **Optical Attenuator** | Passives Library | Swept from 25 dB to 45 dB |
| **PIN Receiver** | Receivers Library | Responsivity 1.0 A/W, Thermal noise 10^-22 W/Hz |
| **APD Receiver** | Receivers Library | Responsivity 1.0 A/W, Gain M = 10, Ionization ratio 0.45 |
| **Low Pass Bessel Filters & BER Analyzers** | Visualizers Library | Cutoff 7.5 GHz, Eye diagram and BER measurement |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Bit Rate | **10.0** | Gbps |
| Target BER | **1.0 × 10^-9** | Q-factor ≥ 6.0 |
| Attenuator PIN Branch | **35.0** | dB |
| Attenuator APD Branch | **38.2** | dB |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp10_Photodiode_Response_Sensitivity.osd`](./Exp10_Photodiode_Response_Sensitivity.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Receiver Architecture | Sensitivity (dBm) | Sensitivity (W) | Performance Analysis |
| --- | --- | --- | --- |
| PIN Receiver Sensitivity | -38.22 dBm | 1.507 × 10^-7 W | Achieves BER = 10^-9 at atten = 35 dB |
| APD Receiver Sensitivity | -41.42 dBm | 7.214 × 10^-8 W | Achieves BER = 10^-9 at atten = 38.2 dB |
| Sensitivity Advantage | 3.20 dB | More than 2x sensitivity gain | APD detects signals half as strong |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp10_Receiver_Sensitivity.png)

---

## 7. Engineering Analysis & Conclusion
The APD receiver achieves $3.2\text{ dB}$ higher sensitivity than the PIN receiver, operating successfully down to $-41.42\text{ dBm}$ received power. This sensitivity margin allows links to span an additional $16\text{ km}$ of standard single-mode fiber ($0.2\text{ dB/km}$) without optical repeaters.

The simulation successfully validated the core physical principles of **Photodiode Response and Sensitivity Analysis using OptiSystem** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp10_Receiver_Sensitivity.png](./Exp10_Receiver_Sensitivity.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp10_Screenshot.png](./Exp10_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp10_Photodiode_Response_Sensitivity.osd`](./Exp10_Photodiode_Response_Sensitivity.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
