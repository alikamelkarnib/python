#les inclusions
import sys
import os
from random import randint

# créer les fonction 
def initialisation():
    outputfile = "output.txt" 
    tailleSequences = 10  
    nbSequences = 10 
    formatOutput = "fasta"  
    nomEspece = "Espece" 
    #toutes ces valeurs sont en défauts
    return outputfile, tailleSequences, nbSequences, formatOutput, nomEspece

def extraireArgument(argument):
     #Extrait la clé et la valeur de l'argument
     if("-formatSortie=" in argument or "-nbSequences=" in argument or "-tailleSequences=" in argument or "-fichierSortie=" in argument or "-nomEspece=" in argument):
        key, value = argument.split("=")
        return key, value
     else:
       key,value="-help"," "
       return key,value

def valideOutputFile(value):
     #Valide et retourne le nom du fichier de sortie
    if os.path.exists(value):
        quitterProgramme("Erreur: Le fichier de sortie existe déjà.")
    return value

def valideEntierPositif(value):
    #Vérifie si la taille est un entier positif
    try:
        int_value = int(value)
        if int_value < 0:
            quitterProgramme("Erreur: La valeur doit être un entier positif.")
        return int_value
    except ValueError:
        quitterProgramme("Erreur: La valeur doit être un entier.")

def valideFormatOutfile(value):
 # Vérifie si le format est soit "fasta" soit "phylip"
       if value not in ['fasta', 'phylip']:
        quitterProgramme("Erreur: Format de sortie non valide. Utiliser 'fasta' ou 'phylip'.")
       return value

def valideNomEspece(value):
    # Vérifie si le nom de l'espèce est une chaîne de caractère
    if value in "1234567890":
        quitterProgramme("Le nom de l'espèce doit etre une chaine de caractère qui ne contient auncun chiffre .")  
    return value

def help():
#Affiche des informations d'aide sur l'utilisation du script lors d'une erreur.
    print("Liste des options de la ligne de commande\n"
          "Options :\n"
          "  -fichierSortie : nom du fichier de sortie. Le fichier ne doit pas exister. Si l’option n’est pas fournit le fichier par défaut sera output.txt.\n"
          "  -formatSortie : fasta ou phylip. Format du fichier de sortie. \n"
          "  -tailleSequences : entier. Taille des séquences\n"
          "  -nbSequences : entier. Nombre de séquences à générer\n"
          "  -nomEspece : chaine de caractère. Format du nom des espèces. Un compteur sera utilisé pour chaque séquence.\n"
          "  -help : Affiche de l'aide\n")
          
def quitterProgramme(message):
    print(message)
    sys.exit(1)

def sauvegarderSequences(sequences, outputfile, formatOutput, nomEspece):
# Sauvegarde les séquences dans le fichier de sortie avec le format spécifié
    with open(outputfile, 'w') as f:
        if formatOutput == "fasta":
            for i, sequence in enumerate(sequences, 1):
                f.write(f">{nomEspece}{i}\n{sequence}\n")
        elif formatOutput == "phylip":
            f.write(f"{len(sequences)} {len(sequences[0])}\n")
            for i, sequence in enumerate(sequences, 1):
                f.write(f"{nomEspece}{i} {sequence}\n")

def genererJeuSequences(tailleSequences, nbSequences):
    # Génère un jeu de séquences aléatoires d'ADN
  import random
  sequences=[]
  caracteres_autorises = 'ACGT'

  for j in range(nbSequences):
     seq=[]
     for l in range(tailleSequences):
          seq.append(random.choice(caracteres_autorises))
     sequences.append(''.join(seq))
     
  return sequences

def presentation():
    print("""=====================================================
- generateur-sequences.py 
- Ce programme permet de générer un jeu de séquences
- Auteur : Fatima Mawassi
- Date : 8 Décembre 2023
- script : conversion.py
- Version : 1.0
- Cours : INF8212 
=====================================================""")




    