# Experiment 16: Eye Diagram Analysis of Optical Communication Link using OptiSystem (Power Variation)

## 1. Objective & Syllabus Linkage
**Objective**: To design an optical fiber link in OptiSystem and analyze the effect of optical source power variation (-10 dBm, 0 dBm, +10 dBm) on Eye Height, Q-factor, and Bit Error Rate (BER).

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
The eye diagram provides a comprehensive visual metric of link quality:
- Eye Height: Measure of signal amplitude margin against additive noise.
- Eye Width: Measure of timing jitter tolerance.

As laser launch power increases, photocurrent $I_p = R P_{\text{rec}}$ grows linearly, improving the signal-to-noise ratio. However, excessive launch power ($> +10\text{ dBm}$) triggers fiber nonlinearities (Self-Phase Modulation - SPM):

$$Q = \frac{I_1 - I_0}{\sigma_1 + \sigma_0}$$

$$\text{BER} \approx \frac{1}{2} \text{erfc}\left(\frac{Q}{\sqrt{2}}\right)$$

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    Laser["CW Laser (193.1 THz, Power: -10 / 0 / +10 dBm)"] --> MZM["Mach-Zehnder Modulator (PRBS 10 Gbps)"]
    MZM --> SMF["Optical Fiber (50 km, α = 0.2 dB/km)"]
    SMF --> PIN["PIN Photodetector"]
    PIN --> Filter["Low Pass RC / Bessel Filter"]
    Filter --> EyeAnalyzer["BER & Eye Diagram Analyzer"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp16_Eye_Diagram_Power_Variation.osd`](./Exp16_Eye_Diagram_Power_Variation.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **CW Laser Source** | Transmitters Library | Frequency 193.1 THz (1552.5 nm), Power swept: -10, 0, +10 dBm |
| **PRBS + NRZ Generator** | Transmitters Library | Bit rate 10 Gbps |
| **Mach-Zehnder Modulator** | Modulators Library | Extinction ratio 30 dB |
| **Single Mode Fiber (SMF)** | Optical Fibers Library | Length 50 km, Attenuation 0.2 dB/km, D = 16 ps/nm/km |
| **PIN Photodiode** | Receivers Library | Responsivity 1.0 A/W, Dark current 1 nA |
| **Low Pass Filter & BER Analyzer** | Visualizers Library | Eye height, Q-factor, and BER analyzer |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Laser Frequency | **193.1** | THz |
| Fiber Length | **50** | km |
| Bit Rate | **10.0** | Gbps |
| Power Test Levels | **-10, 0, +10** | dBm |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp16_Eye_Diagram_Power_Variation.osd`](./Exp16_Eye_Diagram_Power_Variation.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Transmit Power | Max Q-Factor | Min BER | Eye Opening Height | Performance Assessment |
| --- | --- | --- | --- | --- |
| Power = -10 dBm | 3.0773 | 1.044 × 10^-3 | 2.392 × 10^-7 V | Noise-limited regime, partially closed eye |
| Power = 0 dBm | 7.7507 | 4.527 × 10^-15 | 5.942 × 10^-5 V | Optimal operating point, wide open eye, zero errors |
| Power = +10 dBm | 7.7172 | 5.935 × 10^-15 | 6.156 × 10^-4 V | High power regime, onset of self-phase modulation |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp16_BER_vs_Power.png)

---

## 7. Engineering Analysis & Conclusion
At $-10\text{ dBm}$, thermal noise degrades the eye opening ($Q = 3.08$, $\text{BER} = 10^{-3}$). Increasing power to $0\text{ dBm}$ dramatically widens the eye, boosting $Q$ to $7.75$ and achieving $\text{BER} < 10^{-14}$. Further increase to $+10\text{ dBm}$ yields no further BER gain due to self-phase modulation nonlinear broadening.

The simulation successfully validated the core physical principles of **Eye Diagram Analysis of Optical Communication Link using OptiSystem (Power Variation)** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp16_BER_vs_Power.png](./Exp16_BER_vs_Power.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp16_Screenshot.png](./Exp16_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp16_Eye_Diagram_Power_Variation.osd`](./Exp16_Eye_Diagram_Power_Variation.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
