# Experiment 7: Characterization of Laser Diode

## 1. Objective & Syllabus Linkage
**Objective**: To study the Voltage-Current (V-I) and Light-Current (L-I) characteristics, threshold current ($I_{th}$), slope efficiency, and emission spectrum of a semiconductor laser diode.

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit I–IV. Focuses on experimental verification, performance characterization, and computer-aided photonic simulation.

---

## 2. Theoretical Principles & Formulations
A semiconductor laser diode exhibits two operating regimes:
1. Below threshold current $I_{th}$, spontaneous emission dominates (LED mode, low efficiency).
2. Above $I_{th}$, optical gain overcomes cavity losses, yielding stimulated emission with high slope efficiency:

$$P_{\text{opt}} = \eta_d \left(\frac{h\nu}{q}\right) (I - I_{\text{th}}) \quad (I > I_{\text{th}})$$

Differential quantum efficiency $\eta_d = \frac{q}{h\nu} \frac{dP}{dI}$. Lasing output features a narrow coherent spectrum ($< 0.1\text{ nm}$).

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    CurrentSweep["Variable Bias Current Source (0 - 60 mA)"] --> Laser["Semiconductor Laser / Rate Equations"]
    Laser --> Voltmeter["Voltmeter (VF)"]
    Laser --> PowerMeter["Optical Power Meter (Popt)"]
    Laser --> OSA["Optical Spectrum Analyzer (Linewidth)"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp07_Laser_Diode_Characterization.osd`](./Exp07_Laser_Diode_Characterization.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table
| Component Name | Component Library | Configured Properties |
|---|---|---|
| **Semiconductor Laser** | Transmitters Library | Wavelength 1550 nm, Ith = 25 mA, Slope efficiency 0.25 mW/mA |
| **Bias Current Source** | Electrical Sources | Sweep current from 0 to 60 mA |
| **Optical Power Meter** | Visualizers Library | Measures output optical power |
| **Optical Spectrum Analyzer** | Visualizers Library | Measures laser spectral peaks and side-mode suppression |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Operating Wavelength | **1550** | nm |
| Threshold Current (Ith) | **25.0** | mA |
| Forward Voltage (Vf) | **1.5 to 2.0** | V |
| Current Sweep Range | **0 to 60** | mA |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp07_Laser_Diode_Characterization.osd`](./Exp07_Laser_Diode_Characterization.osd).
3. Inspect component connections and confirm optical and electrical parameter settings in the layout canvas.
4. Press **F2** or click **Calculate** to execute the CIDF numerical simulation scheduler.
5. Open the connected visualizers (Optical Spectrum Analyzers, BER Analyzers, Optical Time Domain Visualizers, Power Meters).
6. Record output readings across the test cases and verify alignment with theoretical predictions.

---

## 6. Simulation Results & Observations
| Injection Current | Forward Voltage | Optical Power | Operating Regime |
| --- | --- | --- | --- |
| I = 10 mA (< Ith) | 1.25 V | 0.08 mW | Spontaneous emission regime (LED mode) |
| I = 25 mA (Ith) | 1.52 V | 0.22 mW | Lasing threshold point |
| I = 35 mA (> Ith) | 1.78 V | 2.65 mW | Stimulated emission, steep coherent slope |
| I = 50 mA (> Ith) | 1.98 V | 6.40 mW | High power linear lasing regime |
| Spectral Linewidth | < 0.05 nm | Single-mode DFB | High coherence, SMSR > 45 dB |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp07_Laser_Diode_Characterization.png)

---

## 7. Engineering Analysis & Conclusion
The laser diode shows a sharp transition at $I_{th} = 25\text{ mA}$. Beyond threshold, optical power increases steeply with differential efficiency $0.25\text{ mW/mA}$, accompanied by severe spectral narrowing to $< 0.05\text{ nm}$, ideal for high-speed long-haul single-mode transmission.

The simulation successfully validated the core physical principles of **Characterization of Laser Diode** in OptiSystem, reproducing the laboratory record specifications with high numerical accuracy.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp07_Laser_Diode_Characterization.png](./Exp07_Laser_Diode_Characterization.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp07_Screenshot.png](./Exp07_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp07_Laser_Diode_Characterization.osd`](./Exp07_Laser_Diode_Characterization.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
