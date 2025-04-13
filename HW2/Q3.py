import matplotlib.pyplot as plt
import numpy as np

def simulate_tcp_fairness(R, RTT_ratio, ssth_ratio=0.2, max_steps=1e6, conv_threshold=1e-3):
    f1, f2 = 0.7 * R, 0.01 * R
    rtt1, rtt2 = 1, RTT_ratio
    ssth1 = ssth2 = ssth_ratio * R
    history = []
    converged = False
    
    for step in range(int(max_steps)):
        if f1 + f2 > R:
            f1 *= 0.5
            f2 *= 0.5
            ssth1 = f1  # On congestion, each flow sets ssth = current cwnd
            ssth2 = f2
        else:
            if f1 < ssth1:
                f1 += f1 * (1 / rtt1)  # Slow start (exponential)
            else:
                f1 += (1 / rtt1)       # Congestion avoidance (linear)
            
            if f2 < ssth2:
                f2 += f2 * (1 / rtt2)
            else:
                f2 += (1 / rtt2)
        
        history.append((f1/R, f2/R))
        
        # Convergence check
        if abs(f1 - R/2) < conv_threshold and abs(f2 - R/2) < conv_threshold:
            converged = True
            break
    
    return np.array(history), converged, step + 1

R = 2e4
cases = [
    ("Same RTT", 1),
    ("Different RTT (10:1)", 10)
]

plt.figure(figsize=(12, 6))

# Reference line for fairness (f1 + f2 = R)
x_ref = np.linspace(0, 1, 100)
y_ref = 1 - x_ref

for i, (title, rtt_ratio) in enumerate(cases):
    results, converged, steps = simulate_tcp_fairness(R, rtt_ratio)
    
    # Adding plots
    plt.subplot(1, 2, i+1)
    plt.plot(results[:, 0], results[:, 1], marker='.', linestyle='-', markersize=2)
    plt.plot(x_ref, y_ref, 'r--', label='Fairness Line')
    plt.title(title)
    plt.xlabel('f1/R')
    plt.ylabel('f2/R')
    plt.grid(True)
    plt.axis([0, 1, 0, 1])
    
    # Adding convergence info
    conv_text = f"Converged: {converged}\nSteps: {steps}"
    plt.text(0.05, 0.95, conv_text, 
             transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.legend()
plt.show()
