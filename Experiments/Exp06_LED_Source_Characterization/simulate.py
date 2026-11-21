"""
Experiment 06: # 6. Exp 06: LED Source V-I and L-I
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
    print("Running simulation model for Experiment 06...")
    out_dir = "."
    vf = np.linspace(0, 3.0, 100)
    vth = 1.8
    i_led = np.where(vf > vth, 35 * (vf - vth)**1.4, 0.05 * vf)
    p_led = np.where(i_led > 0.5, 0.04 * (i_led - 0.5), 0)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    ax1.plot(vf, i_led, 'b-', linewidth=2)
    ax1.axvline(vth, color='r', linestyle='--', label=f'Vth ≈ {vth} V')
    ax1.set_xlabel('Forward Voltage VF (V)')
    ax1.set_ylabel('Forward Current IF (mA)')
    ax1.set_title('LED V-I Characteristics')
    ax1.legend()
    ax2.plot(i_led, p_led, 'g-', linewidth=2)
    ax2.set_xlabel('Forward Current IF (mA)')
    ax2.set_ylabel('Optical Output Power (mW)')
    ax2.set_title('LED L-I (P-I) Characteristics')
    plt.suptitle('Exp 6: LED Optical Source Characterization')
    plt.tight_layout()
    plt.savefig(f'./Exp06_LED_Characterization.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp06_LED_Characterization.png")

if __name__ == "__main__":
    run_simulation()
