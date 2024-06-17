class FileHandler:
    def __init__(self, filename, mode):
        # Constructor: se llama automáticamente al crear una instancia de la clase
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)
        print(f"Archivo '{self.filename}' abierto en modo '{self.mode}'.")

    def write_data(self, data):
        # Método para escribir datos en el archivo
        if self.file and not self.file.closed:
            self.file.write(data)
            print(f"Escrito en el archivo '{self.filename}': {data}")
        else:
            print("El archivo no está abierto para escritura.")

    def __del__(self):
        # Destructor: se llama automáticamente cuando se elimina la última referencia al objeto
        if self.file and not self.file.closed:
            self.file.close()
            print(f"Archivo '{self.filename}' cerrado.")

# Uso de la clase FileHandler
def main():
    handler = FileHandler("example.txt", "w")
    handler.write_data("Hola, mundo!\n")
    handler.write_data("Este es un ejemplo de uso de __init__ y __del__.\n")

    # Cuando el objeto handler sea destruido, el archivo será cerrado automáticamente

if __name__ == "__main__":
    main()

