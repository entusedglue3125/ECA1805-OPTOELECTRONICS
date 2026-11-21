"""
Experiment 12: # 12. Exp 12: Advanced Modulation Formats
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
    print("Running simulation model for Experiment 12...")
    out_dir = "."
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 8))
    # OOK
    ax1.plot([0, 1], [0, 0], 'ro', markersize=10)
    ax1.set_xlim(-0.5, 1.5); ax1.set_ylim(-1, 1); ax1.set_title('OOK (1 bit/sym)')
    # PAM-4
    ax2.plot([-3, -1, 1, 3], [0, 0, 0, 0], 'bs', markersize=8)
    ax2.set_xlim(-4, 4); ax2.set_ylim(-1, 1); ax2.set_title('PAM-4 (2 bits/sym)')
    # DPSK
    ax3.plot([-1, 1], [0, 0], 'g^', markersize=10)
    ax3.set_xlim(-1.5, 1.5); ax3.set_ylim(-1, 1); ax3.set_title('DPSK (BPSK Phase)')
    # 4-QAM / QPSK
    qam_i = [-1, 1, -1, 1]; qam_q = [-1, -1, 1, 1]
    ax4.plot(qam_i, qam_q, 'md', markersize=10)
    ax4.set_xlim(-2, 2); ax4.set_ylim(-2, 2); ax4.set_title('QAM / QPSK (4 Constellation Points)')
    plt.suptitle('Exp 12: Advanced Optical Modulation Constellations')
    plt.tight_layout()
    plt.savefig(f'./Exp12_Modulation_Formats.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp12_Modulation_Formats.png")

if __name__ == "__main__":
    run_simulation()
