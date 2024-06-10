class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

# Crear instancia de la clase
clima_semanal = ClimaDiario()

# Ingresar datos
for i in range(7):
    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
    clima_semanal.ingresar_temperatura(temp)

# Calcular y mostrar el promedio
promedio = clima_semanal.calcular_promedio_semanal()
print(f"El promedio semanal de temperaturas es: {promedio:.2f}")
