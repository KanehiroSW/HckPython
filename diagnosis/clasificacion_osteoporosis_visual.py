import matplotlib.pyplot as plt

# Definir los rangos y las categorías de T-score
categorias = ['Normal', 'Osteopenia', 'Osteoporosis', 'Osteoporosis Severa']
rangos = [(-1, 1), (-2.5, -1), (-3.5, -2.5), (-4.5, -3.5)]
colores = ['green', 'yellow', 'orange', 'red']

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(12, 6))

# Añadir barras para cada categoría con su rango específico
for categoria, (inicio, fin), color in zip(categorias, rangos, colores):
    ax.barh(categoria, fin - inicio, left=inicio, color=color, edgecolor='black')

# Etiquetas y título
ax.set_xlabel('T-score')
ax.set_title('Clasificación de Osteoporosis basada en T-score')
ax.set_xlim([-5, 2])
ax.set_xticks(range(-5, 3))
ax.set_xticklabels(range(-5, 3))

# Añadir líneas verticales para los límites entre categorías
plt.axvline(x=-1, color='blue', linestyle='--', label='Límite Normal/Osteopenia')
plt.axvline(x=-2.5, color='purple', linestyle='--', label='Límite Osteopenia/Osteoporosis')

# Añadir leyenda
ax.legend()

# Mostrar la gráfica
plt.show()
