import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def predict_image(image_path):
    model = load_model('../models/osteoporosis_classifier.h5')

    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction, axis=1)[0]

    if class_idx == 0:
        print(f"La imagen {image_path} es de un hueso normal.")
    else:
        print(f"La imagen {image_path} es de un hueso con osteoporosis.")

if __name__ == "__main__":
    image_path = '../data/single_prediction/sample.jpg'  # Cambia esta ruta a la imagen que deseas predecir
    predict_image(image_path)
