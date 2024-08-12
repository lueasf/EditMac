#!/usr/bin/python3

import subprocess
import optparse
import re

# FUNC 1 renvoie l'adresse MAC trouvée
def search_mac(string):
    return re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', str(string)).group(0)

# FUNC 2 récupère l'adresse MAC actuelle
def get_current_mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig",interface])
    # on stoque le resultat de la commande ifconfig dans ifconfig_res
    mac_search = search_mac(ifconfig_res)
    if mac_search:
        return mac_search
    else:
        print("[-] Impossible de trouver une adresse MAC")

# FUNC 3 récupère les arguments
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface à changer") # option est un objet et option.interface est un attribut
    parser.add_option("-m", "--mac", dest="new_mac", help="Nouvelle adresse MAC")
    (options, args) = parser.parse_args()  
    if not options.interface:
        parser.error("[-] Spécifiez une interface avec -i ou --interface, utiliser --help pour + d'infos.")
    elif not options.new_mac:
        parser.error("[-] Spécifiez une nouvelle adresse MAC avec -m ou --mac, utiliser --help pour + d'infos.")
    return options

# interface = input("Choisis une interface : ")
# new_mac = input("Choisis une nouvelle adresse MAC : ")

options = get_args()
current_mac = get_current_mac(options.interface)

# FUNC 4 change l'adresse MAC
def set_new_mac(interface, new_mac):
    print("[+] changement d'adresse MAC pour l'interface " + interface + " de " + current_mac + " à " + new_mac)
    subprocess.call("ifconfig " + interface + " down", shell=True) # on peut appeler une commande shell avec subprocess.call
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True) # changer (hw pour hardware) une adr MAC (ether)
    subprocess.call("ifconfig " + interface + " up", shell=True) 

set_new_mac(options.interface, options.new_mac)