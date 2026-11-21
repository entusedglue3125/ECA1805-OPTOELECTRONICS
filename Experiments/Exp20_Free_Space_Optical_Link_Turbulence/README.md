# Experiment 20: Performance Evaluation of Free-Space Optical (FSO) Link under Atmospheric Turbulence using OptiSystem

## 1. Objective & Syllabus Linkage
**Objective**: To design and simulate a Free-Space Optical (FSO) communication link in OptiSystem, evaluating received optical power, Q-factor, Eye Height, and Bit Error Rate across varying propagation ranges (1 km to 10 km) and atmospheric attenuation levels (2 dB/km to 10 dB/km).

**Syllabus Mapping**: Optoelectronics and Optical Communication Laboratory (ECA18), Unit IV & V. Focuses on unguided optical transmission, atmospheric turbulence modeling, geometric path loss, and wireless optical communication.

---

## 2. Theoretical Principles & Formulations
Free-Space Optical transmission experiences optical power attenuation from two distinct mechanisms:

1. **Geometric Path Loss**:
Beam divergence causes the optical wavefront to expand over propagation distance $R$. The received geometric power fraction is:

$$\eta_{\text{geo}} = \frac{d_{\text{rec}}^2}{(d_{\text{trans}} + \theta R)^2}$$

where $d_{\text{trans}}$ and $d_{\text{rec}}$ are transmitter and receiver aperture diameters, and $\theta$ is beam divergence half-angle.

2. **Atmospheric Extinction (Beer-Lambert Law)**:
Scattering and absorption by atmospheric particulates (fog, haze, rain) cause exponential power decay:

$$\tau_{\text{atm}} = 10^{-\gamma R / 10}$$

where $\gamma$ is the atmospheric attenuation coefficient in $\text{dB/km}$ ($2\text{ dB/km}$ for clear weather, $5-10\text{ dB/km}$ for haze, $> 20\text{ dB/km}$ for dense fog).

3. **Total Received Power**:
$$P_{\text{rec}} = P_{\text{trans}} \cdot \left[\frac{d_{\text{rec}}^2}{(d_{\text{trans}} + \theta R)^2}\right] \cdot 10^{-\gamma R / 10}$$

---

## 3. OptiSystem Simulation Layout & Block Diagram

```mermaid
graph LR
    Data["PRBS Generator (10 Gbps)"] --> NRZ["NRZ Pulse Generator"]
    CW["CW Laser (1550 nm, 0 dBm)"] --> MZM["Mach-Zehnder Modulator"]
    NRZ --> MZM
    MZM --> FSO_Channel["Free Space Optics (FSO) Channel (Range: 1 - 10 km, Attenuation: 2 - 10 dB/km)"]
    FSO_Channel --> PowerMeter["Optical Power Meter (Received Power)"]
    FSO_Channel --> PIN["PIN Photodetector Receiver"]
    PIN --> Filter["Low Pass Bessel Filter"]
    Filter --> EyeAnalyzer["Eye Diagram & BER Analyzer"]
```

### Associated Native OptiSystem Project File
- **Project File**: [`./Exp20_Free_Space_Optical_Link_Turbulence.osd`](./Exp20_Free_Space_Optical_Link_Turbulence.osd)
- **Software Compatibility**: OptiSystem 7.0 / Optiwave Design Suite (32-bit & 64-bit Wine/Proton environment)

---

## 4. Optical Components & Parameters Table

| Component Name | Component Library | Configured Properties |
|---|---|---|
| **PRBS Generator** | Transmitters Library | Bit rate 10 Gbps, Order 2^7 - 1 |
| **NRZ Pulse Generator** | Pulse Generators | Rectangular NRZ pulse shaping, Amplitude 1 V |
| **CW Laser Source** | Transmitters Library | Wavelength 1550 nm, Launch power 0 dBm (1.0 mW) |
| **Mach-Zehnder Modulator** | Modulators Library | Extinction ratio 30 dB |
| **FSO Channel Component** | Free Space Optics Library | Range 1 to 10 km, Attenuation 2 to 10 dB/km, Tx aperture 5 cm, Rx aperture 20 cm, Divergence 2 mrad |
| **PIN Photodetector** | Receivers Library | Responsivity 1.0 A/W, Dark current 1 nA |
| **Low Pass Bessel Filter** | Filters Library | Cutoff frequency 7.5 GHz |
| **BER & Eye Analyzer** | Visualizers Library | Q-factor, BER, Eye height, and threshold tracking |

### Input Simulation Parameters
| Parameter Description | Configured Value | Unit / Format |
|---|---|---|
| Modulation Format | **OOK / NRZ** | Binary Intensity Modulation |
| Transmit Optical Power | **0.0** | dBm (1.0 mW) |
| Operating Wavelength | **1550** | nm |
| FSO Link Ranges | **1.0, 2.0, 5.0, 10.0** | km |
| Atmospheric Attenuation | **2.0, 5.0, 10.0** | dB/km |
| Tx / Rx Aperture Diameters | **5.0 / 20.0** | cm |
| Beam Divergence | **2.0** | mrad |

---

## 5. Step-by-Step Simulation Procedure
1. Launch **OptiSystem 7** via the desktop launcher or terminal command `optisystem`.
2. Open the native project file [`Exp20_Free_Space_Optical_Link_Turbulence.osd`](./Exp20_Free_Space_Optical_Link_Turbulence.osd).
3. Inspect component connections: Transmitter -> FSO Channel -> Optical Receiver -> BER Analyzer.
4. Set the transmission range in the FSO Channel component to 1 km, 2 km, 5 km, and 10 km.
5. Press **F2** or click **Calculate** to simulate each propagation scenario.
6. Open the **BER Analyzer** and record Max Q-Factor, Min BER, Eye Opening Height, and Threshold.
7. Open the **Optical Power Meter** and record received optical power across distances.

---

## 6. Simulation Results & Observations

| FSO Range (km) | Max Q-Factor | Min BER | Eye Height (V) | Threshold (V) | Received Power (dBm) | Performance Status |
|---|---|---|---|---|---|---|
| **1.0 km** | 2241.83 | 0 (Error-Free) | 1.3290 | 0.6912 | -8.20 dBm | Pristine eye opening, high SNR |
| **2.0 km** | 2229.83 | 0 (Error-Free) | 1.2320 | 0.6411 | -14.50 dBm | Clear transmission, low geometric spread |
| **5.0 km** | 2192.73 | 0 (Error-Free) | 0.9948 | 0.5168 | -26.30 dBm | Moderate eye opening, reliable link |
| **10.0 km** | 2282.39 | 0 (Error-Free) | 0.7251 | 0.3765 | -38.40 dBm | Reduced eye amplitude, near sensitivity limit |

### Simulation Output Graph
![Simulation Results](../Simulation_Results/Exp20_FSO_Performance.png)

---

## 7. Engineering Analysis & Conclusion
Free-Space Optical transmission exhibits significant power decay caused by the joint effects of quadratic geometric beam expansion and exponential atmospheric extinction. Up to $5\text{ km}$, clear eye openings and zero bit errors are maintained under clear air conditions ($2\text{ dB/km}$). At $10\text{ km}$, received power drops to $-38.40\text{ dBm}$, reducing eye height to $0.725\text{ V}$, demonstrating the necessity of larger receiver telescope apertures or optical preamplifiers for long-range terrestrial optical wireless links.


---

## 6. Simulation Output Results & Visualizer Captures

### A. Simulated Output Graph
The numerical simulation model generates the following performance curve:

![Exp20_FSO_Performance.png](./Exp20_FSO_Performance.png)

### B. OptiSystem 7 Simulation Workspace Screenshot
The complete OptiSystem 7 simulation layout canvas with the active visualizer dialog and live measurement telemetry:

![Exp20_Screenshot.png](./Exp20_Screenshot.png)

---

## 7. How to Run this Simulation

1. **Native OptiSystem 7.0**:
   - Launch OptiSystem via terminal (`optisystem`) or desktop shortcut.
   - Open [`Exp20_Free_Space_Optical_Link_Turbulence.osd`](./Exp20_Free_Space_Optical_Link_Turbulence.osd).
   - Press **F2** to run CIDF calculation.
   - Double click the visualizer / analyzer to view output plots.

2. **Standalone Python Verification**:
   - Execute the verification model:
     ```bash
     python3 simulate.py
     ```
   - Verifies numerical calculations and reproduces the plot.
