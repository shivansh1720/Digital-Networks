
# EE673 Digital Communication Networks - Assignment 2

**Roll Number:** 221021
**Name:** Shivansh Mangal
**Date:** April 13, 2025

---

## Question 1: Wireshark Labs

### TCP Section (7.5 marks)

#### TCP.1

**Answer:** I was not able to download the author's trace . Therefore, I have answered all the questions based on my trace which is avaailable in the zip file along side.

The source IP i.e. my IP address is 172.23.16.145

#### TCP.2

**Answer:** The IP address of the website for gia.cs.umass.edu is 128.119.245.12 and port is 80 for the communication .

#### TCP.3

**Answer:** As per the frame 143 from the attached trace which sends the post request for uploading the alice.txt to destination website; my client computer's
IP is 172.23.16.145 

### TCP.4

**Answer:**The sequence no. for TCP SYN segment used to initiate connection between client and server is 0(relative) and raw sequence no. is 3263221876 and it is identified as SYN as flag corresponding to this packet si set to 0x002 (SYN). Frame-36 in the trace.

### TCP.5

**Answer:**The sequence no. for TCP SYN_ACk segment used to reply by server to client is 0(relative) and raw sequence no. is 2970056865 identified SYN-ACK as flag corresponding to this packet is set to 0x012. Frame-38 in the attached trace.

### TCP.6

**Answer:** The sequence no. of packet containing POST command is 3263221877. Frame no.143 in the attached trace.

### TCP.7

**Answer:**
| Packet No. | Sequence No. | Time | Time when Ack recieved|
| 1 | 3263221877 | 5.128985448 | 5.135717699 |
| 2 | 3263222509 | 5.129175166 | 5.426379353 |
| 3 | 3263223747 | 5.129183361 | 5.426379473 |
| 4 | 3263334985 | 5.129197838 | 5.426379583 |



## Question 3: TCP Fairness

### Simulation Code

```python
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

```
I have attached plots for 5 different values of R and SSTH. It was observed that in every case the convergence to fairness for observed only for equal flow rates.

---