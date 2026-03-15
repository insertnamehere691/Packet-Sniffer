from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        print(f"[*] Connection: {src_ip} -> {dst_ip} | Protocol: {proto}")

print("[+] Starting sniffer... Press Ctrl+C to stop.")
# This captures 10 packets and calls our function for each one
sniff(filter="ip", prn=packet_callback, count=10)
