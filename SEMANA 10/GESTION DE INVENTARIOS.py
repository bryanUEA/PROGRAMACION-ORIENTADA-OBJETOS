import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.archivo):
            # Crear el archivo si no existe
            open(self.archivo, 'w').close()

        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    linea = linea.strip()
                    if linea:
                        producto, cantidad = linea.split(',')
                        self.productos[producto] = int(cantidad)
        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo} no se encuentra.")
        except PermissionError:
            print(f"Error: No se tiene permiso para leer el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, 'w') as file:
                for producto, cantidad in self.productos.items():
                    file.write(f"{producto},{cantidad}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"Error: No se tiene permiso para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto, cantidad):
        """Añade o actualiza un producto en el inventario."""
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return
        self.productos[producto] = self.productos.get(producto, 0) + cantidad
        self.guardar_inventario()
        print(f"Producto '{producto}' añadido/actualizado exitosamente.")

    def eliminar_producto(self, producto):
        """Elimina un producto del inventario."""
        if producto in self.productos:
            del self.productos[producto]
            self.guardar_inventario()
            print(f"Producto '{producto}' eliminado exitosamente.")
        else:
            print(f"Error: El producto '{producto}' no se encuentra en el inventario.")

    def mostrar_inventario(self):
        """Muestra los productos y sus cantidades en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto, cantidad in self.productos.items():
                print(f"{producto}: {cantidad}")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    inventario.añadir_producto('Laptop', 10)
    inventario.mostrar_inventario()
    inventario.eliminar_producto('Laptop')
    inventario.mostrar_inventario()
