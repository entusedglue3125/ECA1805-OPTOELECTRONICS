# 🔬 ECA1805 - OPTOELECTRONICS
## Optoelectronics and Optical Communication Laboratory Simulation Suite

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CAD Engine](https://img.shields.io/badge/CAD-OptiSystem%207.0-brightgreen.svg)](https://optiwave.com/)
[![Course](https://img.shields.io/badge/Course-ECA1805%20Optoelectronics-orange.svg)](#)
[![Status](https://img.shields.io/badge/Status-Complete%20%26%20Verified-success.svg)](#)

This repository contains the complete collection of native, editable, and simulatable **OptiSystem 7.0** simulation projects, Python physical validation models, high-resolution simulation output graphs, and active workspace GUI screenshots covering all 20 experiments from the **ECA1805 - Optoelectronics and Optical Communication** curriculum (SIMATS School of Engineering).

---

## 📁 Repository Structure

Each experiment is cleanly categorized in its own self-contained folder under `Experiments/` with the native OptiSystem project file (`.osd`), Python numerical verification script (`simulate.py`), simulation plot (`.png`), GUI workspace screenshot (`.png`), and complete laboratory documentation (`README.md`):

```text
ECA1805-OPTOELECTRONICS/
├── Experiments/
│   ├── Exp01_Numerical_Aperture_and_V_Number/
│   │   ├── Exp01_Numerical_Aperture_and_V_Number.osd  # Native OptiSystem project file
│   │   ├── Exp01_NA_and_V_Number.png                  # Simulation plot
│   │   ├── Exp01_Screenshot.png                       # GUI workspace screenshot
│   │   ├── simulate.py                                # Python validation script
│   │   └── README.md                                  # Lab report & procedure
│   ├── Exp02_Fiber_Attenuation_CutBack_Method/
│   ├── ...
│   └── Exp20_Free_Space_Optical_Link_Turbulence/
├── Original_Record/
│   └── ECA18 OPTO LAB MANUAL.pdf                     # Preserved syllabus lab manual
├── Assignments/
│   ├── co1_answer.docx                               # Course Outcome 1 answers
│   ├── ECA18_CO1_Engineering_Design_Assignment.docx  # CO1 design assignment
│   └── ECA18_CO2_Assignment_Condensed.docx           # CO2 coursework assignment
├── README.md                                         # Master repository index
├── LICENSE                                           # MIT License
└── .gitignore                                        # Standard git ignore rules
```

---

## 📋 Complete Categorized Experiment Index

| Exp No | Experiment Title | Category | Experiment Folder & Report | Native OptiSystem Project | Python Script | Output Result Plot | GUI Workspace Screenshot | Key Simulated / Measured Output |
|:---:|---|:---:|---|---|---|---|---|---|
| **01** | Measurement of Numerical Aperture & V-Number of Optical Fiber | Fiber Characterization | [`Exp01_Numerical_Aperture_and_V_Number`](./Experiments/Exp01_Numerical_Aperture_and_V_Number/README.md) | [`Exp01_Numerical_Aperture_and_V_Number.osd`](./Experiments/Exp01_Numerical_Aperture_and_V_Number/Exp01_Numerical_Aperture_and_V_Number.osd) | [`simulate.py`](./Experiments/Exp01_Numerical_Aperture_and_V_Number/simulate.py) | [`Exp01_NA_and_V_Number.png`](./Experiments/Exp01_Numerical_Aperture_and_V_Number/Exp01_NA_and_V_Number.png) | [`Exp01_Screenshot.png`](./Experiments/Exp01_Numerical_Aperture_and_V_Number/Exp01_Screenshot.png) | NA ≈ 0.204, V = 37.71, M = 711 modes |
| **02** | Measurement of Fiber Attenuation using Cut-Back Method | Loss Characterization | [`Exp02_Fiber_Attenuation_CutBack_Method`](./Experiments/Exp02_Fiber_Attenuation_CutBack_Method/README.md) | [`Exp02_Fiber_Attenuation_CutBack_Method.osd`](./Experiments/Exp02_Fiber_Attenuation_CutBack_Method/Exp02_Fiber_Attenuation_CutBack_Method.osd) | [`simulate.py`](./Experiments/Exp02_Fiber_Attenuation_CutBack_Method/simulate.py) | [`Exp02_CutBack_Attenuation.png`](./Experiments/Exp02_Fiber_Attenuation_CutBack_Method/Exp02_CutBack_Attenuation.png) | [`Exp02_Screenshot.png`](./Experiments/Exp02_Fiber_Attenuation_CutBack_Method/Exp02_Screenshot.png) | ΔP = 0.41 dB, α = 205.0 dB/km (SMF: 0.205 dB/km) |
| **03** | Observation of Lower-Order LP Modes in Optical Fiber | Mode Theory | [`Exp03_Observation_Lower_Order_LP_Modes`](./Experiments/Exp03_Observation_Lower_Order_LP_Modes/README.md) | [`Exp03_Observation_Lower_Order_LP_Modes.osd`](./Experiments/Exp03_Observation_Lower_Order_LP_Modes/Exp03_Observation_Lower_Order_LP_Modes.osd) | [`simulate.py`](./Experiments/Exp03_Observation_Lower_Order_LP_Modes/simulate.py) | [`Exp03_LP_Modes.png`](./Experiments/Exp03_Observation_Lower_Order_LP_Modes/Exp03_LP_Modes.png) | [`Exp03_Screenshot.png`](./Experiments/Exp03_Observation_Lower_Order_LP_Modes/Exp03_Screenshot.png) | LP01, LP11, LP21, LP02 transverse spatial profiles, MFD = 10.42 µm |
| **04** | Measurement & Analysis of Dispersion Compensation | Dispersion Management | [`Exp04_Dispersion_Compensation`](./Experiments/Exp04_Dispersion_Compensation/README.md) | [`Exp04_Dispersion_Compensation.osd`](./Experiments/Exp04_Dispersion_Compensation/Exp04_Dispersion_Compensation.osd) | [`simulate.py`](./Experiments/Exp04_Dispersion_Compensation/simulate.py) | [`Exp04_Dispersion_Compensation.png`](./Experiments/Exp04_Dispersion_Compensation/Exp04_Dispersion_Compensation.png) | [`Exp04_Screenshot.png`](./Experiments/Exp04_Dispersion_Compensation/Exp04_Screenshot.png) | 12.50 ps → 52.40 ps (SMF) → 12.65 ps (DCF recompression, 99.7%) |
| **05** | Analysis of Bending Loss in Optical Fiber | Loss Characterization | [`Exp05_Fiber_Bending_Loss_Analysis`](./Experiments/Exp05_Fiber_Bending_Loss_Analysis/README.md) | [`Exp05_Fiber_Bending_Loss_Analysis.osd`](./Experiments/Exp05_Fiber_Bending_Loss_Analysis/Exp05_Fiber_Bending_Loss_Analysis.osd) | [`simulate.py`](./Experiments/Exp05_Fiber_Bending_Loss_Analysis/simulate.py) | [`Exp05_Bending_Loss.png`](./Experiments/Exp05_Fiber_Bending_Loss_Analysis/Exp05_Bending_Loss.png) | [`Exp05_Screenshot.png`](./Experiments/Exp05_Fiber_Bending_Loss_Analysis/Exp05_Screenshot.png) | R = 1–10 cm, turns 1–3, loss up to 7.05 dB, Rc = 2.80 cm |
| **06** | Characterization of LED as an Optical Source | Optical Sources | [`Exp06_LED_Source_Characterization`](./Experiments/Exp06_LED_Source_Characterization/README.md) | [`Exp06_LED_Source_Characterization.osd`](./Experiments/Exp06_LED_Source_Characterization/Exp06_LED_Source_Characterization.osd) | [`simulate.py`](./Experiments/Exp06_LED_Source_Characterization/simulate.py) | [`Exp06_LED_Characterization.png`](./Experiments/Exp06_LED_Source_Characterization/Exp06_LED_Characterization.png) | [`Exp06_Screenshot.png`](./Experiments/Exp06_LED_Source_Characterization/Exp06_Screenshot.png) | Vth = 1.80 V, P-I slope = 0.041 mW/mA, FWHM Δλ = 42.50 nm |
| **07** | Characterization of Semiconductor Laser Diode | Optical Sources | [`Exp07_Laser_Diode_Characterization`](./Experiments/Exp07_Laser_Diode_Characterization/README.md) | [`Exp07_Laser_Diode_Characterization.osd`](./Experiments/Exp07_Laser_Diode_Characterization/Exp07_Laser_Diode_Characterization.osd) | [`simulate.py`](./Experiments/Exp07_Laser_Diode_Characterization/simulate.py) | [`Exp07_Laser_Diode_Characterization.png`](./Experiments/Exp07_Laser_Diode_Characterization/Exp07_Laser_Diode_Characterization.png) | [`Exp07_Screenshot.png`](./Experiments/Exp07_Laser_Diode_Characterization/Exp07_Screenshot.png) | Vth = 1.52 V, Ith = 25.0 mA, η = 0.198 mW/mA, SMSR = 48.20 dB |
| **08** | Characterization of PIN and APD Photodetectors | Photodetectors | [`Exp08_PIN_APD_Photodetector_Characterization`](./Experiments/Exp08_PIN_APD_Photodetector_Characterization/README.md) | [`Exp08_PIN_APD_Photodetector_Characterization.osd`](./Experiments/Exp08_PIN_APD_Photodetector_Characterization/Exp08_PIN_APD_Photodetector_Characterization.osd) | [`simulate.py`](./Experiments/Exp08_PIN_APD_Photodetector_Characterization/simulate.py) | [`Exp08_PIN_APD_Comparison.png`](./Experiments/Exp08_PIN_APD_Photodetector_Characterization/Exp08_PIN_APD_Comparison.png) | [`Exp08_Screenshot.png`](./Experiments/Exp08_PIN_APD_Photodetector_Characterization/Exp08_Screenshot.png) | PIN R = 0.850 A/W, APD gain M = 10× (20.0 dB gain, 850 µA) |
| **09** | Analysis of Photodetector Noise & SNR | Noise & Detection | [`Exp09_Photodetector_Noise_and_SNR`](./Experiments/Exp09_Photodetector_Noise_and_SNR/README.md) | [`Exp09_Photodetector_Noise_and_SNR.osd`](./Experiments/Exp09_Photodetector_Noise_and_SNR/Exp09_Photodetector_Noise_and_SNR.osd) | [`simulate.py`](./Experiments/Exp09_Photodetector_Noise_and_SNR/simulate.py) | [`Exp09_Photodetector_Noise_SNR.png`](./Experiments/Exp09_Photodetector_Noise_and_SNR/Exp09_Photodetector_Noise_SNR.png) | [`Exp09_Screenshot.png`](./Experiments/Exp09_Photodetector_Noise_and_SNR/Exp09_Screenshot.png) | σth² = 6.63×10⁻¹³ A², Pmin = -31.16 dBm (SNR=10dB) |
| **10** | Photodiode Response & Receiver Sensitivity Analysis | Receiver Design | [`Exp10_Photodiode_Response_Sensitivity`](./Experiments/Exp10_Photodiode_Response_Sensitivity/README.md) | [`Exp10_Photodiode_Response_Sensitivity.osd`](./Experiments/Exp10_Photodiode_Response_Sensitivity/Exp10_Photodiode_Response_Sensitivity.osd) | [`simulate.py`](./Experiments/Exp10_Photodiode_Response_Sensitivity/simulate.py) | [`Exp10_Receiver_Sensitivity.png`](./Experiments/Exp10_Photodiode_Response_Sensitivity/Exp10_Receiver_Sensitivity.png) | [`Exp10_Screenshot.png`](./Experiments/Exp10_Photodiode_Response_Sensitivity/Exp10_Screenshot.png) | PIN Sens = -38.22 dBm, APD Sens = -41.42 dBm (+3.20 dB margin) |
| **11** | Analysis of Optical Analog & Digital Modulation | Modulation | [`Exp11_Analog_and_Digital_Modulation`](./Experiments/Exp11_Analog_and_Digital_Modulation/README.md) | [`Exp11_Analog_and_Digital_Modulation.osd`](./Experiments/Exp11_Analog_and_Digital_Modulation/Exp11_Analog_and_Digital_Modulation.osd) | [`simulate.py`](./Experiments/Exp11_Analog_and_Digital_Modulation/simulate.py) | [`Exp11_Analog_Digital_Modulation.png`](./Experiments/Exp11_Analog_and_Digital_Modulation/Exp11_Analog_Digital_Modulation.png) | [`Exp11_Screenshot.png`](./Experiments/Exp11_Analog_and_Digital_Modulation/Exp11_Screenshot.png) | Analog: 1/5 kHz (m=0.65, THD 1.2%), Digital: 2.5 Gbps NRZ (ER 11.2 dB) |
| **12** | Advanced Modulation Formats (OOK, PAM-4, DPSK, QAM) | Coherent Comm | [`Exp12_Advanced_Modulation_Formats_OOK_PAM4_DPSK_QAM`](./Experiments/Exp12_Advanced_Modulation_Formats_OOK_PAM4_DPSK_QAM/README.md) | [`Exp12_Advanced_Modulation_Formats_OOK_PAM4_DPSK_QAM.osd`](./Experiments/Exp12_Advanced_Modulation_Formats_OOK_PAM4_DPSK_QAM/Exp12_Advanced_Modulation_Formats_OOK_PAM4_DPSK_QAM.osd) | [`simulate.py`](./Experiments/Exp12_Advanced_Modulation_Formats_OOK_PAM4_DPSK_QAM/simulate.py) | [`Exp12_Modulation_Formats.png`](./Experiments/Exp12_Advanced_Modulation_Formats_OOK_PAM4_DPSK_QAM/Exp12_Modulation_Formats.png) | [`Exp12_Screenshot.png`](./Experiments/Exp12_Advanced_Modulation_Formats_OOK_PAM4_DPSK_QAM/Exp12_Screenshot.png) | OOK (10G), PAM-4 (20G), DPSK (10G), 16-QAM (40 Gbps, EVM 4.8%) |
| **13** | Dense WDM Multiplexing & Demultiplexing Performance | WDM Systems | [`Exp13_DWDM_Multiplexing_Demultiplexing`](./Experiments/Exp13_DWDM_Multiplexing_Demultiplexing/README.md) | [`Exp13_DWDM_Multiplexing_Demultiplexing.osd`](./Experiments/Exp13_DWDM_Multiplexing_Demultiplexing/Exp13_DWDM_Multiplexing_Demultiplexing.osd) | [`simulate.py`](./Experiments/Exp13_DWDM_Multiplexing_Demultiplexing/simulate.py) | [`Exp13_DWDM_Spectrum.png`](./Experiments/Exp13_DWDM_Multiplexing_Demultiplexing/Exp13_DWDM_Spectrum.png) | [`Exp13_Screenshot.png`](./Experiments/Exp13_DWDM_Multiplexing_Demultiplexing/Exp13_Screenshot.png) | 4-Ch 100 GHz grid (40 Gbps), crosstalk < -42.8 dB, BER < 10⁻²⁰ |
| **14** | EDFA-Based Dense WDM Link Performance Analysis | Optical Amplifiers | [`Exp14_EDFA_Dense_WDM_Link`](./Experiments/Exp14_EDFA_Dense_WDM_Link/README.md) | [`Exp14_EDFA_Dense_WDM_Link.osd`](./Experiments/Exp14_EDFA_Dense_WDM_Link/Exp14_EDFA_Dense_WDM_Link.osd) | [`simulate.py`](./Experiments/Exp14_EDFA_Dense_WDM_Link/simulate.py) | [`Exp14_EDFA_WDM_Performance.png`](./Experiments/Exp14_EDFA_Dense_WDM_Link/Exp14_EDFA_WDM_Performance.png) | [`Exp14_Screenshot.png`](./Experiments/Exp14_EDFA_Dense_WDM_Link/Exp14_Screenshot.png) | Gain = 20.0 dB, NF = 4.5 dB, 50km (Q=10.42), 100km (Q=4.84) |
| **15** | Design & Performance of Passive Optical Network (PON) | Access Networks | [`Exp15_Passive_Optical_Network_PON`](./Experiments/Exp15_Passive_Optical_Network_PON/README.md) | [`Exp15_Passive_Optical_Network_PON.osd`](./Experiments/Exp15_Passive_Optical_Network_PON/Exp15_Passive_Optical_Network_PON.osd) | [`simulate.py`](./Experiments/Exp15_Passive_Optical_Network_PON/simulate.py) | [`Exp15_PON_Performance.png`](./Experiments/Exp15_Passive_Optical_Network_PON/Exp15_PON_Performance.png) | [`Exp15_Screenshot.png`](./Experiments/Exp15_Passive_Optical_Network_PON/Exp15_Screenshot.png) | OLT 1490/1310 nm, 20 km feeder + 2 km drop, ONU Q = 4.81 |
| **16** | Eye Diagram Analysis (Launch Power Variation) | Signal Integrity | [`Exp16_Eye_Diagram_Power_Variation`](./Experiments/Exp16_Eye_Diagram_Power_Variation/README.md) | [`Exp16_Eye_Diagram_Power_Variation.osd`](./Experiments/Exp16_Eye_Diagram_Power_Variation/Exp16_Eye_Diagram_Power_Variation.osd) | [`simulate.py`](./Experiments/Exp16_Eye_Diagram_Power_Variation/simulate.py) | [`Exp16_BER_vs_Power.png`](./Experiments/Exp16_Eye_Diagram_Power_Variation/Exp16_BER_vs_Power.png) | [`Exp16_Screenshot.png`](./Experiments/Exp16_Eye_Diagram_Power_Variation/Exp16_Screenshot.png) | -10 dBm (Q=3.08), 0 dBm optimal (Q=7.75), +10 dBm SPM limited (Q=7.72) |
| **17** | Eye Diagram Analysis (Fiber Length Variation) | Signal Integrity | [`Exp17_Eye_Diagram_Fiber_Length_Variation`](./Experiments/Exp17_Eye_Diagram_Fiber_Length_Variation/README.md) | [`Exp17_Eye_Diagram_Fiber_Length_Variation.osd`](./Experiments/Exp17_Eye_Diagram_Fiber_Length_Variation/Exp17_Eye_Diagram_Fiber_Length_Variation.osd) | [`simulate.py`](./Experiments/Exp17_Eye_Diagram_Fiber_Length_Variation/simulate.py) | [`Exp17_BER_vs_Length.png`](./Experiments/Exp17_Eye_Diagram_Fiber_Length_Variation/Exp17_BER_vs_Length.png) | [`Exp17_Screenshot.png`](./Experiments/Exp17_Eye_Diagram_Fiber_Length_Variation/Exp17_Screenshot.png) | 25km (Q=15.26), 50km (Q=8.02), 75km (Q=4.89), Max reach = 78.0 km |
| **18** | Optical Spectrum & OSNR Evolution Analysis | Spectral Analysis | [`Exp18_Optical_Spectrum_and_OSNR_Analysis`](./Experiments/Exp18_Optical_Spectrum_and_OSNR_Analysis/README.md) | [`Exp18_Optical_Spectrum_and_OSNR_Analysis.osd`](./Experiments/Exp18_Optical_Spectrum_and_OSNR_Analysis/Exp18_Optical_Spectrum_and_OSNR_Analysis.osd) | [`simulate.py`](./Experiments/Exp18_Optical_Spectrum_and_OSNR_Analysis/simulate.py) | [`Exp18_OSNR_vs_Distance.png`](./Experiments/Exp18_Optical_Spectrum_and_OSNR_Analysis/Exp18_OSNR_vs_Distance.png) | [`Exp18_Screenshot.png`](./Experiments/Exp18_Optical_Spectrum_and_OSNR_Analysis/Exp18_Screenshot.png) | 50km (32.5 dB), 75km (28.1 dB), 100km (24.2 dB), rate = 0.166 dB/km |
| **19** | Optical Fiber Link Characterization using OTDR | Fiber Diagnostics | [`Exp19_OTDR_Fiber_Link_Characterization`](./Experiments/Exp19_OTDR_Fiber_Link_Characterization/README.md) | [`Exp19_OTDR_Fiber_Link_Characterization.osd`](./Experiments/Exp19_OTDR_Fiber_Link_Characterization/Exp19_OTDR_Fiber_Link_Characterization.osd) | [`simulate.py`](./Experiments/Exp19_OTDR_Fiber_Link_Characterization/simulate.py) | [`Exp19_OTDR_Trace.png`](./Experiments/Exp19_OTDR_Fiber_Link_Characterization/Exp19_OTDR_Trace.png) | [`Exp19_Screenshot.png`](./Experiments/Exp19_OTDR_Fiber_Link_Characterization/Exp19_Screenshot.png) | L = 5.11 km, α = 0.200 dB/km, Splice loss 0.30 dB @ 2.45 km, Fresnel spike |
| **20** | Free-Space Optical (FSO) Link under Turbulence | Wireless Optics | [`Exp20_Free_Space_Optical_Link_Turbulence`](./Experiments/Exp20_Free_Space_Optical_Link_Turbulence/README.md) | [`Exp20_Free_Space_Optical_Link_Turbulence.osd`](./Experiments/Exp20_Free_Space_Optical_Link_Turbulence/Exp20_Free_Space_Optical_Link_Turbulence.osd) | [`simulate.py`](./Experiments/Exp20_Free_Space_Optical_Link_Turbulence/simulate.py) | [`Exp20_FSO_Performance.png`](./Experiments/Exp20_Free_Space_Optical_Link_Turbulence/Exp20_FSO_Performance.png) | [`Exp20_Screenshot.png`](./Experiments/Exp20_Free_Space_Optical_Link_Turbulence/Exp20_Screenshot.png) | Clear air 1km (Q>2000, Eye 1.33V), Fog 3km (Q=5.20, Eye 0.73V) |

---

## 🚀 How to Open and Simulate the Projects

### Method 1: Using OptiSystem 7.0 (Recommended)
1. **Launch OptiSystem**:
   - On Linux (via Wine/Proton): Run `optisystem` in terminal or click the **OptiSystem 7** desktop shortcut.
   - On Windows: Launch **OptiSystem 7** from the Start Menu.
2. **Open Project**:
   - Press `Ctrl + O` and navigate to any experiment folder inside `Experiments/`.
   - Open the `.osd` project file (e.g., `Exp04_Dispersion_Compensation.osd`).
3. **Execute Simulation**:
   - Press **F2** (or click the play/Calculate icon on the toolbar).
   - OptiSystem's Component Iteration and Data Flow (CIDF) scheduler will execute the simulation.
4. **View Outputs**:
   - Double-click any visualizer/analyzer (e.g., **Optical Spectrum Analyzer**, **Eye Diagram Analyzer**, **OTDR Visualizer**) to inspect output curves, eye diagrams, and numerical measurements.

### Method 2: Python Numerical Physics Model
Each experiment folder contains an independent `simulate.py` script that models the physical equations and reproduces the publication-quality graphs:
```bash
cd Experiments/Exp01_Numerical_Aperture_and_V_Number
python3 simulate.py
```

---

## ⚙️ Technical Environment & Standards
- **Platform**: Linux x86_64 / Windows 10/11
- **CAD Simulation Suite**: Optiwave OptiSystem 7.0
- **Language & Libraries**: Python 3.10+, NumPy, Matplotlib, SciPy
- **Preserved Source**: `ECA18 OPTO LAB MANUAL.pdf` (SIMATS School of Engineering, 148 pages)

---

## 📄 License
This project is licensed under the [MIT License](LICENSE) - feel free to use and adapt for academic and research purposes.
