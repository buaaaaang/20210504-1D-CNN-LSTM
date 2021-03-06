from keras.models import Sequential
from keras import layers
from keras import optimizers



def model():#hp):
    shape = (128000,1)
    unit = 128

    model = Sequential(name='1D')

    model.add(layers.Conv1D(filters=64,kernel_size=(3),strides=1,padding='same',input_shape = shape))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('elu'))
    
    model.add(layers.MaxPooling1D(pool_size=4, strides=4))

    model.add(layers.Conv1D(filters=64,kernel_size=(3),strides=1,padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('elu'))
    model.add(layers.MaxPooling1D(pool_size=4, strides=4))

    model.add(layers.Conv1D(filters=128,kernel_size=(3),strides=1,padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('elu'))
    model.add(layers.MaxPooling1D(pool_size=4, strides=4))

    model.add(layers.Conv1D(filters=128,kernel_size=(3),strides=1,padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('elu'))
    model.add(layers.MaxPooling1D(pool_size=4, strides=4))

    model.add(layers.LSTM(units=unit))

    model.add(layers.Dense(units=5,activation='softmax'))
    
    #opt = optimizers.Adam(lr=0.0001)
    opt = optimizers.SGD(lr = 0.0001, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(optimizer=opt,loss='categorical_crossentropy',metrics=['categorical_accuracy'])

    return model


if __name__ == "__main__":
    #hyperparamter tuning
    '''
    import kerastuner as kt
    import IPython
    import h5py
    import tensorflow as tf
    import numpy as np
    from numpy import newaxis
    file = "C:/Users/LG/Desktop/skt/KoreanSpeechDataForSER/1D.hdf5"
    hf = h5py.File(file,'r')
    
    x_tr = (hf['x'][:16000])[:,:,newaxis]
    x_v = (hf['x'][16000:20000])[:,:,newaxis]
    x_t = (hf['x'][20000:])[:,:,newaxis]

    Y = hf['y']
    y = np.zeros((Y.size,5))
    y[np.arange(Y.size),Y] = 1
    y_tr = y[:16000]
    y_v = y[16000:20000]
    y_t = y[20000:]
    
    tuner = kt.Hyperband(model,objective='val_categorical_accuracy',max_epochs=30,hyperband_iterations=2)
    tuner.search(x_tr,y_tr,epochs=30,validation_data=(x_v,y_v),
        callbacks=[tf.keras.callbacks.EarlyStopping(patience=1)])
    best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
    print(best_hps['lr'])
    print(best_hps['units'])
    '''
    
    
    
