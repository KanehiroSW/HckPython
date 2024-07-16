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

# Solicitar datos al usuario
t_score_paciente = float(input("Ingrese el T-score del paciente: "))
fracturas = input("¿Tiene el paciente fracturas por fragilidad? (s/n): ").strip().lower() == 's'

# Clasificar y mostrar el resultado
clasificacion = clasificar_osteoporosis(t_score_paciente, fracturas)
print(f"El paciente tiene: {clasificacion}")
