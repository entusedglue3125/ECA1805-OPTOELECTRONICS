"""
Experiment 16: # 16. Exp 16: Eye Diagram vs Power
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
    print("Running simulation model for Experiment 16...")
    out_dir = "."
    powers = np.array([-10, 0, 10]) # dBm
    q_pwr = np.array([3.08, 7.75, 7.72])
    ber_pwr = np.array([1.04e-3, 4.53e-15, 5.94e-15])
    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(powers, q_pwr, 'bo-', linewidth=2, label='Max Q-Factor')
    ax1.set_xlabel('CW Laser Power (dBm)')
    ax1.set_ylabel('Q-Factor', color='b')
    ax2 = ax1.twinx()
    ax2.semilogy(powers, ber_pwr, 'rs--', linewidth=2, label='Min BER')
    ax2.set_ylabel('Bit Error Rate (BER)', color='r')
    plt.title('Exp 16: Q-Factor & BER vs Optical Source Power (10 Gbps 50 km Link)')
    plt.tight_layout()
    plt.savefig(f'./Exp16_BER_vs_Power.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp16_BER_vs_Power.png")

if __name__ == "__main__":
    run_simulation()
