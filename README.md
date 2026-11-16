# Network Packet Sniffer Using Python and Scapy

A Python-based network packet sniffer developed using Scapy to capture, monitor, and analyse network traffic for cybersecurity and network security analysis.

## Project Overview

This project involves developing a lightweight network packet sniffer capable of capturing and analysing IP packets transmitted across a network interface.

The tool provides visibility into network communications by identifying source and destination IP addresses, detecting network protocols, inspecting transport-layer information, identifying DNS queries, and displaying relevant packet metadata.

The project demonstrates practical knowledge of TCP/IP networking, packet inspection, Python programming, and network security monitoring.

## Project Objectives

- Capture live network traffic from a specified network interface.
- Identify source and destination IP addresses.
- Detect TCP, UDP, and ICMP protocols.
- Extract source and destination port numbers.
- Identify and display DNS queries.
- Inspect packet timestamps and sizes.
- Apply Berkeley Packet Filter (BPF) expressions.
- Develop a command-line network monitoring tool.

## Technologies and Tools

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Scapy | Packet capture and analysis |
| Kali Linux | Development and testing environment |
| TCP/IP | Network communication protocols |
| Wireshark | Packet analysis and verification |
| libpcap | Packet capture and BPF filtering support |

## Project Features

### 1. Live Packet Capture
Captures IP packets transmitted through a specified network interface.

### 2. IP Address Identification
Extracts and displays source and destination IP addresses.

### 3. Protocol Detection
Identifies common network protocols:
- TCP
- UDP
- ICMP

### 4. Port Inspection
Extracts source and destination port numbers from TCP and UDP packets.

### 5. DNS Query Detection
Identifies DNS queries and extracts requested domain names when available.

### 6. Packet Filtering
Supports Berkeley Packet Filter (BPF) expressions to filter network traffic based on specified protocols or ports.

### 7. Packet Metadata Analysis
Displays:
- Packet timestamp
- Packet size
- Source IP address
- Destination IP address
- Protocol type
- Source and destination ports

## Project Structure

```text
CodeAlpha_BasicNetworkSniffer/
│
├── network_sniffer.py
├── README.md
├── requirements.txt
└── screenshots/
    ├── installation.png
    ├── packet_capture.png
    ├── protocol_detection.png
    ├── dns_detection.png
    └── packet_filtering.png
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/emmanuel101cyber/CodeAlpha_BasicNetworkSniffer.git
```

### 2. Navigate to the Project Directory

```bash
cd CodeAlpha_BasicNetworkSniffer
```

### 3. Install Dependencies

Update the Kali Linux package repository:

```bash
sudo apt update
```

Install Scapy and packet capture dependencies:

```bash
sudo apt install python3-scapy tcpdump libpcap-dev
```

###
