#/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import random

def genPassword():
	lettre = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	LETTRE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	chiffre = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
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
