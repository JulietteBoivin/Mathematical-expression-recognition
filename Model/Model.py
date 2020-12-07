import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten,LSTM, Lambda, Attention, TimeDistributed
from keras.layers import Conv2D, MaxPooling2D, Conv2DTranspose, BatchNormalization
from AttentionLayer import attention

def OurModel():
  model = Sequential()

  model.add(Conv2D(64, kernel_size=(3, 3),activation='relu',input_shape=(128,128, 4)))
  model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, input_shape = (126,126,64)))
  model.add(MaxPooling2D(pool_size=(2, 2), input_shape = (126, 126, 64)))

  model.add(Conv2D(128, kernel_size=(3, 3),activation='relu', input_shape = (63, 63, 64)))
  model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, input_shape = (61, 61, 128)))
  model.add(MaxPooling2D(pool_size=(2, 2), input_shape=(61, 61, 128)))

  model.add(Conv2D(256, kernel_size=(3, 3),activation='relu', input_shape = (30, 30, 128)))
  model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, input_shape = (28, 28, 256)))
  model.add(MaxPooling2D(pool_size=(2, 2), input_shape = (28, 28, 256)))

  model.add(Conv2D(512, kernel_size=(2, 2),activation='relu', input_shape = (14, 14, 256)))   
  model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, input_shape = (13, 13, 512)))
  model.add(MaxPooling2D(pool_size=(1, 1), input_shape = (13, 13, 512)))

  model.add(Conv2D(1024, kernel_size=(2, 2), activation='relu', input_shape = (13, 13, 512)))
  model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, input_shape = (12, 12, 1024)))

  model.add(Conv2DTranspose(filters = 1, kernel_size = (2,2), input_shape = (12, 12, 1024)))

  model.add(Flatten())

  model.add(keras.layers.Reshape((13, 13)))
  model.add(Bidirectional(LSTM(637, return_sequences=True), input_shape = (13, 13)))
  model.add(attention(return_sequences=True)) # receive 3D and output 3D

  model.add(keras.layers.Reshape((49, 338)))

  model.add(TimeDistributed(Dense(73, activation='softmax')))

  model.summary()

  model.compile(loss='SparseCategoricalCrossentropy', optimizer='adam', metrics=['accuracy'])
  
  return model
 
