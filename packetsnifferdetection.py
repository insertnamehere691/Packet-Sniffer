from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        print(f"[*] Connection: {src_ip} -> {dst_ip} | Protocol: {proto}")

        # Vulnerability Detection: Check for unencrypted HTTP traffic
        if packet.haslayer(TCP):
            if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                print(f"    [!] ALERT: Unencrypted HTTP traffic detected on port 80!")
                print(f"    [!] RISK: Credentials or sensitive data may be exposed in plain text.")

print("[+] Starting Security Sniffer... Press Ctrl+C to stop.")
sniff(filter="ip", prn=packet_callback)
