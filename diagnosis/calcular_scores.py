import matplotlib.pyplot as plt
import numpy as np

# Función para calcular el T-score
def calcular_t_score(dmo_paciente, dmo_promedio_joven, desviacion_estandar_joven):
    t_score = (dmo_paciente - dmo_promedio_joven) / desviacion_estandar_joven
    return t_score

# Función para calcular el Z-score
def calcular_z_score(dmo_paciente, dmo_promedio_edad, desviacion_estandar_edad):
    z_score = (dmo_paciente - dmo_promedio_edad) / desviacion_estandar_edad
    return z_score

# Función para clasificar la osteoporosis basada en el T-score
def clasificar_osteoporosis(t_score):
    if t_score >= -1:
        return "Normal"
    elif -2.5 < t_score < -1:
        return "Osteopenia"
    elif t_score <= -2.5:
        return "Osteoporosis"
    else:
        return "Clasificación no definida"

# Solicitar datos al usuario
edad = int(input("Ingrese la edad del paciente: "))
dmo_paciente = float(input("Ingrese la DMO del paciente (g/cm^2): "))
dmo_promedio_joven = 1.2  # Valor promedio para población joven
desviacion_estandar_joven = 0.1  # Desviación estándar para población joven
dmo_promedio_edad = float(input("Ingrese la DMO promedio de la población de la misma edad (g/cm^2): "))
desviacion_estandar_edad = float(input("Ingrese la desviación estándar de la DMO para la población de la misma edad (g/cm^2): "))

# Calcular T-score y Z-score
t_score = calcular_t_score(dmo_paciente, dmo_promedio_joven, desviacion_estandar_joven)
z_score = calcular_z_score(dmo_paciente, dmo_promedio_edad, desviacion_estandar_edad)

# Clasificar la osteoporosis
clasificacion = clasificar_osteoporosis(t_score)

# Mostrar los resultados al usuario
print(f"\nResultados:")
print(f"T-score: {t_score:.2f}")
print(f"Z-score: {z_score:.2f}")
print(f"Clasificación de Osteoporosis: {clasificacion}")

# Visualizar los resultados
edades = np.arange(20, 81, 10)  # Edades de 20 a 80 años
dmo_pacientes = [dmo_paciente] * len(edades)
t_scores = [(dmo - dmo_promedio_joven) / desviacion_estandar_joven for dmo in dmo_pacientes]
z_scores = [(dmo - dmo_promedio) / desviacion_estandar_edad for dmo, dmo_promedio in zip(dmo_pacientes, [dmo_promedio_edad] * len(edades))]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(edades, t_scores, label='T-score', marker='o')
plt.plot(edades, z_scores, label='Z-score', marker='s')
plt.axhline(y=-2.5, color='r', linestyle='--', label='Umbral Osteoporosis')
plt.axhline(y=-1, color='orange', linestyle='--', label='Umbral Osteopenia')
plt.xlabel('Edad')
plt.ylabel('Score')
plt.title('T-score y Z-score en Diferentes Edades')
plt.legend()
plt.grid(True)
plt.show()
