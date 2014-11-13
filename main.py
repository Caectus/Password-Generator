#/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import random
import string

def genPassword():
	lettre = list(string.ascii_lowercase)
	LETTRE = list(string.ascii_uppercase)
	chiffre = list(string.digits)
	mdpFinal = ""
	while(len(mdpFinal) < 9):
		hasard = random.randint(1, 3)
		if(hasard == 1):
			mdpAjout = random.choice(lettre)
			mdpFinal = mdpFinal + mdpAjout
		elif(hasard == 2):
			mdpAjout = random.choice(LETTRE)
			mdpFinal = mdpFinal + mdpAjout
		else:
			mdpAjout = random.choice(chiffre)
			mdpFinal = mdpFinal + mdpAjout
			
	print(mdpFinal)
genPassword()
