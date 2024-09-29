import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime


# Crear la clase para la aplicación de la agenda
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame superior: Entrada de datos
        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack(pady=10)

        # Etiquetas y campos de entrada
        tk.Label(self.frame_input, text="Fecha (dd/mm/yyyy):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_input, date_pattern='dd/MM/yyyy', width=12, background='darkblue',
                                    foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_input, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.time_entry = tk.Entry(self.frame_input, width=10)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.frame_input, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_input, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Botones
        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(pady=10)

        self.add_button = tk.Button(self.frame_buttons, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=0, column=0, padx=10)

        self.delete_button = tk.Button(self.frame_buttons, text="Eliminar Evento Seleccionado",
                                       command=self.delete_event)
        self.delete_button.grid(row=0, column=1, padx=10)

        self.quit_button = tk.Button(self.frame_buttons, text="Salir", command=self.root.quit)
        self.quit_button.grid(row=0, column=2, padx=10)

        # Frame inferior: Vista de eventos
        self.frame_tree = tk.Frame(self.root)
        self.frame_tree.pack(pady=10)

        # Definir TreeView
        self.tree = ttk.Treeview(self.frame_tree, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=80)
        self.tree.column("Descripción", width=300)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.pack(padx=10, pady=10)

    # Método para agregar evento
    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.desc_entry.get()

        # Validación básica
        if not time or not description:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        try:
            datetime.datetime.strptime(time, '%H:%M')
        except ValueError:
            messagebox.showerror("Hora inválida", "Por favor, introduzca una hora válida en formato HH:MM.")
            return

        # Agregar evento a la lista
        self.tree.insert("", "end", values=(date, time, description))
        self.clear_entries()

    # Método para eliminar evento
    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar eliminación",
                                          "¿Está seguro de que desea eliminar el evento seleccionado?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Selección vacía", "Por favor, seleccione un evento para eliminar.")

    # Método para limpiar las entradas de texto
    def clear_entries(self):
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.date_entry.set_date(datetime.datetime.now())


# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
