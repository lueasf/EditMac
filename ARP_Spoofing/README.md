# ARP Spoofing

L'ARP Spoofing (la parodie ARP) est une technique qui consiste à envoyer des trames ARP falsifiées pour se faire passer pour une autre machine. Il s'agit d'un Man-in-the-middle. Man-in-the-middle, consiste à se placer entre deux machines pour intercepter les échanges.

## Rappel
ARP est un protocole de la couche 2 (MAC) qui permet de faire correspondre une adresse IP à une adresse MAC. Il est utilisé pour déterminer l'adresse MAC d'une machine à partir de son adresse IP.
On trouve souvent la question "Who has IP x.x.x.x ? Tell IP y.y.y.y" dans les trames ARP.

## Exercice
Réaliser un ARP Spoofing via un script python.

## Principe
Pour réaliser cet exercice, on va utiliser une VM Virtualbox Windows10 sur linux.
On doit configurer le réseau de la VM en bridge pour que:
-les ip soient différentes (assigné par DHCP)
-la VM ets visible sur le réseau local (comme une machine physique)
-la VM à son propre accès internet
Contrairement au mode NAT par défaut qui ne permet pas de voir la VM depuis le réseau local.

Une fois la VM configurée, on peut voir avec *ipconfig* sur la VM qu'une adresse IP a été attribuée et qu'elle est dans le meme réseau que la machine hôte. (ici 192.168.68.). On utilise *ifconfig* sur linux.

Pour continuer l'experience, il faut passer le réseau du public à privée dans les paramètres de réseau de la VM, sinon windows va bloquer les paquets ARP. De plus, il est possible de pouvoir ping linux depuis la VM mais l'inverse. Dans ce cas, il faut activer la règle : "File and Printer Sharing (Echo Request - ICMPv4-In)" dans les paramètres avancés du pare-feu de Windows.

On peut faire :
```bash
arp -a
``` 
dans le terminal linux afin de voir les machines connectées au réseau. On trouve bien le routeur et la VM avec ses adresses ip et MAC. En effet, grace au mode bridge, la VM a une carte réseau virtuelle.


## Librairies
- scapy (pip install)

## attaques
on fait dabord un ping des deux cotés pour mettre les adresses MAC dans la table ARP.
puis on verifie avec arp -a que les adresses MAC sont bien enregistrées.
enfin on fait sudo python3 arp_spoofing.py pour lancer l'attaque.
et on peut voir sur la VM avec un arp -a que l'adresse MAC du linux est mnt associé à l'ip du linux ET du routeur.