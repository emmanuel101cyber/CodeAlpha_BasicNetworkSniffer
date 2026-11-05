# CodeAlpha Basic Network Sniffer

A Python-based network packet sniffer developed using Scapy to capture, monitor, and analyse network traffic for cybersecurity and network security analysis.

## Project Overview

This project involves developing a basic network sniffer capable of capturing and analysing IP packets transmitted across a network interface.

The tool provides visibility into network communications by identifying source and destination IP addresses, detecting network protocols, inspecting packet headers, and displaying relevant packet information.

The project demonstrates practical knowledge of network protocols, packet inspection, Python programming, and network security monitoring.

## Objectives

- Capture live network traffic.
- Identify source and destination IP addresses.
- Detect TCP, UDP, and ICMP protocols.
- Extract source and destination port numbers.
- Identify DNS queries.
- Inspect packet sizes and timestamps.
- Apply packet filtering during network capture.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Scapy | Packet capture and analysis |
| Kali Linux | Development and testing environment |
| TCP/IP | Network communication protocols |
| Wireshark | Network traffic verification |

## Project Structure

```text
CodeAlpha_BasicNetworkSniffer/
│
├── network_sniffer.py
├── README.md
├── requirements.txt
└── screenshots/
```

## Features

### 1. Packet Capture
Captures live IP packets from a specified network interface.

### 2. IP Address Identification
Extracts source and destination IP addresses from captured packets.

### 3. Protocol Detection
Identifies common network protocols, including:
- TCP
- UDP
- ICMP

### 4. Port Inspection
Displays source and destination port numbers for TCP and UDP packets.

### 5. DNS Query Detection
Identifies DNS queries and extracts requested domain names when available.

### 6. Packet Filtering
Supports Berkeley Packet Filter (BPF) expressions to narrow down captured traffic.

### 7. Packet Information
Displays packet timestamps, lengths, protocols, and addressing information.

## Installation

Clone the repository:

```bash
git clone https://github.com/emmanuel101cyber/CodeAlpha_BasicNetworkSniffer.git
```

Navigate into the project directory:

```bash
cd CodeAlpha_BasicNetworkSniffer
```

Install Scapy:

```bash
sudo apt update
sudo apt install python3-scapy
```

## Usage

Run the network sniffer:

```bash
sudo python3 network_sniffer.py -i eth0
```

Capture a specified number of packets:

```bash
sudo python3 network_sniffer.py -i eth0 -c 30
```

Capture TCP traffic:

```bash
sudo python3 network_sniffer.py -i eth0 -f "tcp"
```

Capture UDP traffic:

```bash
sudo python3 network_sniffer.py -i eth0 -f "udp"
```

Replace `eth0` with the actual network interface available on your system.

## Security and Ethical Considerations

This tool is intended for educational purposes, authorised network monitoring, and controlled cybersecurity laboratory environments.

Network packet capture should only be performed on networks and devices that you own or have explicit permission to monitor.

The tool does not decrypt encrypted network communications.

## Learning Outcomes

Through this project, the following practical skills are explored:

- Network packet analysis.
- TCP/IP protocol fundamentals.
- Python network programming.
- Network traffic monitoring.
- DNS inspection.
- Basic network security analysis.
- Command-line tool development.

## Project Status

Development and testing in progress.

## Author

**Idowu Oluwaferanmi Emmanuel**

Cybersecurity | Network Security | Ethical Hacking

GitHub: [@emmanuel101cyber](https://github.com/emmanuel101cyber)

---

Developed as part of the CodeAlpha Cybersecurity Internship.
