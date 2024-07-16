import os
from flask import Flask, request, jsonify, render_template_string
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

app = Flask(__name__)

model_path = 'models/osteoporosis_classifier.h5'

if os.path.exists(model_path):
    model = load_model(model_path)
    print("Modelo cargado exitosamente.")
else:
    raise FileNotFoundError(f"El archivo {model_path} no existe.")

# Crear la carpeta temp si no existe
if not os.path.exists('./temp'):
    os.makedirs('./temp')

def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB')  # Asegurarse de que la imagen tiene tres canales (RGB)
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data action="/predict">
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
    ''')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify(error='No file provided'), 400

    file = request.files['file']
    image_path = f'./temp/{file.filename}'
    file.save(image_path)

    image = preprocess_image(image_path)
    prediction = model.predict(image)
    os.remove(image_path)

    prediction_class = int(np.argmax(prediction))
    class_names = ["Normal", "Osteoporosis"]
    confidence = float(np.max(prediction)) * 100

    # Diagnóstico presuntivo basado en la predicción
    if prediction_class == 1:
        diagnosis = "Diagnóstico presuntivo: Posible enfermedad esquelética osteoporosis"
    else:
        diagnosis = "Diagnóstico presuntivo: Usted no tiene osteoporosis"

    response = {
        'diagnosis': diagnosis,
        'tipo_de_enfermedad': class_names[prediction_class],
        'confidence': f'{confidence:.2f}%',
        'imagen_subida': file.filename
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
