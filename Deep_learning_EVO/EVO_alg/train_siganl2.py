from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import regularizers
import numpy as np

from DnnFunctions import asimovSignificanceLossInvert, significanceLossInvert, significanceLoss

# Helper: Early stopping.

early_stopper = EarlyStopping(patience=3)

class get_data:
    def __init__(self,train_data_path:str=None,test_data_path:str=None,\
                lumi:float=100.,sig_xs:float=None,bg_xs:list=[None],systematic:float=None):
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path
        self.lumi = lumi
        self.sig_xs = sig_xs
        self.bg_xs = bg_xs
        self.systematic = systematic
        
        
    def get_np_data(self):
        with np.load(self.train_data_path) as f:
            X_train, y_train = f['x'], f['y']    

        with np.load(self.test_data_path) as f:
            X_test, y_test = f['x'], f['y']    
        
        nb_classes = len(np.bincount(y_train))
        batch_size = 4096*8
        input_shape = (X_train.shape[1],)
        
        if nb_classes > 2:
            y_test = to_categorical(y_test)
            y_train = to_categorical(y_train)
    
        return (nb_classes, batch_size, input_shape, X_train, X_test, y_train, y_test)



def compile_model(network, nb_classes, input_shape, expectedSignal, expectedBkgd, systematic, loss_func, is_asimov):
    """Compile a sequential model.
    Args:
        network (dict): the parameters of the network
    Returns:
        a compiled network.
    """
    # Get our network parameters.
    nb_layers = network['nb_layers']
    nb_neurons = network['nb_neurons']
    activation = network['activation']
    optimizer = network['optimizer']
    initializer = network['initializer']
    alpha = network['alpha']
    model = Sequential()

    # Add each layer.
    for i in range(nb_layers):

        # Need input shape for first layer.
        if i == 0:
            model.add(Dense(nb_neurons, activation=activation, kernel_initializer=initializer, kernel_regularizer=regularizers.l2(alpha), input_shape=input_shape))
        else:
            model.add(Dense(nb_neurons, kernel_initializer=initializer, kernel_regularizer=regularizers.l2(alpha), activation=activation))

        #model.add(Dropout(0.2))  # hard-coded dropout

    # Output layer.
    if nb_classes > 2:
        model.add(Dense(nb_classes, activation='sigmoid'))

        if is_asimov:
            model.compile(loss=loss_func, optimizer=optimizer,
                          metrics=[asimovSignificanceLossInvert(expectedSignal,expectedBkgd,systematic)])
        else:
            model.compile(loss=loss_func, optimizer=optimizer,
                          metrics=['accuracy'])
    else:
        model.add(Dense(1, activation='sigmoid'))

    return model


def train_and_score(network, dataset):
    """Train the model, return test loss.
    Args:
        network (dict): the parameters of the network
        dataset (str): Dataset to use for training/evaluating
    """
    
    nb_classes, batch_size, input_shape, x_train, \
    x_test, y_train, y_test = dataset.get_np_data()
    
    expectedSignal = dataset.lumi * dataset.sig_xs
    expectedBkgd = [i*dataset.lumi for i in dataset.bg_xs]
    systematic = dataset.systematic
    
    '''
    model = compile_model(network, nb_classes, input_shape, expectedSignal, expectedBkgd, systematic,'binary_crossentropy',is_asimov=False)
    #pre training
    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=50,  
              verbose=0,
              validation_data=(x_test, y_test),
              callbacks=[early_stopper])
    '''
    
    #To run asimov mode. Uncomment the code bellow
    model = compile_model(network, nb_classes, input_shape, expectedSignal, expectedBkgd, systematic,\
                          asimovSignificanceLossInvert(expectedSignal,expectedBkgd,systematic),is_asimov=True)
    
    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=50,  
              verbose=0,
              validation_data=(x_test, y_test),
              callbacks=[early_stopper])
      
    score = model.evaluate(x_test, y_test, verbose=0)
    
    with open("/home/joao/Desktop/Artigos/BGL_project2p0/EVO_alg/models/ah2/NN_asimov_{:.10f}.json".format(score[1]), "w") as json_file:
        json_file.write(model.to_json())

    model.save_weights("/home/joao/Desktop/Artigos/BGL_project2p0/EVO_alg/weights/weights_asimov_{:.10f}.hdf5".format(score[1]))
    return score[1] 
    
    '''
    score = model.evaluate(x_test, y_test, verbose=0)
    
    with open("./models/Q6-1/NN_Q6_Accuracy_{:.4f}.json".format(score[1]), "w") as json_file:
        json_file.write(model.to_json())

    model.save_weights("./weights/Q6-1/weights_Q6_Accuracy_{:.4f}.hdf5".format(score[1]))
    return score[1] 
    '''
