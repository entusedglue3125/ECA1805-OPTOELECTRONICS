# Experiment 11: Analysis of Optical Analog and Digital Modulation using Fiber Optic Trainer Kit & OptiSystem

## 1. Objective & Syllabus Linkage
**Objective**: To design and analyze optical analog sine-wave intensity modulation and optical digital NRZ modulation over an optical fiber link in OptiSystem.

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
1. Optical Analog Modulation:
Intensity of the optical carrier is modulated proportionally to an analog message $m(t) = V_m \sin(2\pi f_m t)$:

$$P(t) = P_0 [1 + m \cdot \sin(2\pi f_m t)]$$

where $m = V_m / V_\pi$ is the modulation depth.

2. Optical Digital Modulation:
A binary sequence $b_k \in \{0, 1\}$ is mapped to NRZ rectangular pulses and applied to a Mach-Zehnder electro-optic modulator, producing on-off keyed optical bits with high extinction ratio.

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph TD
    subgraph Analog Branch
        SineGen["1 kHz / 5 kHz Sine Generator"] --> AMZM["Mach-Zehnder Intensity Modulator"]
        CW1["CW Laser 1550 nm"] --> AMZM
        AMZM --> Fiber1["Optical Fiber (10 km)"]
        Fiber1 --> PIN1["PIN Detector"] --> Scope["Oscilloscope Visualizer"]
    end
    subgraph Digital Branch
        PRBS["PRBS Generator"] --> NRZ["NRZ Pulse Generator"]
        NRZ --> DMZM["Mach-Zehnder Modulator"]
        CW2["CW Laser 1550 nm"] --> DMZM
        DMZM --> Fiber2["Optical Fiber (10 km)"]
        Fiber2 --> PIN2["PIN Detector"] --> Eye["Eye Diagram Analyzer"]
    end
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp11_Analog_and_Digital_Modulation.osd`](./Exp11_Analog_and_Digital_Modulation.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **Analog Sine Generator** | Electrical Sources | Frequency 1 kHz & 5 kHz, Amplitude 1.0 V p-p |
| **PRBS + NRZ Generator** | Transmitters Library | Data rate 2.5 Gbps, Bit pattern 10101010 / PRBS7 |
| **CW Lasers (x2)** | Transmitters Library | Wavelength 1550 nm, Power 0 dBm |
| **Mach-Zehnder Modulators** | Modulators Library | Extinction ratio 30 dB |
| **Optical Fiber (10 km)** | Optical Fibers Library | SMF, α = 0.2 dB/km, D = 16 ps/nm/km |
| **PIN Receivers + Visualizers** | Visualizers Library | Electrical Oscilloscope and Eye Diagram Analyzer |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Analog Frequency | **1.0 and 5.0** | kHz |
| Analog Amplitude | **1.0** | V p-p |
| Digital Bit Rate | **2.5** | Gbps |
| Fiber Length | **10** | km |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp11_Analog_and_Digital_Modulation.osd`](./Exp11_Analog_and_Digital_Modulation.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Modulation Format | Received Output | Signal Quality | Observation |
| --- | --- | --- | --- |
| Analog 1 kHz Modulation | 0.95 V p-p | THD < 1.2% | Distortion-free recovered sine wave |
| Analog 5 kHz Modulation | 0.92 V p-p | THD < 1.5% | High linearity sinusoidal transmission |
| Digital Pattern 10101010 | Square clock waveform | Sharp edges | Clean bit transitions |
| Digital PRBS NRZ | Wide open eye diagram | Q = 9.4, BER < 10^-20 | Negligible dispersion degradation at 10 km |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp11_Analog_Digital_Modulation.png)

---

## 7. Engineering Analysis & Conclusion
Analog transmission requires strict Mach-Zehnder linearity in the quadrature bias region to prevent harmonic distortion. Digital transmission offers robust noise immunity with high noise margin, readily quantified by eye height and Q-factor.

The simulation successfully validated the core physical principles of **Analysis of Optical Analog and Digital Modulation using Fiber Optic Trainer Kit & OptiSystem** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp11_Analog_Digital_Modulation.png](./Exp11_Analog_Digital_Modulation.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp11_Screenshot.png](./Exp11_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp11_Analog_and_Digital_Modulation.osd`](./Exp11_Analog_and_Digital_Modulation.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
