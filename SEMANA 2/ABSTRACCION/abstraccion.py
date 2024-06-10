from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Uso
mi_perro = Perro()
mi_gato = Gato()
print(mi_perro.hacer_sonido())  # Salida: Guau
print(mi_gato.hacer_sonido())   # Salida: Miau
