from PIL import Image
import pytesseract
import re

def clasificar_osteoporosis(t_score, fracturas_fragilidad=False):
    if t_score >= -1:
        return "Normal"
    elif -2.5 < t_score < -1:
        return "Osteopenia"
    elif t_score <= -2.5:
        if fracturas_fragilidad:
            return "Osteoporosis severa"
        else:
            return "Osteoporosis"
    else:
        return "Clasificación no definida"

# Configura la ruta al ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Cargar la imagen
imagen_path = 'eva/1 (2).JPEG'  # Reemplaza con la ruta a tu imagen
imagen = Image.open(imagen_path)

# Usar pytesseract para extraer el texto de la imagen
texto_extraido = pytesseract.image_to_string(imagen)

# Buscar y extraer el valor del T-score del texto extraído
patron_t_score = re.compile(r'T-score\s*=\s*(-?\d+\.\d+)')
coincidencias = patron_t_score.search(texto_extraido)

if coincidencias:
    t_score_paciente = float(coincidencias.group(1))
    fracturas = False  # Supongamos que no tenemos información sobre fracturas en este ejemplo

    # Clasificar y mostrar el resultado
    clasificacion = clasificar_osteoporosis(t_score_paciente, fracturas)
    print(f"El paciente tiene: {clasificacion}")
else:
    print("No se encontró un T-score en la imagen.")
