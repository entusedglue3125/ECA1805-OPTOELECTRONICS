# Experiment 9: Analysis of Photodetector Noise and SNR using MATLAB/SCILAB & OptiSystem

## 1. Objective & Syllabus Linkage
**Objective**: To analyze the fundamental noise mechanisms in optical photodetectors (shot noise, dark current noise, and thermal Johnson noise) and compute the Signal-to-Noise Ratio (SNR) and Minimum Detectable Power ($P_{min}$).

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
The total noise current variance in an optical receiver is the sum of independent noise sources:

$$\sigma_{\text{total}}^2 = \sigma_{\text{shot}}^2 + \sigma_{\text{dark}}^2 + \sigma_{\text{th}}^2$$

$$\sigma_{\text{shot}}^2 = 2 q I_p B = 2 q (R P_{\text{in}}) B$$

$$\sigma_{\text{dark}}^2 = 2 q I_d B$$

$$\sigma_{\text{th}}^2 = \frac{4 k_B T B F_n}{R_L}$$

The electrical Signal-to-Noise Ratio is:

$$\text{SNR} = \frac{I_p^2}{\sigma_{\text{total}}^2} = \frac{(R P_{\text{in}})^2}{2 q (R P_{\text{in}} + I_d) B + \frac{4 k_B T B F_n}{R_L}}$$

Solving for $\text{SNR} = 1$ ($0\text{ dB}$) yields the Minimum Detectable Power $P_{\text{min}}$.

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    InputSweep["Optical Power Sweep (-60 to 0 dBm)"] --> Detector["PIN Receiver with Noise Parameters"]
    Detector --> NoiseAnalyzer["Noise Spectrum Analyzer"]
    NoiseAnalyzer --> ShotNoise["Shot Noise Variance σ²shot"]
    NoiseAnalyzer --> ThNoise["Thermal Noise Variance σ²th"]
    NoiseAnalyzer --> SNRCalc["Electrical SNR Analyzer (dB)"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp09_Photodetector_Noise_and_SNR.osd`](./Exp09_Photodetector_Noise_and_SNR.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **Optical Source + Attenuator** | Transmitters Library | Wavelength 1550 nm, Power swept from -60 to 0 dBm |
| **PIN Photodetector (Noise Mode)** | Receivers Library | η = 0.85, Id = 5 nA, T = 300 K, RL = 50 Ω, Fn = 2, B = 1 GHz |
| **Electrical SNR Visualizer** | Visualizers Library | Plots SNR (dB) vs incident optical power |
| **RF Spectrum Analyzer** | Visualizers Library | Measures thermal, shot, and total noise floors |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Quantum Efficiency (η) | **0.85** | Dimensionless |
| Wavelength (λ) | **1550** | nm |
| Dark Current (Id) | **5.0** | nA |
| Load Resistance (RL) | **50** | Ω |
| Receiver Bandwidth (B) | **1.0** | GHz |
| Noise Figure (Fn) | **2.0 (3 dB)** | Dimensionless |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp09_Photodetector_Noise_and_SNR.osd`](./Exp09_Photodetector_Noise_and_SNR.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Parameter / Condition | Computed Value | Physical Significance |
| --- | --- | --- |
| Responsivity (R) | 1.0625 A/W | Theoretical R = ηqλ / hc |
| Thermal Noise (σ²th) | 6.629 × 10^-13 A² | Dominant noise at low optical powers |
| Dark Current Noise (σ²dark) | 1.602 × 10^-18 A² | Constant shot noise from dark leakage |
| Pin = -50 dBm | SNR = -37.69 dB | Noise-limited regime (thermal dominated) |
| Pin = -31.16 dBm | SNR = 0.00 dB | Minimum Detectable Power (Pmin ≈ 766 nW) |
| Pin = 0 dBm | SNR = +62.05 dB | Shot-noise-limited regime (high SNR) |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp09_Photodetector_Noise_SNR.png)

---

## 7. Engineering Analysis & Conclusion
Thermal noise sets the lower sensitivity limit of $-31.16\text{ dBm}$ ($766\text{ nW}$) at low power levels. As input optical power exceeds $-20\text{ dBm}$, signal-dependent shot noise becomes dominant, leading to a linear increase in SNR on the logarithmic scale.

The simulation successfully validated the core physical principles of **Analysis of Photodetector Noise and SNR using MATLAB/SCILAB & OptiSystem** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp09_Photodetector_Noise_SNR.png](./Exp09_Photodetector_Noise_SNR.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp09_Screenshot.png](./Exp09_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp09_Photodetector_Noise_and_SNR.osd`](./Exp09_Photodetector_Noise_and_SNR.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
