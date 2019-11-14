import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

import numpy as np
import pickle

#data = cnnDataLoader()
#X, y = data.loadData()


class cnnFireDetectionModel(object):
    def __init__(self):
        super().__init__()
        
    def runModel (self, X, y):
        X = X/ 255.0
        y = np.array(y)

        model = Sequential()

        model.add(Conv2D(256, (3, 3), input_shape= X.shape[1:]))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(256, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

        model.add(Dense(64))

        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

        model.fit(X, y, batch_size=32, epochs=15, validation_split=0.3)