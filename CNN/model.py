import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from keras.layers.advanced_activations import LeakyReLU
import numpy as np
import sys

import pickle


if __name__ == '__main__':

    X_Training = pickle.load(open("X_Training.pickle", 'rb'))
    y_Training = pickle.load(open("y_Training.pickle", 'rb'))

    # y_Test = pickle.load(open("y_Test.pickle", 'rb'))
    # X_Test = pickle.load(open("X_Test.pickle", 'rb'))
    
    y_Test = pickle.load(open("y_Test2.pickle", 'rb'))
    X_Test = pickle.load(open("X_Test2.pickle", 'rb'))


    y_Training = np.array(y_Training)
    X_Training = X_Training/255.0

    y_Test = np.array(y_Test)
    X_Test = X_Test / 255.0

    unos = ''
    while (True):
        print('\n')
        print("MENI: (nas test), test sa canvasa")
        print("1. VGG accuracy: (79%) 59%")
        print("2. Model2 accuracy: (88%) 65%")
        print("3. Model3 accuracy: (91%) 65%")
        print('X  ZA IZLAZ')
        unos = input(">> ")

        if (unos == '1'):

            # model = Sequential()
            # model.add(Conv2D(32, (3, 3), strides=1, padding="same", activation="relu", input_shape=(64, 64, 1)))
            # model.add(Dropout(0.4))
            # model.add(Conv2D(32, (3, 3), strides=1, padding="same", activation="relu"))
            # model.add(Dropout(0.4))
            # model.add(MaxPooling2D((2, 2)))
            #
            # model.add(Conv2D(64, (3, 3), strides=1, padding="same", activation="relu"))
            # model.add(Dropout(0.4))
            # model.add(Conv2D(64, (3, 3), strides=1, padding="same", activation="relu"))
            # model.add(Dropout(0.4))
            # model.add(MaxPooling2D((2, 2)))
            #
            # model.add(Conv2D(128, (3, 3), strides=1, padding="same", activation="relu"))
            # model.add(Dropout(0.4))
            # model.add(Conv2D(128, (3, 3), strides=1, padding="same", activation="relu"))
            # model.add(Dropout(0.4))
            # model.add(MaxPooling2D((2, 2)))
            #
            # model.add(Flatten())
            #
            # model.add(Dense(3, activation="softmax"))
            #
            # model.compile(loss='sparse_categorical_crossentropy',
            #               optimizer='adam',
            #               metrics=['accuracy'])
            #
            # model.fit(X_Training, y_Training, batch_size=64, epochs=20, validation_split=0.3)
            # model.save("model_vgg")

            model = tf.keras.models.load_model("model_vgg")
            test_eval = model.evaluate(X_Test, y_Test, verbose=1, batch_size=16)

            print("Test loss: " + str(test_eval[0]))
            print("Test accuracy " + str(test_eval[1]))
            
        elif (unos == '2'):

            # model = Sequential()
            #
            # model.add(Conv2D(128, (3, 3), padding='same', activation='linear', input_shape=X_Training.shape[1:]))
            # model.add(LeakyReLU(alpha=0.1))
            # model.add(MaxPooling2D(pool_size=(2, 2)))
            # model.add(Dropout(0.1))
            #
            # model.add(Conv2D(128, (3, 3), padding='same', activation='linear'))
            # model.add(LeakyReLU(alpha=0.1))
            # model.add(MaxPooling2D(pool_size=(2, 2)))
            # model.add(Dropout(0.2))
            #
            # model.add(Conv2D(128, (3, 3), padding='same', activation='linear'))
            # model.add(LeakyReLU(alpha=0.1))
            # model.add(MaxPooling2D(pool_size=(2, 2)))
            # model.add(Dropout(0.3))
            #
            # model.add(Conv2D(128, (3, 3), activation='linear', padding='same'))
            # model.add(LeakyReLU(alpha=0.1))
            # model.add(MaxPooling2D((2, 2), padding='same'))
            # model.add(Dropout(0.4))
            #
            # model.add(Flatten())
            #
            # model.add(Dense(3, activation="softmax"))
            #
            # model.compile(loss='sparse_categorical_crossentropy',
            #               optimizer='adam',
            #               metrics=['accuracy'])
            #
            # model.fit(X_Training, y_Training, batch_size=16, epochs=20, validation_split=0.3)
            # model.save("model88")

            model = tf.keras.models.load_model("model88")
            test_eval = model.evaluate(X_Test, y_Test, verbose=1, batch_size=16)

            print("Test loss: " + str(test_eval[0]))
            print("Test accuracy " + str(test_eval[1]))
            
        elif (unos == '3' ):
            # model = Sequential()
            #
            # model.add(Conv2D(256, (3, 3), input_shape=X_Training.shape[1:]))
            # model.add(LeakyReLU(alpha=0.1))
            # model.add(MaxPooling2D(pool_size=(2, 2)))
            # model.add(Dropout(0.1))
            #
            # model.add(Conv2D(128, (3, 3)))
            # model.add(LeakyReLU(alpha=0.1))
            # model.add(MaxPooling2D(pool_size=(2, 2)))
            # model.add(Dropout(0.2))
            #
            # model.add(Conv2D(64, (3, 3)))
            # model.add(LeakyReLU(alpha=0.1))
            # model.add(MaxPooling2D(pool_size=(2, 2)))
            # model.add(Dropout(0.3))
            #
            # model.add(Conv2D(32, (3, 3)))
            # model.add(LeakyReLU(alpha=0.1))
            # model.add(MaxPooling2D((2, 2), padding='same'))
            # model.add(Dropout(0.4))
            #
            # model.add(Flatten())
            #
            # model.add(Dense(3, activation="softmax"))
            #
            # model.compile(loss='sparse_categorical_crossentropy',
            #               optimizer='adam',
            #               metrics=['accuracy'])
            #
            # model.fit(X_Training, y_Training, batch_size=16, epochs=40, validation_split=0.3)
            # model.save("model3")

            model = tf.keras.models.load_model("model91")
            test_eval = model.evaluate(X_Test, y_Test, verbose=1, batch_size=16)

            print("Test loss: " + str(test_eval[0]))
            print("Test accuracy " + str(test_eval[1]))


        elif (unos == 'x' or unos == 'X'):
            print("Dovidjenja")
            sys.exit()

        else:
            print("Neispravan unos")


