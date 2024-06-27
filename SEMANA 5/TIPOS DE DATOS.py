import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    area = math.pi * radio ** 2
    return area

def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dada su base y altura."""
    area = base * altura
    return area

def convertir_celsius_a_fahrenheit(celsius):
    """Convierte la temperatura de grados Celsius a Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    # Solicitar datos del usuario
    radio = float(input("Introduce el radio del círculo: "))
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))
    celsius = float(input("Introduce la temperatura en grados Celsius: "))

    # Calcular áreas
    area_circulo = calcular_area_circulo(radio)
    area_rectangulo = calcular_area_rectangulo(base, altura)
    fahrenheit = convertir_celsius_a_fahrenheit(celsius)

    # Mostrar resultados
    print(f"\nÁrea del círculo con radio {radio}: {area_circulo:.2f}")
    print(f"Área del rectángulo con base {base} y altura {altura}: {area_rectangulo:.2f}")
    print(f"Temperatura en Fahrenheit: {fahrenheit:.2f}")

if __name__ == "__main__":
    main()
