"""
Experiment 08: # 8. Exp 08: PIN and APD Characterization
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
    print("Running simulation model for Experiment 08...")
    out_dir = "."
    pin_power = np.linspace(0, 80, 50) # uW
    r_pin = 0.85 # A/W
    i_pin = r_pin * (pin_power * 1e-6) * 1e6 # uA
    m_apd = 10.0 # avalanche gain
    i_apd = m_apd * i_pin
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(pin_power, i_pin, 'b-', label='PIN Photodiode (R = 0.85 A/W, M = 1)')
    ax.plot(pin_power, i_apd, 'r-', label='APD (R = 0.85 A/W, Gain M = 10)')
    ax.set_xlabel('Incident Optical Power (µW)')
    ax.set_ylabel('Photocurrent (µA)')
    ax.set_title('Exp 8: PIN vs APD Photocurrent & Avalanche Multiplication')
    ax.legend()
    plt.tight_layout()
    plt.savefig(f'./Exp08_PIN_APD_Comparison.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp08_PIN_APD_Comparison.png")

if __name__ == "__main__":
    run_simulation()
