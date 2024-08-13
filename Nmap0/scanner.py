import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

ip = input("Quel est l'IP de la machine à scanner ?")

print("-" * 70)
print("scan en cours...")
print("-" * 70)

aucun = 0

t1 = datetime.now()

try:
    for port in range(1, 27):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # on ouvre une connexion TCP avec ipv4. AF_INET6 pour ipv6.
        res = sock.connect_ex((ip, port))
        if res == 0:  # Si la connexion est réussie
                aucun = 1
                try:
                    service = socket.getservbyport(port)  # Récupère le nom du service associé au port
                except OSError:
                    service = "Service inconnu"
                print(f"Port {port} ({service}) : Ouvert")
        sock.close()

    if aucun == 0:
        print("Aucun port ouvert")
            

except KeyboardInterrupt:
    sys.exit()

except socket.error:
    print("Impossible de se connecter à l'IP")
    sys.exit()

t2 = datetime.now()

t3 = t2-t1
print("temps d'execution : {}".format(str(t3)))

