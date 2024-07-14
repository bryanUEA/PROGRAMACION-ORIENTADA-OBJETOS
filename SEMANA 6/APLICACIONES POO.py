# Clase base 'Empleado'
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre  # Atributo privado (encapsulación)
        self.__salario = salario  # Atributo privado (encapsulación)

    def obtener_informacion(self):
        return f"Nombre: {self.__nombre}, Salario: {self.__salario}"

    def trabajar(self):
        pass  # Método que será sobrescrito por las clases derivadas

    # Métodos getter y setter para encapsulación
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

# Clase derivada 'Desarrollador' que hereda de 'Empleado'
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)  # Llamada al constructor de la clase base
        self.lenguaje = lenguaje

    def trabajar(self):
        return f"{self.get_nombre()} está codificando en {self.lenguaje}"

# Clase derivada 'Diseñador' que hereda de 'Empleado'
class Diseñador(Empleado):
    def __init__(self, nombre, salario, herramienta):
        super().__init__(nombre, salario)  # Llamada al constructor de la clase base
        self.herramienta = herramienta

    def trabajar(self):
        return f"{self.get_nombre()} está diseñando usando {self.herramienta}"

# Crear instancias de las clases y demostrar funcionalidad
desarrollador = Desarrollador("Alice", 70000, "Python")
diseñador = Diseñador("Bob", 65000, "Photoshop")

# Mostrar información de los empleados y lo que están haciendo
print(desarrollador.obtener_informacion())  # Salida: Nombre: Alice, Salario: 70000
print(desarrollador.trabajar())  # Salida: Alice está codificando en Python

print(diseñador.obtener_informacion())  # Salida: Nombre: Bob, Salario: 65000
print(diseñador.trabajar())  # Salida: Bob está diseñando usando Photoshop
