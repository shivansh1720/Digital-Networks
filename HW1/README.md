# EE673 Digital Communication Networks - Assignment 1

<!-- ## Submission Information
- **Course:** EE673 - Digital Communication Networks
- **Assignment:** 1
- **Submitted By:** [Your Name]
- **Roll No:** [Your Roll Number]
- **Submission Date:** [Date]

## Directory Structure
```
.
├── EE673_2025_Assignment_1.pdf  # Assignment PDF
├── Q1_tcp.py                     # TCP Client-Server Implementation
├── Q1_udp.py                     # UDP Client-Server Implementation
├── Q2.py                         # UDP Chat Application
└── README.md                     # This file
```

--- -->

## Question 1: TCP & UDP Client-Server Implementation

### **1. TCP Client-Server (Q1_tcp.py)**
#### **How to Run**
1. Open a terminal and start the server:
   ```bash
   python3 Q1_tcp.py server
   ```
2. Open another terminal and start the client:
   ```bash
   python3 Q1_tcp.py client
   ```
3. The client will send a message, and the server will respond with the message converted to uppercase.

### **2. UDP Client-Server (Q1_udp.py)**
#### **How to Run**
1. Start the UDP server:
   ```bash
   python3 Q1_udp.py server
   ```
2. Start the UDP client:
   ```bash
   python3 Q1_udp.py client
   ```
3. The client sends a message, and the server returns the uppercase version of the message.

---

## Question 2: UDP Chat Application (Q2.py)

### **How to Set Up & Run**
This application allows **two-way chat** between a PC and a mobile device using **UDP Monitor**.

### **1. Install & Configure UDP Monitor on Mobile**
- **Download UDP Monitor** from the Play Store: [UDP Monitor](https://tinyurl.com/udpMonitor)
- Open the app and note your phone’s **Local IP** (e.g., `192.168.1.100`).
- Set **Local Port** (e.g., `6000`).
- Enter your **PC’s Local IP** and **Remote Port** (e.g., `5000`).

### **2. Find Your PC’s Local IP**
Run the following command in a terminal:
```bash
ip a  # Linux/macOS
ipconfig  # Windows
```
Example output:
```
wlo1: inet 192.168.1.50  # Your PC’s IP
```

### **3. Run the UDP Chat Application**
On your **PC**, start the chat by running:
```bash
python3 Q2.py 5000 <Mobile_IP> 6000
```
Example:
```bash
python3 Q2.py 5000 192.168.1.100 6000
```

### **4. Start Chatting**
- **Messages sent from PC** will appear on **UDP Monitor (Mobile)**.
- **Messages sent from Mobile (UDP Monitor)** will appear in the **PC terminal**.
- Type **"exit" or "bye"** in either device to end the chat.

---

## Notes
- Both the applications are able to recieve only messaages which are about 1024 characters long. For messages longer than this , Only first 1024 characters will be recieved.
- Ensure that both **PC and mobile** are on the **same network**.
- The UDP chat uses **multi-threading**, so both sending and receiving work in parallel.
- The application properly **exits when "exit" or "bye" is received**.
- You can use keyboard interupts to close the servers in Q1.

---


