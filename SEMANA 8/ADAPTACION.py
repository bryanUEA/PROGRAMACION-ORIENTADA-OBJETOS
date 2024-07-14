import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def ejecutar_script(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        print(f"\n--- Ejecutando {ruta_script} ---\n")
        os.system(f'python "{ruta_script_absoluta}"')
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el archivo: {e}")

def buscar_script(nombre_parcial, opciones):
    resultados = {key: val for key, val in opciones.items() if nombre_parcial.lower() in val.lower()}
    return resultados

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Unidad 2/2.1. Introducción a Python/2.1-1. Hola Mundo.py',
        '3': 'Unidad 3/3.1. Estructuras de Datos/3.1-1. Listas y Tuplas.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n--- Menú Principal - Dashboard ---")
        print("1. Ver código de un script")
        print("2. Ejecutar un script")
        print("3. Buscar un script por nombre")
        print("0. Salir")
        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            break
        elif eleccion == '1':
            print("\n--- Ver código de un script ---")
            for key in opciones:
                print(f"{key} - {opciones[key]}")
            eleccion_script = input("Elige un script para ver su código o '0' para volver al menú principal: ")
            if eleccion_script in opciones:
                ruta_script = os.path.join(ruta_base, opciones[eleccion_script])
                mostrar_codigo(ruta_script)
            else:
                print("Opción no válida.")
        elif eleccion == '2':
            print("\n--- Ejecutar un script ---")
            for key in opciones:
                print(f"{key} - {opciones[key]}")
            eleccion_script = input("Elige un script para ejecutar o '0' para volver al menú principal: ")
            if eleccion_script in opciones:
                ruta_script = os.path.join(ruta_base, opciones[eleccion_script])
                ejecutar_script(ruta_script)
            else:
                print("Opción no válida.")
        elif eleccion == '3':
            nombre_parcial = input("Introduce parte del nombre del script a buscar: ")
            resultados = buscar_script(nombre_parcial, opciones)
            if resultados:
                print("\n--- Resultados de la búsqueda ---")
                for key in resultados:
                    print(f"{key} - {resultados[key]}")
            else:
                print("No se encontraron scripts que coincidan con la búsqueda.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()

