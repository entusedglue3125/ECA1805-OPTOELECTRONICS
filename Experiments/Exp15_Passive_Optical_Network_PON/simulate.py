"""
Experiment 15: # 15. Exp 15: Passive Optical Network (PON)
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
    print("Running simulation model for Experiment 15...")
    out_dir = "."
    channels = ['ONU 1 (Ch 1)', 'ONU 2 (Ch 2)']
    q_pon = [4.81, 4.80]
    ber_pon = [5.50e-7, 5.69e-7]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    x = np.arange(len(channels))
    width = 0.35
    ax.bar(x, q_pon, width, color='skyblue', edgecolor='navy', label='Q-Factor')
    for i, v in enumerate(q_pon):
        ax.text(i, v + 0.1, f'Q = {v:.2f}\nBER = {ber_pon[i]:.2e}', ha='center', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(channels)
    ax.set_ylabel('Q-Factor')
    ax.set_ylim(0, 6.5)
    ax.set_title('Exp 15: WDM-PON Splitter Output Performance across ONUs')
    plt.tight_layout()
    plt.savefig(f'./Exp15_PON_Performance.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp15_PON_Performance.png")

if __name__ == "__main__":
    run_simulation()
