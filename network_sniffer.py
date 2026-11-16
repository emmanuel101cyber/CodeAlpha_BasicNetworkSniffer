#!/usr/bin/env python3

"""
Basic Network Packet Sniffer
Author: Idowu Oluwaferanmi Emmanuel

A Python-based packet sniffer using Scapy.
Captures and analyses IP packets for network security monitoring.
"""

import argparse
from datetime import datetime

from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS, DNSQR


def analyse_packet(packet):

    if IP not in packet:
        return

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_size = len(packet)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    protocol = "OTHER"
    source_port = "N/A"
    destination_port = "N/A"

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"

    print("\n" + "=" * 55)
    print("NETWORK PACKET DETECTED")
    print("=" * 55)

    print(f"Timestamp:          {timestamp}")
    print(f"Source IP:          {source_ip}")
    print(f"Destination IP:     {destination_ip}")
    print(f"Protocol:           {protocol}")
    print(f"Source Port:        {source_port}")
    print(f"Destination Port:   {destination_port}")
    print(f"Packet Size:        {packet_size} bytes")

    if DNS in packet and DNSQR in packet:
        query = packet[DNSQR].qname.decode(errors="ignore")
        print(f"DNS Query:          {query}")

    print("=" * 55)


def start_sniffer(interface, count, packet_filter):

    print("\n" + "=" * 55)
    print("PYTHON NETWORK PACKET SNIFFER")
    print("=" * 55)

    print(f"Interface: {interface}")
    print(f"Packet Filter: {packet_filter or 'None'}")
    print(f"Packet Limit: {count if count else 'Unlimited'}")

    print("\nListening for network traffic...")
    print("Press CTRL+C to stop capturing.\n")

    try:
        sniff(
            iface=interface,
            prn=analyse_packet,
            filter=packet_filter,
            count=count,
            store=False
        )

    except KeyboardInterrupt:
        print("\nPacket capture stopped.")

    except Exception as error:
        print(f"\nError: {error}")


def main():

    parser = argparse.ArgumentParser(
        description="Python Network Packet Sniffer using Scapy"
    )

    parser.add_argument(
        "-i", "--interface",
        required=True,
        help="Network interface to monitor"
    )

    parser.add_argument(
        "-c", "--count",
        type=int,
        default=0,
        help="Number of packets to capture (0 means unlimited)"
    )

    parser.add_argument(
        "-f", "--filter",
        default="",
        help="BPF packet filter, e.g. tcp, udp or icmp"
    )

    args = parser.parse_args()

    if args.count < 0:
        parser.error("Packet count cannot be negative.")

    start_sniffer(
        args.interface,
        args.count,
        args.filter
    )


if __name__ == "__main__":
    main()
