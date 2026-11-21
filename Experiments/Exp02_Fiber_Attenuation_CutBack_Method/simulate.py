"""
Experiment 02: # 2. Exp 02: Cut-back attenuation
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
    print("Running simulation model for Experiment 02...")
    out_dir = "."
    fig, ax = plt.subplots(figsize=(8, 5))
    lengths = np.array([1, 2, 3, 5, 10]) # meters
    p_out_dbm = -0.20 * lengths # 0.20 dB/m typical plastic / MM
    ax.plot(lengths, p_out_dbm, 'ro-', linewidth=2, label='Transmitted Power (dBm)')
    ax.set_xlabel('Fiber Length L (m)')
    ax.set_ylabel('Relative Output Power (dBm)')
    ax.set_title('Exp 2: Optical Fiber Attenuation via Cut-Back Method (Slope = α)')
    ax.legend()
    plt.tight_layout()
    plt.savefig(f'./Exp02_CutBack_Attenuation.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp02_CutBack_Attenuation.png")

if __name__ == "__main__":
    run_simulation()
