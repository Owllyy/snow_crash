from scapy.all import *

packets = rdpcap('level02/Ressources/level02.pcap')

print(b''.join(p[Raw].load for p in packets if Raw in p))