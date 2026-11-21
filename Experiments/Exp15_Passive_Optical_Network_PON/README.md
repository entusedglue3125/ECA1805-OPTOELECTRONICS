# Experiment 15: Design and Performance Analysis of Passive Optical Network (PON) using OptiSystem

## 1. Objective & Syllabus Linkage
**Objective**: To design and simulate a Wavelength-Division Multiplexed Passive Optical Network (WDM-PON) in OptiSystem, distributing two independent optical channels through a shared feeder single-mode fiber and passive optical splitter to multiple Optical Network Units (ONUs).

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
Passive Optical Networks eliminate active electronic repeaters in the distribution path. An Optical Line Terminal (OLT) multiplexes downstream traffic into a common feeder fiber:

$$P_{\text{ONU}} = P_{\text{OLT}} - \alpha_{\text{fiber}} L - 10 \log_{10}(N) - L_{\text{excess}}$$

where $N$ is the splitter split ratio ($N = 2 \rightarrow 3\text{ dB}$ ideal split loss; $N = 4 \rightarrow 6\text{ dB}$; $N = 8 \rightarrow 9\text{ dB}$). Each ONU receives its assigned wavelength channel with sufficient power margin.

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph TD
    subgraph OLT Central Office
        Laser1["CW Laser 1 (1550 nm)"] --> MZM1["MZM 1 (PRBS 2.5 Gbps)"]
        Laser2["CW Laser 2 (1552 nm)"] --> MZM2["MZM 2 (PRBS 2.5 Gbps)"]
        MZM1 & MZM2 --> MUX["WDM Mux 2x1"]
    end
    MUX --> Feeder["Feeder SMF Fiber (20 km)"]
    Feeder --> Splitter["1x2 Passive Optical Splitter"]
    Splitter --> ONU1["ONU 1 Receiver (PIN + LPF + BER Analyzer 1)"]
    Splitter --> ONU2["ONU 2 Receiver (PIN + LPF + BER Analyzer 2)"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp15_Passive_Optical_Network_PON.osd`](./Exp15_Passive_Optical_Network_PON.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **CW Lasers (Ch 1 & Ch 2)** | Transmitters Library | Wavelengths 1550 nm & 1552 nm, Power 0 dBm |
| **PRBS + NRZ Generators** | Transmitters Library | Bit rate 2.5 Gbps per subscriber |
| **WDM Multiplexer 2x1** | WDM Multiplexers | 100 GHz channel spacing |
| **Feeder SMF Fiber** | Optical Fibers Library | Length 20 km, Attenuation 0.2 dB/km, D = 16 ps/nm/km |
| **Passive Optical Splitter 1x2** | Passives Library | Split ratio 50:50, Insertion loss 3.0 dB |
| **ONU Receivers (x2)** | Receivers Library | PIN photodiode, Low pass Bessel filter, BER Analyzer |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Bit Rate per Channel | **2.5** | Gbps |
| Feeder Fiber Length | **20** | km |
| Splitter Split Ratio | **1:2 (50:50)** | Dimensionless |
| Splitter Insertion Loss | **3.0** | dB |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp15_Passive_Optical_Network_PON.osd`](./Exp15_Passive_Optical_Network_PON.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Subscriber Unit | Max Q-Factor | Min BER | Eye Opening Height | Network Performance |
| --- | --- | --- | --- | --- |
| ONU 1 (Channel 1) | 4.8118 | 5.497 × 10^-7 | 0.924 mV | Clear eye opening, robust voice/data service |
| ONU 2 (Channel 2) | 4.8050 | 5.695 × 10^-7 | 0.918 mV | Uniform optical power distribution, compliant |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp15_PON_Performance.png)

---

## 7. Engineering Analysis & Conclusion
The 1x2 passive optical splitter introduces a $3.0\text{ dB}$ power division loss without introducing active noise or nonlinear distortion. Both ONUs achieve balanced $Q$-factors of $4.81$ and bit error rates of $5.5 \times 10^{-7}$, confirming successful shared PON infrastructure operation.

The simulation successfully validated the core physical principles of **Design and Performance Analysis of Passive Optical Network (PON) using OptiSystem** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp15_PON_Performance.png](./Exp15_PON_Performance.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp15_Screenshot.png](./Exp15_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp15_Passive_Optical_Network_PON.osd`](./Exp15_Passive_Optical_Network_PON.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
