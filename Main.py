from DataFormatting import GetDataLists
from GTVectorization import padding
from Model.Model import OurModel


[(X_train, y_train), (X_valid, y_valid), (X_test, y_test)] = GetDataLists()

model = OurModel()

grammar_file_name = '/content/drive/My Drive/listSymbolsPart2.txt'
grammar=[]
with open(grammar_file_name, 'r') as gram:
    grammar = gram.read().splitlines() 
    
full_grammar=list(np.copy(list(grammar)))
full_grammar.append('{')
full_grammar.append('}')
full_grammar.append('')
full_grammar.append('_')
full_grammar.append('\\frac')
full_grammar = [' '] + full_grammar

#Checkpoints
cpath = "/content/drive/My Drive/Deep/Checkpoints/epochs:{epoch:03d}.hdf5"
cp = ModelCheckpoint(cpath, verbose=1, save_best_only=True)
callback_list = [cp]

#Model fitting
hist = model.fit(np.array(X_train),np.array(padding(y_train,49)),
                 batch_size=batch_size, epochs=epochs, verbose=1,
                 validation_data=(np.array(X_valid),np.array(padding(y_valid,49))),
                 callbacks=callback_list)
                 
#Plot train loss and validation loss
loss_train = hist.history['loss']
loss_valid = hist.history['val_loss']
plt.plot(loss_train,"b:o", label = "loss_train")
plt.plot(loss_valid,"r:o", label = "loss_valid")
plt.title("Loss over training epochs")
plt.legend()
plt.savefig('loss_training_model.png')
plt.close()
