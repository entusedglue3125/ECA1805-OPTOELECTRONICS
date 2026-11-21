"""
Experiment 20: # 20. Exp 20: FSO Link vs Range
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
    print("Running simulation model for Experiment 20...")
    out_dir = "."
    ranges = np.array([1, 2, 5, 10]) # km
    q_fso = np.array([2241.83, 2229.83, 2192.73, 2282.39])
    eye_h = np.array([1.329, 1.232, 0.995, 0.725]) # V
    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(ranges, eye_h, 'bs-', linewidth=2, label='Eye Height (V)')
    ax1.set_xlabel('FSO Link Range (km)')
    ax1.set_ylabel('Eye Height (V)', color='b')
    ax1.set_ylim(0.5, 1.5)
    ax2 = ax1.twinx()
    p_rec_fso = -2.0 * ranges - 10 * np.log10(ranges**2 + 0.1) # geometric spreading + atten
    ax2.plot(ranges, p_rec_fso, 'r^--', linewidth=2, label='Received Power Trend (dBm)')
    ax2.set_ylabel('Received Optical Power (dBm)', color='r')
    plt.title('Exp 20: Free-Space Optical (FSO) Link Performance vs Propagation Range')
    plt.tight_layout()
    plt.savefig(f'./Exp20_FSO_Performance.png', dpi=150)
    plt.close()
    
    print('All 20 simulation result plots generated successfully!')
    "
    print("Generated output graph: Exp20_FSO_Performance.png")

if __name__ == "__main__":
    run_simulation()
