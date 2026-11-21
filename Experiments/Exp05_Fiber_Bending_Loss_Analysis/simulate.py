"""
Experiment 05: # 5. Exp 05: Bending Loss
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
    print("Running simulation model for Experiment 05...")
    out_dir = "."
    fig, ax = plt.subplots(figsize=(8, 5))
    radius = np.array([1, 2, 3, 4, 5, 6, 8, 10]) # cm
    loss_1turn = 3.5 * np.exp(-0.4 * radius)
    loss_3turn = 3 * loss_1turn
    ax.plot(radius, loss_1turn, 'bo-', label='1 Turn Bend Loss (dB)')
    ax.plot(radius, loss_3turn, 'rs--', label='3 Turns Bend Loss (dB)')
    ax.set_xlabel('Bend Radius (cm)')
    ax.set_ylabel('Macro-bending Loss (dB)')
    ax.set_title('Exp 5: Optical Fiber Bending Loss vs Bend Radius & Turn Count')
    ax.legend()
    plt.tight_layout()
    plt.savefig(f'./Exp05_Bending_Loss.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp05_Bending_Loss.png")

if __name__ == "__main__":
    run_simulation()
