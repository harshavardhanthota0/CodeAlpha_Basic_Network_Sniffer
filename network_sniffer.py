#!/usr/bin/env python3
"""Educational packet-metadata viewer. Use only on networks you are authorized to monitor."""
import argparse
from datetime import datetime

try:
    from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, ARP
except ImportError:
    print("Scapy is not installed. Run: python -m pip install -r requirements.txt")
    raise SystemExit(1)

def describe_packet(packet):
    timestamp = datetime.now().strftime("%H:%M:%S")
    length = len(packet)
    src = dst = "N/A"
    protocol = "Other"
    details = ""

    if ARP in packet:
        src, dst, protocol = packet[ARP].psrc, packet[ARP].pdst, "ARP"
    elif IP in packet:
        src, dst = packet[IP].src, packet[IP].dst
        if TCP in packet:
            protocol = "TCP"
            details = f"ports {packet[TCP].sport} -> {packet[TCP].dport}"
        elif UDP in packet:
            protocol = "UDP"
            details = f"ports {packet[UDP].sport} -> {packet[UDP].dport}"
        elif ICMP in packet:
            protocol = "ICMP"
    elif IPv6 in packet:
        src, dst = packet[IPv6].src, packet[IPv6].dst
        if TCP in packet:
            protocol = "TCP"
            details = f"ports {packet[TCP].sport} -> {packet[TCP].dport}"
        elif UDP in packet:
            protocol = "UDP"
            details = f"ports {packet[UDP].sport} -> {packet[UDP].dport}"
        else:
            protocol = "IPv6"

    suffix = f" | {details}" if details else ""
    print(f"{timestamp} | {protocol:<6} | {src} -> {dst} | {length} bytes{suffix}")

def main():
    parser = argparse.ArgumentParser(description="Display metadata from authorized network packet captures.")
    parser.add_argument("-c", "--count", type=int, default=20,
                        help="packets to capture (default: 20; 0 means continuous)")
    parser.add_argument("-i", "--interface", default=None, help="network interface (optional)")
    args = parser.parse_args()
    if args.count < 0:
        parser.error("--count must be 0 or greater")

    print("CodeAlpha Basic Network Sniffer")
    print("Only monitor traffic you own or are explicitly authorized to inspect.")
    print("Packet payloads are not printed.")
    print("Press Ctrl+C to stop.\n")
    try:
        sniff(prn=describe_packet, count=args.count, iface=args.interface, store=False)
    except PermissionError:
        print("\nPermission denied. Use an elevated terminal only if permitted.")
        raise SystemExit(1)
    except KeyboardInterrupt:
        print("\nCapture stopped.")
    except OSError as exc:
        print(f"\nCapture error: {exc}")
        print("Check the interface name, permissions, and packet-capture driver.")

if __name__ == "__main__":
    main()
