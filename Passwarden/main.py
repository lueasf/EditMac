
import os.path # os.path est une lib qui permet de manip les fichiers
import subprocess
import sys
import random
import string
import bcrypt
import stdiomask

# FUNC 1
def checkExistence():
    if os.path.exists("vault.txt"):
        pass
    else:
        file = open("vault.txt", "w")
        file.close()

# FUNC 2
def append_new_passw():
    with open("vault.txt", "a") as appender :
        print()
        username = input("Entrez le nom d'utilisateur : ")
        password = stdiomask.getpass(prompt = "Entrez le mot de passe : ", mask = "#")
        app = input("Entrez l'application : ")
        print()

        usernameLine = "Nom d'utilisateur : " + username + "\n"
        passwordLine = "Mot de passe : " + password + "\n"
        appLine = "Application : " + app + "\n"

        appender.write("-" * 50 + "\n")
        appender.write(usernameLine)
        appender.write(passwordLine)
        appender.write(appLine)
        appender.write("-" * 50 + "\n")

# FUNC HASH INUTILE car on ne peut pas déchiffrer le mot de passe
def hashpass(password):
    salt = bcrypt.gensalt() # génère un sel
    hash = bcrypt.hashpw(password.encode('utf-8'), salt) # hashpw permet de hasher le mot de passe

# FUNC 3
def readPasswords():
    content = ''
    with open("vault.txt", "r") as reader:
        content = reader.read() # read() permet de lire tout le contenu du fichier
    print()
    print(content)

# FUNC 4
def generatePassw(length):
    randomString = string.ascii_letters + string.digits + string.punctuation # pour avoir ts les char.
    newPass = ''
    for i in range(length):
        newPass += random.choice(randomString) 
    print()
    print("Mot de passe : " + newPass)

# MAIN
subprocess.call('clear', shell=True)

print("-" *30 + " Passwarden " + "-" *30)
print()
print("choisissez une option :")
print("1. Ajouter un mot de passe")
print("2. Générer un mot de passe")
print("3. Lire les mots de passe")

choix = input("Votre choix : (1, 2 ou 3) ")

if choix == "1":
    checkExistence()
    append_new_passw()
elif choix == "2":
    length = input("Entrez la longueur du mot de passe : ")
    if not string.ascii_letters in length:
        generatePassw(int(length))
    else:
        print("Entrez un nombre.")
        sys.exit()

elif choix == "3":
    readPasswords()
else:
    print("Choix invalide.")
    sys.exit()
