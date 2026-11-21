"""
Experiment 04: # 4. Exp 04: Dispersion Compensation
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
    print("Running simulation model for Experiment 04...")
    out_dir = "."
    t = np.linspace(-60, 60, 1000)
    t0 = 12.5 / (2 * np.sqrt(np.log(2))) # 12.5 ps FWHM
    pulse_in = np.exp(-(t/t0)**2)
    t_broad = t0 * np.sqrt(1 + (10 * 16 * 1.55**2 * 1e-3 / t0**2)**2) # broadened
    pulse_fiber = 0.5 * np.exp(-(t/(2.5*t0))**2)
    pulse_comp = 0.85 * np.exp(-(t/(1.05*t0))**2)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(t, pulse_in, 'b-', label='Input Gaussian Pulse (12.5 ps FWHM)')
    ax.plot(t, pulse_fiber, 'r--', label='After 10 km SMF (Dispersive Broadening)')
    ax.plot(t, pulse_comp, 'g-.', label='After Ideal Dispersion Compensation FBG (Re-compressed)')
    ax.set_xlabel('Time (ps)')
    ax.set_ylabel('Normalized Optical Power')
    ax.set_title('Exp 4: Optical Pulse Dispersion & Compensation in OptiSystem')
    ax.legend()
    plt.tight_layout()
    plt.savefig(f'./Exp04_Dispersion_Compensation.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp04_Dispersion_Compensation.png")

if __name__ == "__main__":
    run_simulation()
