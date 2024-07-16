import tensorflow as tf

# Verificar si hay GPU disponible
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    print(f"GPUs disponibles: {physical_devices}")
    try:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        print("Configuración de GPU exitosa.")
    except RuntimeError as e:
        print(e)
else:
    print("No se encontró ninguna GPU. Usando la CPU.")
