import numpy as np
from cv2 import cv2
import os
import random
import pickle


def create_training_data(DATA_DIR):
    training_data = []
    for category in CATEGORIES:
        path = os.path.join(DATA_DIR, category)
        class_num = CATEGORIES.index(category)

        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            training_data.append([new_array, class_num])


    return training_data


if __name__ == '__main__':
    DATA_DIR_TEST = "Dataset/Test"
    DATA_DIR_TRAINING = "Dataset/Training"

    CATEGORIES = ["Normal", "Virus", "Bacteria"]
    IMG_SIZE = 64

    trainig_data = create_training_data(DATA_DIR_TRAINING)
    test_data = create_training_data(DATA_DIR_TEST)

    random.shuffle(trainig_data)
    random.shuffle(test_data)


    X_Training = []
    y_Training = []

    for features, label in trainig_data:
        X_Training.append(features)
        y_Training.append(label)

    X_Training = np.array(X_Training).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    picke_out = open("X_Training.pickle", "wb")
    pickle.dump(X_Training, picke_out)
    picke_out.close()

    picke_out = open("y_Training.pickle", "wb")
    pickle.dump(y_Training, picke_out)
    picke_out.close()

    X_Test = []
    y_Test = []

    for features, label in test_data:
        X_Test.append(features)
        y_Test.append(label)

    X_Test = np.array(X_Test).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    picke_out = open("X_Test.pickle", "wb")
    pickle.dump(X_Test, picke_out)
    picke_out.close()

    picke_out = open("y_Test.pickle", "wb")
    pickle.dump(y_Test, picke_out)
    picke_out.close()







