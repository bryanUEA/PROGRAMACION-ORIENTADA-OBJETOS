def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Entrada de datos
temperaturas = ingresar_temperaturas()

# Cálculo del promedio
promedio = calcular_promedio_semanal(temperaturas)
print(f"El promedio semanal de temperaturas es: {promedio:.2f}")
