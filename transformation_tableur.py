# coding: utf-8

import csv
import os

# Attention : le script doit etre place dans le meme dossier que le fichier a transformer

# prametres a modifier pour chaque fichier
NOM_FICHIER_ENTREE = "FD19_2021_.csv"
NOM_FICHIER_SORTIE = "FD19_2021.csv"
COLONNE_1 = 16
COLONNE_2 = 22
SEPARATEUR = ";"
COL_COORD_X = 5
COL_COORD_Y = 6
COL_DATE = 3

repertoire_actuel = os.path.dirname(__file__) # permet de selectionner l'environnement ou tout le processus se deroule.

nom_fichier_entree = os.path.join(repertoire_actuel, NOM_FICHIER_ENTREE)
with open(nom_fichier_entree, 'r') as fichier_entree:
    lecture = csv.reader(fichier_entree, delimiter=SEPARATEUR)
    futur_csv = []
    ligne_1 = next(iter(lecture)) # permet de sauter la premiere ligne (l'en-tete) sans faire de if (gourmand en ressource) + de recuperer la premiere ligne
    for ligne in lecture:
        flag = 0
        for i in ligne[COLONNE_1-1:COLONNE_2]:
            if i != "" and int(i) > 0 : # prend en compte les cases laissees vides
                future_ligne = [ligne_1[COLONNE_1-1+flag],ligne[COL_COORD_X-1],ligne[COL_COORD_Y-1],ligne[COL_DATE-1],i, ligne[0]]
                futur_csv.append(future_ligne) 
            flag += 1
# A partir de ce point j'ai cree mon tableau transforme en python. Il me reste a l'exporter en csv.

nom_fichier_sortie = os.path.join(repertoire_actuel, NOM_FICHIER_SORTIE)
with open(nom_fichier_sortie, 'w') as fichier_sortie:
    ecriture = csv.writer(fichier_sortie, delimiter=';', lineterminator='\n') # creer un fichier csv avec separateur = ;
    ecriture.writerows(futur_csv)
