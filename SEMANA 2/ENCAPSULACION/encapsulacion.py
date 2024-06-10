class Coche:
    def __init__(self, velocidad_maxima):
        self.__velocidad_maxima = velocidad_maxima  # Variable privada

    def set_velocidad_maxima(self, velocidad):
        self.__velocidad_maxima = velocidad

    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

# Uso
mi_coche = Coche(180)
print(mi_coche.get_velocidad_maxima())  # Salida: 180
mi_coche.set_velocidad_maxima(200)
print(mi_coche.get_velocidad_maxima())  # Salida: 200
