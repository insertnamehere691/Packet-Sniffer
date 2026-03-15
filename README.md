# Packet-Sniffer
A lightweight network monitoring tool developed in Python using the Scapy library. This project was created to demonstrate the fundamentals of network traffic analysis, packet structure, and the OSI model. It captures live IP traffic and extracts key metadata including source/destination addresses and protocol types.
Features
Real-time Capture: Intercepts live IP packets passing through the Network Interface Card (NIC).

Protocol Identification: Automatically identifies and categorizes traffic (TCP, UDP, ICMP).

Linux Optimized: Designed to run in a Kali Linux environment using administrative privileges for promiscuous mode monitoring.

How It Works
The script utilizes a callback function to process each captured packet. It checks for the presence of the IP Layer and then parses the following:

Source IP: The origin of the packet.

Destination IP: The intended recipient.

Protocol Number: The transport layer protocol (e.g., 6 for TCP, 17 for UDP).

Usage

Clone the repo:
git clone https://github.com/your-username/python-sniffer.git

Install dependencies:
sudo apt install python3-scapy

Run with sudo:
sudo python3 sniffer.py

Legal Disclosure: 
This tool is intended for educational and authorized security testing purposes only. It was developed to better understand network forensics and defensive security measures within a controlled lab environment.
