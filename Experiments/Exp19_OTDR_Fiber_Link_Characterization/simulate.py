"""
Experiment 19: # 19. Exp 19: OTDR Trace
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
    print("Running simulation model for Experiment 19...")
    out_dir = "."
    z = np.linspace(0, 6, 1000) # km
    alpha = 0.20 # dB/km
    trace = -alpha * z
    # add connector reflection at z=0
    trace[0:15] += np.linspace(0, 12, 15)
    # add splice at z=2.5 km (loss step 0.3 dB)
    trace[z >= 2.5] -= 0.30
    # add end of fiber reflection at z=5.11 km
    end_idx = np.argmin(np.abs(z - 5.11))
    trace[end_idx-5:end_idx+5] += np.linspace(0, 15, 10)
    trace[z > 5.11] = -35.0 # noise floor
    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.plot(z, trace, 'b-', linewidth=1.5)
    ax.annotate('Near-end Connector\nReflection', xy=(0, 0), xytext=(0.3, 5), arrowprops=dict(facecolor='black', shrink=0.05, width=1))
    ax.annotate('Fusion Splice Event\n(Loss = 0.3 dB)', xy=(2.5, -0.8), xytext=(2.6, 3), arrowprops=dict(facecolor='blue', shrink=0.05, width=1))
    ax.annotate('Fiber End Reflection\n(L ≈ 5.11 km)', xy=(5.11, -1.0), xytext=(4.2, 7), arrowprops=dict(facecolor='red', shrink=0.05, width=1))
    ax.set_xlabel('Fiber Distance (km)')
    ax.set_ylabel('Backscatter Optical Power (dB)')
    ax.set_title('Exp 19: Simulated OTDR Trace for Optical Fiber Link Diagnostics')
    ax.set_ylim(-40, 15)
    plt.tight_layout()
    plt.savefig(f'./Exp19_OTDR_Trace.png', dpi=150)
    plt.close()
    print("Generated output graph: Exp19_OTDR_Trace.png")

if __name__ == "__main__":
    run_simulation()
