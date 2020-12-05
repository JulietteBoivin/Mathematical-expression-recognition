import re


def formatting(mystring):

  def mysplit(mystr):
    return re.split("([+-/*{}_= ()])", mystr.replace(" ", ""))

  #split on spaces
  b = mystring.split(' ')

  B = []
  for i in range(len(b)):
    B.append(mysplit(b[i]))

  BB = []
  for i in B:
    BB = BB + i

  BB = [i for i in BB if i != ''] 

  return BB
  
  
  def encode_words_labels(l):
    """
    Encodes the Ground Truth Labels to a list of Values like eg.HAT returns [17,10,29]
    """
    label_lst=[]
    for i in range(len(l)):
      #print(l[i]) 
      #print(char)
      if l[i] not in full_grammar:
         
         full_grammar.append(l[i])
      label_lst.append(full_grammar.index(l[i])) # keeping 0 for blank and for padding labels
    return label_lst
    
    
def embedding(Y_train): 
  Y_train_encd= [] # list to keep track of encoded data 
  z=0              #variable to keep track of max length 
  for i in range(len(Y_train)):
    
    yy=formatting(Y_train[i])  #format the data via character splitting 
    ye=encode_words_labels(yy) #encode the data 
    if len(ye)> z:   #comparing lengths, to use the max for padding 
      z=len(ye)

    Y_train_encd.append(ye) #adding encoded y to the list 
  return Y_train_encd,z
    
def padding(Y,z):
    y_encoded,max_length=embedding(Y) #recuperating encoded data and max length 
    
    YYe=[] # list of padded and encoded data 

    for i in range(len(y_encoded)):
        if len(y_encoded[i])< z:
            m=len(y_encoded[i])
            y_encoded[i].extend([0]* (z-m)) # adding zeros if the length is smaller than the max_length found
        YYe.append(y_encoded[i])
     
    return YYe 
    
    
    
    
    
    
    
    
