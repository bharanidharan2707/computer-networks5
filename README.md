# Network Packet Analyzer

## Project Overview
Network Packet Analyzer is a beginner-level Computer Networks project developed using Python and Flask. It captures network packets and displays information such as source IP address, destination IP address, protocol type, and packet size through a web dashboard.

## Features
- Capture IP network packets.
- Display source IP address.
- Display destination IP address.
- Identify TCP, UDP, and ICMP protocols.
- Display packet size in bytes.
- Start and stop packet capturing.
- Real-time web dashboard updates.

## Technologies Used
- Python
- Flask
- Scapy
- HTML
- CSS
- JavaScript

## Project Structure

```text
NetworkPacketAnalyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Network-Packet-Analyzer.git
```

### 2. Open the project folder

```bash
cd Network-Packet-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install Npcap

Windows users need Npcap for packet capture.

Download: https://npcap.com/#download

## Run the Application

Open VS Code or PowerShell as Administrator if required.

```bash
python app.py
```

Open your browser:

http://127.0.0.1:5004

## How to Use

1. Start the application.
2. Open the web dashboard.
3. Click the Start Capture button.
4. Generate network traffic by opening websites.
5. View packet information in the dashboard.
6. Click Stop Capture to stop monitoring.

## Sample Output

| Source IP | Destination IP | Protocol | Packet Size |
|---|---|---|---|
| 192.168.1.5 | 142.250.183.14 | TCP | 60 bytes |
| 192.168.1.5 | 8.8.8.8 | UDP | 70 bytes |

*Example values only. Actual packet details depend on network traffic.*

## Networking Concepts
- IP addressing
- TCP protocol
- UDP protocol
- ICMP protocol
- Network packet structure
- Packet capturing
- Network monitoring

## Learning Objectives
- Understand how network packets travel.
- Identify source and destination IP addresses.
- Learn basic network protocols.
- Understand packet capture using Python.
- Build a simple network monitoring dashboard.

## Security Note
This project is intended for educational purposes. Capture only network traffic that you own or have permission to monitor. The application displays packet metadata and does not inspect message contents.

## Author
Bharanidharan

## License
Created for educational purposes.
