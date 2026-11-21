"""
Experiment 01: # 1. Exp 01: NA & V-number
ECA1805 - OPTOELECTRONICS
Simulation Model and Output Verification Script
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

def run_simulation():
    print("Running simulation model for Experiment 01...")
    out_dir = "."
    fig, ax1 = plt.subplots(figsize=(8, 5))
    core_d = np.array([50, 62.5, 100]) # um
    na_vals = np.array([0.200, 0.275, 0.290])
    v_850 = (np.pi * core_d * na_vals) / 0.850
    v_1300 = (np.pi * core_d * na_vals) / 1.300
    modes_850 = (v_850**2) / 2
    ax1.plot(core_d, na_vals, 'bo-', linewidth=2, label='Numerical Aperture (NA)')
    ax1.set_xlabel('Core Diameter (µm)')
    ax1.set_ylabel('Numerical Aperture', color='b')
    ax1.set_ylim(0.15, 0.35)
    ax2 = ax1.twinx()
    ax2.plot(core_d, v_850, 'rs--', linewidth=2, label='V-Number @ 850 nm')
    ax2.plot(core_d, v_1300, 'g^--', linewidth=2, label='V-Number @ 1300 nm')
    ax2.set_ylabel('Normalized Frequency (V-Number)', color='r')
    plt.title('Exp 1: Numerical Aperture & V-Number Characterization')
    plt.tight_layout()
    plt.savefig(f'./Exp01_NA_and_V_Number.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp01_NA_and_V_Number.png")

if __name__ == "__main__":
    run_simulation()
