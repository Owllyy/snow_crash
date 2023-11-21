from scapy.all import *

packets = rdpcap('level02/Ressources/level02.pcap')

# Let's iterate through every packet
for packet in packets:
    pakcet.show(label_lvl: str = 'load')