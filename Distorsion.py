import cv2 
import numpy as np
from PIL import Image
 
def global_distortion(img, imagepath, k, γ):

    A=img[:,:,0]
    (m,n) = np.shape(A)
    
    #k percent of original size
    width = int(m * k)
    height = int(n * k)
    
    dim = (width, height)
    
    image = Image.open(imagepath)
    resized = image.resize((width, height))
    new_resized=(np.array(resized))[:,:,0]

    # returning to the image's initial dimensions 
    (r,s)=(m-width,n-height) #width=89,height=89
    result=np.full((m,n),255,dtype='uint8')
    cx=m//2
    cy=n//2
    result[cx-width//2:cx+width//2+1,cy-height//2:cy+height//2+1]=new_resized
    
    #image rotation 

    # grab the dimensions of the image and then determine the
    # center
    (h, w) = result.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -γ, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    rotated= cv2.warpAffine(result, M, (m, n))
    
    return rotated
    

#Function to remove borders of the old image and expand dimension of our image
def bordexp(img):
  
  #removing borders by making them white 
    for j in range(128):
      for i in range(20):
        img[i,j]=255
    for i in range(128):
      for j in range(15):
        img[i,j]=255
        
  #adding a third dimension to have (128,128,4)
    (m,n)=np.shape(img)
    new_im=np.zeros((m,n,4))
    for i in range(m):
      for j in range(n):
        for k in range(4):
          new_im[i,j]=4*[img[i,j]]

    return new_im
    
    
#Function to generate a distorted dataset 
def distorted_dataset(data ,listofnames ,labels ):
     
    distorted=[] #list to keep distorted data 
    names=[ ]    #list of names of distorted data
    y= [ ]  #list of labels
    for i in range(len(data)):
        t=global_distortion(data[i],listofnames[i],0.7,-5) #distort=resize+rotate
        new_t=bordexp(t)                                   #remove borders and return in 3 dimensions
        distorted.append(new_t)
        names.append(listofnames[i])
        y.append(labels[i])
    
    return distorted, names,y
