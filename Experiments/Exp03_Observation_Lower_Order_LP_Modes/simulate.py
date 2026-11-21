"""
Experiment 03: # 3. Exp 03: LP Modes
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
    print("Running simulation model for Experiment 03...")
    out_dir = "."
    r = np.linspace(-25, 25, 200)
    R, TH = np.meshgrid(r, r)
    RADIUS = np.sqrt(R**2 + TH**2)
    lp01 = np.exp(-2*(RADIUS/15)**2)
    lp11 = (R/15)**2 * np.exp(-2*(RADIUS/15)**2)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    im1 = ax1.imshow(lp01, extent=[-25, 25, -25, 25], cmap='inferno')
    ax1.set_title('LP01 Fundamental Mode')
    plt.colorbar(im1, ax=ax1, fraction=0.046)
    im2 = ax2.imshow(lp11, extent=[-25, 25, -25, 25], cmap='inferno')
    ax2.set_title('LP11 First Higher-Order Mode')
    plt.colorbar(im2, ax=ax2, fraction=0.046)
    plt.suptitle('Exp 3: Transverse LP Mode Intensity Profiles')
    plt.tight_layout()
    plt.savefig(f'./Exp03_LP_Modes.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp03_LP_Modes.png")

if __name__ == "__main__":
    run_simulation()
