import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from preprocess import load_dataset

def build_model(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def main():
    train_directory = '../data/train'
    normal_data, normal_labels, _ = load_dataset(os.path.join(train_directory, 'normal'))
    osteoporosis_data, osteoporosis_labels, _ = load_dataset(os.path.join(train_directory, 'osteoporosis'))
    
    # Verificación de que hay datos
    if len(normal_data) == 0 or len(osteoporosis_data) == 0:
        print("No se encontraron imágenes en las carpetas de entrenamiento.")
        return

    x_train = np.concatenate((normal_data, osteoporosis_data), axis=0)
    y_train = np.concatenate((normal_labels, osteoporosis_labels), axis=0)

    y_train = to_categorical(y_train)

    model = build_model((224, 224, 3), y_train.shape[1])
    model.fit(x_train, y_train, epochs=10, batch_size=32)

    if not os.path.exists('../models'):
        os.makedirs('../models')
    model.save('../models/osteoporosis_classifier.h5')
    print("Todos los modelos han sido entrenados y guardados exitosamente.")

if __name__ == "__main__":
    main()
    print("Entrenamiento completado exitosamente.")
