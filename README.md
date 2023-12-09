Description du travail
Le but de ce travail est d’écrire un script Python permettant de générer un jeu de séquences aléatoires d’ADN.
Les paramètres de génération des séquences seront fournis sur la ligne de commande.
Liste des options de la ligne de commande :
• -fichierSortie : nom du fichier de sortie. Le fichier ne doit pas exister. Si l’option n’est pas fournit le fichier par
défaut sera output.txt.
• -formatSortie : fasta ou phylip. Format du fichier de sortie.
• -tailleSequences : entier. Taille des séquences
• -nbSequences : entier. Nombre de séquences à générer
• -nomEspece : chaine de caractère. Format du nom des espèces. Un compteur sera utilisé pour chaque séquence.
• -aide : affichage de l’aide. Description des différentes options.
Au démarrage du script (generateur-sequences.py), les informations suivantes doivent apparaitre :
• nom du programme,
• description du programme,
• auteur(s),
• date,
• version du programme
Important
• Je fournis un script python generateur-sequences.py.
• Vous devez créer un script generateur.py qui sera importé.
• Chaque fonction de votre fichier doit avoir un maximum de 10 lignes.
• Les arguments de la ligne de commande doivent être validés.
• Vous ne pouvez importer que les packages os, sys et la fonction random.randint.
• Les caractères autorisés dans une séquence sont A, C, G et T.
• Vous pouvez utiliser toutes les autres fonctions de python ne nécessitant pas une importation.
