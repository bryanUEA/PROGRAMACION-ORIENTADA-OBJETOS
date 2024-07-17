import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos

    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].establecer_precio(precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos.values() if
                       nombre.lower() in producto.obtener_nombre().lower()]
        return encontrados

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id_producto: vars(producto) for id_producto, producto in self.productos.items()}, f)
        print("Inventario guardado en", archivo)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos = json.load(f)
                for id_producto, datos in productos.items():
                    producto = Producto(id_producto, datos['nombre'], datos['cantidad'], datos['precio'])
                    self.añadir_producto(producto)
            print("Inventario cargado desde", archivo)
        except FileNotFoundError:
            print("El archivo no existe.")


def menu():
    inventario = Inventario()
    inventario.cargar_inventario('inventario.json')

    while True:
        print("\nMenu de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no desea actualizar): ")
            precio = input("Nuevo precio (dejar en blanco si no desea actualizar): ")
            inventario.actualizar_producto(id_producto, cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            encontrados = inventario.buscar_producto_por_nombre(nombre)
            if encontrados:
                print("Productos encontrados:")
                for producto in encontrados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            inventario.guardar_inventario('inventario.json')

        elif opcion == '7':
            inventario.guardar_inventario('inventario.json')
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, elija de nuevo.")


if __name__ == "__main__":
    menu()
