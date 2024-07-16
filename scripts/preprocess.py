import os
import numpy as np
from PIL import Image

def load_dataset(directory):
    data = []
    labels = []
    label = os.path.basename(directory)
    label_idx = 0 if label == 'normal' else 1
    
    if not os.path.isdir(directory):
        print(f"La carpeta {directory} no existe o no es un directorio.")
        return np.array(data), np.array(labels), {}
    
    for file in os.listdir(directory):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            file_path = os.path.join(directory, file)
            try:
                image = Image.open(file_path).resize((224, 224))
                image = np.array(image) / 255.0
                if image.shape == (224, 224, 3):  # Only accept images with correct shape
                    data.append(image)
                    labels.append(label_idx)
            except Exception as e:
                print(f"Error procesando el archivo {file_path}: {e}")
    
    data = np.array(data)
    labels = np.array(labels)
    return data, labels, {label: label_idx}

if __name__ == "__main__":
    # Verificación rápida
    train_directory = '../data/train'
    normal_data, normal_labels, _ = load_dataset(os.path.join(train_directory, 'normal'))
    osteoporosis_data, osteoporosis_labels, _ = load_dataset(os.path.join(train_directory, 'osteoporosis'))

    print(f"Normal samples: {len(normal_data)}")
    print(f"Osteoporosis samples: {len(osteoporosis_data)}")
