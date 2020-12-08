# Mathematical-expression-recognition

1.Training an End-to-End System for Handwritten Mathematical Expressions

In this project we tried to reproduce the model proposed by Anh Duc Le and Masaki Nakagawa, Department of Computer Information Tokyo University of Agriculture and Technology in their article “Training an End-to-End System for Handwritten Mathematical Expressions”.

The authors of this article propose an end to end system for recognition of such expressions. Starting from INKML files, we wanted to predict the associated LaTex formulas. In order to do so we constructed an architecture based on a Convolutional Neural Network, bidirectional LSTM and Attention based encoder decoder model. Starting from the CROHME dataset, we used CROHME 2011 to train our model and CROHME 2012 to test. 

2.Requirements

Keras
Python 
XML notions

This project was developed during our first semester of Master of Data Science and Engineering for the course of “Deep learning”. 
Basic understanding of XML is required since the original data is in INKML form. 
Knowledge of Python and Keras libraries is required. 

3.Contents

Data preparation
Model 
Distortion
Contributions 

3.a. Data preparation

3.a.1. DataFormatting.py

Contains a function developed by us to recuperate the data as lists, as well as their names and labels. It returns the data partitioned for training, validating and testing. 

3.a.2. GTVectorization.py

Contains functions developed by us in order to split the label data into their sub-elements. It also includes functions responsible for padding, encoding and embedding. Vectorization is based on the element’s position in the grammar 
(ex. Letter a is represented by 0 since it’s the first element of the grammar).

3.a.3. inkml2img.py

The data being in INKML format, must be transformed to images in order to be fed to the CNN network. This file contains all the necessary functions to transform and save an INKML file as an .png image. 

3.b. Model 

3.b.1 AttentionLayer.py 

Class implementing an attention encoder decoder model for the LSTM to use in the main model. 

3.b.2 Model.py 

Model implemented by us using Keras in order to mimic the proposed architecure of the article read. 

3.c Distortion

3.c.1 Distortion.py

File containing the functions responsible for global distortion, border removal and distorted dataset preparation. The functions have been implemented by us and with the use of cv2 library. 

3.d.Contributions 

- https://learnandshare645.blogspot.com/2016/06/feeding-your-own-data-set-into-cnn.html
 
- https://github.com/ducanh841988/Handwritten-Math-Recognition
(Original Authors, model implemented in Lua programming language. )

- We also read a plethora of articles and blogs, most of them being from Medium, Towards Data Science and Keras forums and documentation.

