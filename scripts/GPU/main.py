import os
import tensorflow as tf

# Desactivar las advertencias de oneDNN
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Verificar si hay GPU disponible
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    try:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        print(f"Usando GPU: {physical_devices[0]}")
    except RuntimeError as e:
        print(e)
else:
    print("No se encontró ninguna GPU. Usando la CPU.")

from scripts.train_models import train_model
from scripts.evaluate import evaluate_image

def main():
    # Entrenar el modelo
    train_model()

    # Evaluar una imagen de prueba
    test_image_path = 'data/test/osteoporosis/example.jpg'
    if os.path.exists(test_image_path):
        score = evaluate_image(test_image_path)
        print(f'Diagnóstico presuntivo: {"Osteoporosis" if score > 0.5 else "Normal"} con una confianza de {score:.2f}')
    else:
        print(f'La imagen de prueba no se encuentra en la ruta: {test_image_path}')

if __name__ == "__main__":
    main()
