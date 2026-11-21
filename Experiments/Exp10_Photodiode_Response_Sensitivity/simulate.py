"""
Experiment 10: # 10. Exp 10: Photodiode Response & Sensitivity
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
    print("Running simulation model for Experiment 10...")
    out_dir = "."
    atten = np.linspace(25, 45, 50)
    p_rec_pin = 0 - atten - 3.2 # dBm
    p_rec_apd = 0 - atten # dBm
    ber_pin = 0.5 * np.exp(-((10**((p_rec_pin + 38.2)/5))**2))
    ber_apd = 0.5 * np.exp(-((10**((p_rec_apd + 41.4)/5))**2))
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(atten, np.clip(ber_pin, 1e-15, 1), 'b-', label='PIN Receiver (Sensitivity ≈ -38.2 dBm)')
    ax.semilogy(atten, np.clip(ber_apd, 1e-15, 1), 'r--', label='APD Receiver (Sensitivity ≈ -41.4 dBm)')
    ax.axhline(1e-9, color='k', linestyle=':', label='Target BER = 10^-9')
    ax.set_xlabel('Channel Attenuation (dB)')
    ax.set_ylabel('Bit Error Rate (BER)')
    ax.set_title('Exp 10: Receiver Sensitivity & BER Analysis for PIN vs APD')
    ax.legend()
    plt.tight_layout()
    plt.savefig(f'./Exp10_Receiver_Sensitivity.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp10_Receiver_Sensitivity.png")

if __name__ == "__main__":
    run_simulation()
