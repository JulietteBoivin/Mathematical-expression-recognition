from PIL import Image
import os
import numpy as np

pathTrain =  '/content/drive/My Drive/Train/train_img'
pathTrainR =  '/content/drive/My Drive/Train/ORNELA_train_img_resized'

pathV = '/content/drive/My Drive/Train/valid_img'
pathVR =  '/content/drive/My Drive/Train/valid_img_resized'

pathTest = '/content/drive/My Drive/Test/CROHME_test_img'
pathTestR =  '/content/drive/My Drive/Test/test_img_resized'

#Resizing train images
listingTrain = os.listdir(pathTrain)
num_samples_Train =np.size(listingTrain)

for file in listingTrain:
    imTrain = Image.open(pathTrain + '/' + file)  
    imgTrain = imTrain.resize((128,128))     
    imgTrain.save(pathTrainR +'/' +  file, 'png')



#Resizing validation images
listingValid = os.listdir(pathV)
num_samples_Valid =np.size(listingValid)

for file in listingValid:
    imValid = Image.open(pathV + '/' + file)  
    imgValid = imValid.resize((128,128))     
    imgValid.save(pathVR +'/' +  file, 'png')



 #Resizing test images
listingTest = os.listdir(pathTest)
num_samples_Test =np.size(listingTest)

for file in listingTest:
    imTest = Image.open(pathTest + '/' + file)  
    imgTest = imTest.resize((128,128))     
    imgTest.save(pathTestR +'/' +  file, 'png')
    
    
    
    
    
