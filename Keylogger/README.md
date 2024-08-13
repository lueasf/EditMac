
L'objectif est de créer un keylogger basique en python.
Un keylogger est un logiciel qui enregistre les frappes du clavier ou autre événements d'entrée.

Pour ce faire, nous allons utiliser la librairie pynput et logging.

```python
pip install pynput.
```

On peut aussi lancer le keylogger en arrière plan avec &.
Nohup est un outil qui permet de lancer une commande en arrière plan et de ne pas être interrompu par la fermeture de la session.
```bash
nohup python keylogger.py &
```
On peut aller sur internet et taper des lettres qui seront enregistrées dans le fichier keylog.txt.
