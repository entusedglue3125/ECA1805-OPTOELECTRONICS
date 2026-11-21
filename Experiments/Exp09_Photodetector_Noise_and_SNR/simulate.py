"""
Experiment 09: # 9. Exp 09: Photodetector Noise & SNR
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
    print("Running simulation model for Experiment 09...")
    out_dir = "."
    pdbm = np.linspace(-60, 0, 100)
    p_watts = 10**((pdbm - 30)/10)
    q = 1.602e-19; b = 1e9; r = 1.0625; id_curr = 5e-9; kb = 1.381e-23; t = 300; rl = 50; fn = 2
    ip = r * p_watts
    var_shot = 2 * q * ip * b
    var_dark = 2 * q * id_curr * b * np.ones_like(p_watts)
    var_th = (4 * kb * t * b * fn / rl) * np.ones_like(p_watts)
    var_tot = var_shot + var_dark + var_th
    snr = (ip**2) / var_tot
    snr_db = 10 * np.log10(snr)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
    ax1.plot(pdbm, np.log10(var_th), 'r--', label='Thermal Noise σ²th')
    ax1.plot(pdbm, np.log10(var_shot), 'g-', label='Shot Noise σ²shot')
    ax1.plot(pdbm, np.log10(var_dark), 'k:', label='Dark Current Noise σ²dark')
    ax1.plot(pdbm, np.log10(var_tot), 'b-', label='Total Noise σ²total')
    ax1.set_xlabel('Input Power Pin (dBm)')
    ax1.set_ylabel('log10(Noise Variance / A²)')
    ax1.set_title('Photodetector Noise Variances')
    ax1.legend()
    ax2.plot(pdbm, snr_db, 'b-', linewidth=2)
    ax2.axhline(0, color='r', linestyle='--', label='SNR = 0 dB (Pmin ≈ -31.16 dBm)')
    ax2.set_xlabel('Input Power Pin (dBm)')
    ax2.set_ylabel('SNR (dB)')
    ax2.set_title('Signal-to-Noise Ratio vs Input Power')
    ax2.legend()
    plt.suptitle('Exp 9: Photodetector Noise and SNR Analysis')
    plt.tight_layout()
    plt.savefig(f'./Exp09_Photodetector_Noise_SNR.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp09_Photodetector_Noise_SNR.png")

if __name__ == "__main__":
    run_simulation()
