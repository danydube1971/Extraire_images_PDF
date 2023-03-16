"""Le script parcourt tous les fichiers dans le dossier actuel ayant l'extension ".pdf" et utilise la commande système "pdfimages" pour extraire toutes les images de chaque fichier PDF. Les images extraites sont stockées dans un dossier nommé "images PDF" créé dans le dossier actuel. Enfin, toutes les images extraites sont renommées pour qu'elles soient au format .jpg."""

import os
import subprocess

# Création du dossier pour stocker les images PDF
if not os.path.exists("images PDF"):
    os.makedirs("images PDF")

# Parcours de tous les fichiers PDF dans le dossier actuel
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        # Extraction des images à l'aide de la commande "pdfimages"
        subprocess.run(["pdfimages", "-j", filename, "images PDF/" + filename[:-4]])

        # Renommer toutes les images extraites au format .jpg
        for imagefile in os.listdir("images PDF"):
            if imagefile.startswith(filename[:-4]):
                os.rename("images PDF/" + imagefile, "images PDF/" + imagefile[:-3] + "jpg")

