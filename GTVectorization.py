import re


def formatting(mystring):

  def mysplit(mystr):
    return re.split("([+-/*{}_= ()])", mystr.replace(" ", ""))

  #split on spaces
  string_space = mystring.split(' ')
  
  #split on ([+-/*{}_= ()])
  string_charac = []
  for i in range(len(string_space)):
    string_charac.append(mysplit(string_space[i]))

  new_string = []
  for i in string_charac:
    new_string = new_string + i
  
  #Remove '' in the new_string list
  new_string = [i for i in new_string if i != ''] 

  return new_string
  
  
  def encode_words_labels(splitted_list, grammar):
    #Encodes the Ground Truth Labels to a list of Values
    label_lst=[]
    
    for i in range(len(splitted_list)):
      
      if splitted_list[i] not in grammar:
         grammar.append(splitted_list[i])
          
      label_lst.append(grammar.index(splitted_list[i])) # keeping 0 for blank and for padding labels
      
    return label_lst
    
    
def embedding(Y, grammar): 
  Y_encd= [] # list to keep track of encoded data 
  max_length=0              #variable to keep track of max length 
  for i in range(len(Y)):
    
    Y_format=formatting(Y[i])  #format the data via character splitting 
    Y_e=encode_words_labels(Y_format, grammar) #encode the data 
    if len(Y_e)> max_length:   #comparing lengths, to use the max for padding 
      max_length=len(Y_e)

    Y_encd.append(Y_e) #adding encoded y to the list 
  return Y_encd, max_length
    
  
def padding(Y,padding_length, grammar):
  
    y_encoded,max_length = embedding(Y, grammar) #recuperating encoded data and max length 
    
    Y_padded=[] # list of padded and encoded data 
    for i in range(len(y_encoded)):
        if len(y_encoded[i])< padding_length:
            m=len(y_encoded[i])
            y_encoded[i].extend([0]* (padding_length - m)) # adding zeros if the length is smaller than the max_length found
        Y_padded.append(y_encoded[i])
     
    return Y_padded
    
    
    
    
    
    
    
    
