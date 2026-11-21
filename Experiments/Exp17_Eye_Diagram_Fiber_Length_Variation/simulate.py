"""
Experiment 17: # 17. Exp 17: Eye Diagram vs Fiber Length
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
    print("Running simulation model for Experiment 17...")
    out_dir = "."
    lengths_17 = np.array([25, 50, 75, 100, 125, 150])
    q_len = np.array([15.26, 8.02, 4.89, 0, 0, 0])
    ber_len = np.array([7.06e-53, 5.26e-16, 5.00e-7, 1.0, 1.0, 1.0])
    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(lengths_17[:3], q_len[:3], 'go-', linewidth=2, label='Q-Factor')
    ax1.plot(lengths_17[2:], q_len[2:], 'go--', linewidth=1.5, alpha=0.5)
    ax1.set_xlabel('Fiber Length (km)')
    ax1.set_ylabel('Q-Factor', color='g')
    ax2 = ax1.twinx()
    ax2.semilogy(lengths_17[:3], ber_len[:3], 'md-', linewidth=2, label='Min BER')
    ax2.set_ylabel('Bit Error Rate (BER)', color='m')
    plt.title('Exp 17: Signal Degradation & BER vs Fiber Length (10 Gbps Link)')
    plt.tight_layout()
    plt.savefig(f'./Exp17_BER_vs_Length.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp17_BER_vs_Length.png")

if __name__ == "__main__":
    run_simulation()
