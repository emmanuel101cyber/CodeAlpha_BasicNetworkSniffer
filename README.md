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

### 4. Verify Installation

```bash
python3 -c "import scapy.all; print('Scapy installed successfully')"
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

## Testing and Validation

The application will be tested using controlled network traffic to validate:

- Successful packet capture.
- Correct source and destination IP identification.
- TCP, UDP, and ICMP protocol detection.
- Source and destination port extraction.
- DNS query identification.
- Packet size and timestamp extraction.
- Successful application of packet filters.

Wireshark may be used to independently verify captured packet information.

## Security and Ethical Considerations

This tool is intended for educational purposes, authorised network monitoring, and controlled cybersecurity laboratory environments.

Network packet capture should only be performed on networks and devices that you own or have explicit permission to monitor.

The application focuses on packet metadata and selected protocol headers. It does not decrypt encrypted network communications.

## Learning Outcomes

This project demonstrates practical experience in:

- Network packet analysis.
- TCP/IP protocol fundamentals.
- Python network programming.
- Network traffic monitoring.
- DNS inspection.
- Packet filtering.
- Command-line tool development.
- Basic network security analysis.

## Project Status

Development and testing in progress.

## Author

**Idowu Oluwaferanmi Emmanuel**

Cybersecurity | Network Security | Ethical Hacking

GitHub: https://github.com/emmanuel101cyber

Developed as part of the CodeAlpha Cybersecurity Internship.
