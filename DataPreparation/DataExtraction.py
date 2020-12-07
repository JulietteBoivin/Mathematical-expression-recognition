
from inkml2img import *
import xml.etree.ElementTree as ET
import os
from PIL import Image
from os import walk
from PIL import Image
from numpy import *
from os import walk

#Data path
Rep = '/content/drive/My Drive/Train/CROHME_training_inkml'
RepImg = '/content/drive/My Drive/Train/CROHME_training_img'
RepGT = '/content/drive/My Drive/Train/CROHME_training_txt'

#Load inkml training files
FilesList = []
for (repertoire, sousRepertoires, fichiers) in walk(Rep):
 FilesList.extend(fichiers)

#Get images from inkml training files
for filename in listeFichiers:
  inkml2img(Rep + '/' + filename, RepImg + '/' + filename.split('.')[0])
  
#Display one image 
image = RepImg + 'algb02.png'
im = Image.open(image)
display(im)

#Get text target from inkml files
for filename in listeFichiers:
  file = Rep + '/' + filename
  tree = ET.parse(file)
  root = tree.getroot()
  for child in root: 
    if 'truth' in child.attrib.values():
      os.chdir(RepGT)
      with open(filename.split('.')[0] + '.txt', 'a') as fichier:
        fichier.write(child.text)
        fichier.close()


