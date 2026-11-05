from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS, DNSQR, conf
import argparse
from datetime import datetime


def analyze_packet(packet):

    if IP in packet:

        ip_layer = packet[IP]

        source_ip = ip_layer.src
        destination_ip = ip_layer.dst

        protocol = "OTHER"
        details = ""

        if TCP in packet:
            protocol = "TCP"
            details = (
                f"Source Port: {packet[TCP].sport} | "
                f"Destination Port: {packet[TCP].dport}"
            )

        elif UDP in packet:
            protocol = "UDP"
            details = (
                f"Source Port: {packet[UDP].sport} | "
                f"Destination Port: {packet[UDP].dport}"
            )

        elif ICMP in packet:
            protocol = "ICMP"
            details = f"ICMP Type: {packet[ICMP].type}"

        if DNS in packet and packet[DNS].qd:
            query = packet[DNS].qd
            if DNSQR in query:
                domain = query[DNSQR].qname.decode(
                    errors="replace"
                ).rstrip("\x00")

                details += f" | DNS Query: {domain}"

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print("\n" + "=" * 65)
        print(f"Timestamp:       {timestamp}")
        print(f"Source IP:       {source_ip}")
        print(f"Destination IP:  {destination_ip}")
        print(f"Protocol:        {protocol}")
        print(f"Packet Length:   {len(packet)} bytes")
        print(f"Details:         {details}")
        print("=" * 65)


def main():

    parser = argparse.ArgumentParser(
        description="Python Basic Network Sniffer"
    )

    parser.add_argument(
        "-i", "--interface",
        default=conf.iface,
        help="Network interface to monitor"
    )

    parser.add_argument(
        "-c", "--count",
        type=int,
        default=0,
        help="Number of packets to capture (0 = unlimited)"
    )

    parser.add_argument(
        "-f", "--filter",
        default="ip",
        help="BPF capture filter (default: ip)"
    )

    args = parser.parse_args()

    print("\n[+] CODEALPHA BASIC NETWORK SNIFFER")
    print("[+] Starting packet capture...")
    print(f"[+] Interface: {args.interface}")
    print(f"[+] Filter: {args.filter}")
    print("[+] Press CTRL+C to stop.\n")

    try:
        sniff(
            iface=args.interface,
            filter=args.filter,
            prn=analyze_packet,
            store=False,
            count=args.count
        )

    except KeyboardInterrupt:
        print("\n[!] Packet capture stopped.")

    except PermissionError:
        print("[!] Permission denied. Run with sudo.")

    except Exception as error:
        print(f"[!] Error: {error}")


if __name__ == "__main__":
    main()
