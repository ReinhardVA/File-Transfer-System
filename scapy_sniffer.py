from scapy.all import sniff
from scapy.layers.inet import IP, UDP
from common.config import PORT

def packet_callback(packet):
    print("IP: ", IP)
    print("UDP: ", UDP)
    print(":::: ", packet[0][UDP].dport)
    
    if IP in packet and UDP in packet:
        if packet[0][UDP].dport == PORT:  
            ip_layer = packet[IP]
            print(f"\n[+] Packet captured:")
            print(f"    Source IP     : {ip_layer.src}")
            print(f"    Destination IP: {ip_layer.dst}")
            print(f"    TTL           : {ip_layer.ttl}")
            print(f"    Flags         : {ip_layer.flags}")
            print(f"    Fragment Offset: {ip_layer.frag}")
            print(f"    Checksum      : {ip_layer.chksum}")
            print(f"    Total Length  : {ip_layer.len}")


def start_sniffing():
    print(f"Listening for UDP packets on port {PORT}...")
    sniff(iface="Wi-Fi", filter="udp", prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffing()
   

