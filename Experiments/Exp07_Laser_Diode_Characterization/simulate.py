"""
Experiment 07: # 7. Exp 07: Laser Diode V-I and L-I
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
    print("Running simulation model for Experiment 07...")
    out_dir = "."
    vf = np.linspace(0, 2.5, 100)
    vth = 1.5
    i_ld = np.where(vf > vth, 50 * (vf - vth)**1.5, 0.1 * vf)
    ith = 25.0 # mA threshold
    p_ld = np.where(i_ld > ith, 0.25 * (i_ld - ith), 0.01 * (i_ld / ith))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    ax1.plot(vf, i_ld, 'm-', linewidth=2)
    ax1.axvline(vth, color='r', linestyle='--', label=f'Vth ≈ {vth} V')
    ax1.set_xlabel('Forward Voltage VF (V)')
    ax1.set_ylabel('Injection Current I (mA)')
    ax1.set_title('Laser Diode V-I Curve')
    ax1.legend()
    ax2.plot(i_ld, p_ld, 'r-', linewidth=2)
    ax2.axvline(ith, color='k', linestyle='--', label=f'Ith ≈ {ith} mA')
    ax2.set_xlabel('Injection Current I (mA)')
    ax2.set_ylabel('Optical Power Output (mW)')
    ax2.set_title('Laser Diode L-I (P-I) Curve')
    ax2.legend()
    plt.suptitle('Exp 7: Semiconductor Laser Diode Characterization')
    plt.tight_layout()
    plt.savefig(f'./Exp07_Laser_Diode_Characterization.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp07_Laser_Diode_Characterization.png")

if __name__ == "__main__":
    run_simulation()
