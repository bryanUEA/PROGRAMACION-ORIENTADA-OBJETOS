# Definición de la clase Cliente
class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente[ID: {self.id_cliente}, Nombre: {self.nombre}, Email: {self.email}]"

# Definición de la clase Habitación
class Habitación:
    def __init__(self, id_habitacion, tipo, precio):
        self.id_habitacion = id_habitacion
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = True

    def __str__(self):
        estado = "Disponible" if self.esta_disponible else "Ocupada"
        return f"Habitación[ID: {self.id_habitacion}, Tipo: {self.tipo}, Precio: ${self.precio}, Estado: {estado}]"

    def marcar_como_ocupada(self):
        self.esta_disponible = False

    def marcar_como_disponible(self):
        self.esta_disponible = True

# Definición de la clase Reserva
class Reserva:
    def __init__(self, id_reserva, cliente, habitacion, fecha_inicio, fecha_fin):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        return (f"Reserva[ID: {self.id_reserva}, Cliente: {self.cliente.nombre}, "
                f"Habitación: {self.habitacion.id_habitacion}, "
                f"Fecha de inicio: {self.fecha_inicio}, Fecha de fin: {self.fecha_fin}]")

# Ejemplo de uso del sistema de reservas

# Creación de clientes
cliente1 = Cliente(1, "Juan Pérez", "juan.perez@example.com")
cliente2 = Cliente(2, "María García", "maria.garcia@example.com")

# Creación de habitaciones
habitacion1 = Habitación(101, "Simple", 100)
habitacion2 = Habitación(102, "Doble", 150)

# Creación de reservas
reserva1 = Reserva(1, cliente1, habitacion1, "2024-07-01", "2024-07-05")
reserva2 = Reserva(2, cliente2, habitacion2, "2024-07-03", "2024-07-08")

# Marcando las habitaciones como ocupadas
habitacion1.marcar_como_ocupada()
habitacion2.marcar_como_ocupada()

# Imprimiendo la información
print(cliente1)
print(cliente2)
print(habitacion1)
print(habitacion2)
print(reserva1)
print(reserva2)

# Resultados esperados:
# Cliente[ID: 1, Nombre: Juan Pérez, Email: juan.perez@example.com]
# Cliente[ID: 2, Nombre: María García, Email: maria.garcia@example.com]
# Habitación[ID: 101, Tipo: Simple, Precio: $100, Estado: Ocupada]
# Habitación[ID: 102, Tipo: Doble, Precio: $150, Estado: Ocupada]
# Reserva[ID: 1, Cliente: Juan Pérez, Habitación: 101, Fecha de inicio: 2024-07-01, Fecha de fin: 2024-07-05]
# Reserva[ID: 2, Cliente: María García, Habitación: 102, Fecha de inicio: 2024-07-03, Fecha de fin: 2024-07-08]
