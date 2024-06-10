class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def descripcion(self):
        return f"{super().descripcion()}, Tipo: {self.tipo}"

# Uso
mi_coche = Coche("Toyota", "Corolla", "Sedán")
print(mi_coche.descripcion())  # Salida: Marca: Toyota, Modelo: Corolla, Tipo: Sedán
