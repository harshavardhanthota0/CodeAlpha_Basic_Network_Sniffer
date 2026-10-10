# CodeAlpha_Basic_Network_Sniffer

A beginner-friendly Python network sniffer for CodeAlpha Cyber Security Internship Task 1. It displays packet metadata: source/destination addresses, protocol, packet size, and TCP/UDP ports.

## Features
- Captures packets using Scapy
- Recognizes IPv4, IPv6, ARP, TCP, UDP, and ICMP where available
- Displays timestamp, addresses, protocol, packet length, and ports
- Configurable packet count and optional network interface
- Does not print packet payloads or collect credentials

## Requirements
- Python 3.9+ recommended
- Scapy
- A supported packet-capture environment; administrator/root privileges may be required

## Setup
1. Download or clone the repository.
2. In a terminal in the project folder, install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Run the sniffer:
   ```bash
   python network_sniffer.py --count 20
   ```
   Capture 50 packets:
   ```bash
   python network_sniffer.py --count 50
   ```
   Continuous capture (stop with Ctrl+C):
   ```bash
   python network_sniffer.py --count 0
   ```
   Choose an interface if needed:
   ```bash
   python network_sniffer.py --count 20 --interface "INTERFACE_NAME"
   ```
   Replace `INTERFACE_NAME` with an interface available on your computer.

### Windows note
Packet capture on Windows may require Npcap. Install it from its official website and follow its instructions. Run with elevated permissions only when necessary and authorized.

## Example output
```text
20:15:01 | TCP    | 192.168.1.10 -> 142.250.72.14 | 60 bytes | ports 51520 -> 443
20:15:02 | UDP    | 192.168.1.10 -> 192.168.1.1 | 78 bytes | ports 53000 -> 53
```
These are illustrative examples, not actual captured traffic.

## Safety
Use this tool only on your own device/network or with explicit permission. Packet metadata can be sensitive. Do not intercept or disclose other people's traffic or use this tool to collect credentials.

## Limitations
Visible packet details depend on your OS, interface, permissions, and network. Encrypted application traffic is not displayed as plaintext. This is an educational demo, not a production intrusion-detection system.

## Submission checklist
- [ ] Install Scapy and test capture in an authorized environment.
- [ ] Upload `network_sniffer.py`, `requirements.txt`, and `README.md`.
- [ ] Use repository name `CodeAlpha_Basic_Network_Sniffer`.
- [ ] Record a short demo and explain the output and safe-use boundaries.
- [ ] Submit the repository link using the official CodeAlpha submission form.

## Technologies
Python, Scapy
