import tkinter as tk
from tkinter import messagebox

# Función para agregar el texto a la lista
def agregar():
    texto = entrada_texto.get()
    if texto:
        lista.insert(tk.END, texto)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor ingrese algún texto.")

# Función para limpiar la lista
def limpiar():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.grid(row=0, column=0, padx=10, pady=10)

# Campo de texto
entrada_texto = tk.Entry(ventana)
entrada_texto.grid(row=0, column=1, padx=10, pady=10)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.grid(row=0, column=2, padx=10, pady=10)

# Lista para mostrar los datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
