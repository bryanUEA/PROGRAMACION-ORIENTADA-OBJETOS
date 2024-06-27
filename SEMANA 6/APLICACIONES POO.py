# Definición de la clase base 'Animal'
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado (encapsulación)
        self.__edad = edad      # Atributo privado (encapsulación)

    def sonido(self):
        pass  # Método que será sobrescrito por las clases derivadas

    def descripcion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

# Definición de la clase derivada 'Perro' que hereda de 'Animal'
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.raza = raza

    def sonido(self):
        return "Guau!"

    def descripcion(self):
        # Polimorfismo: Sobrescribiendo el método de la clase base
        return f"{super().descripcion()}, Raza: {self.raza}"

# Definición de la clase derivada 'Gato' que hereda de 'Animal'
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.color = color

    def sonido(self):
        return "Miau!"

    def descripcion(self):
        # Polimorfismo: Sobrescribiendo el método de la clase base
        return f"{super().descripcion()}, Color: {self.color}"

# Crear instancias de las clases y demostrar funcionalidad
perro = Perro("Rex", 5, "Labrador")
gato = Gato("Mimi", 3, "Blanco")

# Mostrar descripciones y sonidos de los animales
print(perro.descripcion())  # Salida: Nombre: Rex, Edad: 5, Raza: Labrador
print(perro.sonido())       # Salida: Guau!

print(gato.descripcion())   # Salida: Nombre: Mimi, Edad: 3, Color: Blanco
print(gato.sonido())        # Salida: Miau!
