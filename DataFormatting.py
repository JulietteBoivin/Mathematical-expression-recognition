from os import walk
import matplotlib.image as mpimg
 
repImgTrain = '/content/drive/My Drive/Train/ORNELA_train_img_resized'
repImgValid = '/content/drive/My Drive/Train/valid_img_resized'
repImgTest = '/content/drive/My Drive/Test/ORNELA_test_img_resized'

def ListOfImg(rep):
  listf = []    #list of training  files 
  for (repertoire, sousRepertoires, fichiers) in walk(rep):
    listf.extend(fichiers)

  ImgNames = []  #obtaining the list of the file names for training
  for i in range (len(listf)):
    ImgNames.append(rep + '/' + listf[i])

  ImgList = []  # saving each file in the form of an image 
  for i in range (len(ImgNames)):
    ImgList.append(mpimg.imread(ImgNames[i])) 
    
  return ImgList
  
X_train = ListOfImg(repImgTrain)
X_valid = ListOfImg(repImgValid)
X_test = ListOfImg(repImgTest)

  
repTxtTrain = '/content/drive/My Drive/Train/train_txt'
repTxtValid = '/content/drive/My Drive/Train/valid_txt'
repTxtTest = '/content/drive/My Drive/Test/CROHME_test_txt'

def ListOfTxt(rep):
  list = []  
  for (repertoire, sousRepertoires, fichiers) in walk(rep):
    listy.extend(fichiers)

  TxtNames = [] #obtaining the list of the file names' labels for training
  for i in range (len(list)):
    TxtNames.append(rep + '/' + list[i])

  TxtList = []  # saving each file in the form of a txt/latex label 
  for i in range (len(TxtNames)):
    filename = TxtNames[i]
    with open(filename, 'r') as fichier:
      t = fichier.readline()
      t = t[:-1]
      TxtList.append(t)
      
   return TxtList
   
y_train = ListOfTxt(repTxtTrain)
y_valid = ListOfTxt(repTxtValid)
y_test = ListOfTxt(repTxtTest) 
   
   
def RemoveBlankElements(X, y):
  i = 0
  while i <(len(y)):
    if y[i] == '':
      del y[i]
      del X[i]
    else:
      i += 1
      
RemoveBlankElements(X_train, y_train)
RemoveBlankElements(X_valid, y_valid)
RemoveBlankElements(X_test, y_test)
   
def GetDataLists():
  return [(X_train, y_train), (X_valid, y_valid), (X_test, y_test)]
   
   
   
   
   
      
