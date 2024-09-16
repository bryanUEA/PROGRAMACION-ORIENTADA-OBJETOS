# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Titulo y autor almacenados como tupla inmutable
        self.info = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.info[1]}, Autor: {self.info[0]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        if self.libros_prestados:
            return [str(libro) for libro in self.libros_prestados]
        else:
            return "No tiene libros prestados."

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros (clave: ISBN, valor: objeto Libro)
        self.usuarios = {}  # Diccionario de usuarios (clave: ID de usuario, valor: objeto Usuario)
        self.ids_usuarios = set()  # Conjunto para asegurar IDs de usuarios únicos

    # Añadir libro a la biblioteca
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.info[1]}' añadido a la biblioteca.")
        else:
            print("El libro ya está en la biblioteca.")

    # Eliminar libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.info[1]}' eliminado de la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    # Registrar nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.ids_usuarios:
            self.usuarios[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print("El ID de usuario ya está en uso.")

    # Dar de baja a un usuario
    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios.pop(user_id)
            self.ids_usuarios.remove(user_id)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print("El usuario no está registrado.")

    # Prestar un libro
    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros.pop(isbn)  # Quita el libro de la biblioteca
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.info[1]}' prestado a '{usuario.nombre}'.")
        else:
            print("No se pudo realizar el préstamo (Usuario o libro no encontrado).")

    # Devolver un libro
    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros[isbn] = libro  # Regresa el libro a la biblioteca
                    print(f"Libro '{libro.info[1]}' devuelto por '{usuario.nombre}'.")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and libro.info[1].lower() == valor.lower()) or \
               (criterio == "autor" and libro.info[0].lower() == valor.lower()) or \
               (criterio == "categoria" and libro.categoria.lower() == valor.lower()):
                resultados.append(str(libro))
        return resultados if resultados else "No se encontraron libros con ese criterio."

    # Listar libros prestados de un usuario
    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            return usuario.listar_libros_prestados()
        else:
            return "Usuario no encontrado."


# Pruebas del sistema
if __name__ == "__main__":
    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "123456")
    libro2 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "654321")
    libro3 = Libro("Ficciones", "Jorge Luis Borges", "Ficción", "789012")

    # Crear usuarios
    usuario1 = Usuario("Ana", "U001")
    usuario2 = Usuario("Carlos", "U002")

    # Crear biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("U001", "123456")
    biblioteca.prestar_libro("U002", "654321")

    # Listar libros prestados por usuarios
    print(usuario1.listar_libros_prestados())
    print(usuario2.listar_libros_prestados())

    # Devolver libros
    biblioteca.devolver_libro("U001", "123456")

    # Buscar libros por autor
    print(biblioteca.buscar_libros("autor", "Jorge Luis Borges"))

    # Listar libros prestados de un usuario
    print(biblioteca.listar_libros_prestados("U001"))

    # Eliminar libro
    biblioteca.quitar_libro("789012")
