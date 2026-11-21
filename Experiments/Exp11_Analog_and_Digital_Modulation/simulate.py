"""
Experiment 11: # 11. Exp 11: Analog & Digital Modulation
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
    print("Running simulation model for Experiment 11...")
    out_dir = "."
    t_mod = np.linspace(0, 4, 1000) # ms
    sine_in = np.sin(2 * np.pi * 1 * t_mod) # 1 kHz
    bits = np.array([1, 0, 1, 0, 1, 1, 0, 0])
    nrz_sig = np.repeat(bits, 125)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    ax1.plot(t_mod, sine_in, 'b-')
    ax1.set_xlabel('Time (ms)')
    ax1.set_ylabel('Signal Amplitude (V)')
    ax1.set_title('Analog Sine Modulation (1 kHz)')
    ax2.plot(t_mod, nrz_sig, 'r-', linewidth=2)
    ax2.set_xlabel('Time (ms)')
    ax2.set_ylabel('Binary Bit Level')
    ax2.set_title('Digital NRZ Pattern Transmission')
    plt.suptitle('Exp 11: Optical Analog & Digital Modulation Waveforms')
    plt.tight_layout()
    plt.savefig(f'./Exp11_Analog_Digital_Modulation.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp11_Analog_Digital_Modulation.png")

if __name__ == "__main__":
    run_simulation()
