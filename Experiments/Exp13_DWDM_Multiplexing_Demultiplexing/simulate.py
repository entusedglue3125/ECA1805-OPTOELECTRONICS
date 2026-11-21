"""
Experiment 13: # 13. Exp 13: DWDM Multiplexing & Demultiplexing
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
    print("Running simulation model for Experiment 13...")
    out_dir = "."
    freqs = np.linspace(193.0, 193.5, 500) # THz
    ch_freqs = [193.1, 193.2, 193.3, 193.4] # 100 GHz spacing
    spectrum = np.zeros_like(freqs)
    for cf in ch_freqs:
        spectrum += 10 * np.exp(-((freqs - cf)/0.015)**2)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(freqs, 10 * np.log10(spectrum + 1e-4), 'b-', linewidth=1.5)
    for cf in ch_freqs:
        ax.axvline(cf, color='r', linestyle=':', alpha=0.6)
    ax.set_xlabel('Optical Frequency (THz)')
    ax.set_ylabel('Power Spectrum (dBm)')
    ax.set_title('Exp 13: 4-Channel DWDM Multiplexed Spectrum (100 GHz Channel Grid)')
    plt.tight_layout()
    plt.savefig(f'./Exp13_DWDM_Spectrum.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp13_DWDM_Spectrum.png")

if __name__ == "__main__":
    run_simulation()
