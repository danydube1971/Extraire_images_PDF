# Extraire_images_PDF
Extraction des images contenus dans le ou les PDF du dossier actuel au format JPG

Le script parcourt tous les fichiers dans le dossier actuel ayant l'extension ".pdf" et utilise la commande système "pdfimages" 
pour extraire toutes les images de chaque fichier PDF. Les images extraites sont stockées dans un dossier nommé "images PDF" créé 
dans le dossier actuel. Enfin, toutes les images extraites sont renommées pour qu'elles soient au format .jpg.

**Comment utiliser le script**

1.Placer le script *Extraction_images_PDF.py* dans le même dossier que les fichiers PDF.

2.Ouvrir un terminal et exécuter la commande **python3 "Extraction_images_PDF.py"**.

Testé sous Linux Mint 21
