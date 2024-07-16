import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from preprocess import load_dataset

def evaluate_model():
    test_directory = '../data/test'
    normal_data, normal_labels, _ = load_dataset(os.path.join(test_directory, 'normal'))
    osteoporosis_data, osteoporosis_labels, _ = load_dataset(os.path.join(test_directory, 'osteoporosis'))

    x_test = np.concatenate((normal_data, osteoporosis_data), axis=0)
    y_test = np.concatenate((normal_labels, osteoporosis_labels), axis=0)

    y_test = to_categorical(y_test)

    model = load_model('../models/osteoporosis_classifier.h5')

    loss, accuracy = model.evaluate(x_test, y_test)
    print(f"Test Loss: {loss}")
    print(f"Test Accuracy: {accuracy}")

if __name__ == "__main__":
    evaluate_model()
