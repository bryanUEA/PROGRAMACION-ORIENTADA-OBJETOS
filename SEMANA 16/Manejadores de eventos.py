import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("400x400")

        # Lista de tareas
        self.task_list = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        add_button.pack(pady=5)

        # Lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(self.root, width=40, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Botón para marcar como completada
        complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        complete_button.pack(pady=5)

        # Botón para eliminar tarea
        delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        delete_button.pack(pady=5)

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_list.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, introduce una tarea.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_list:
            display_task = task["task"]
            if task["completed"]:
                display_task += " [Completada]"
            self.task_listbox.insert(tk.END, display_task)

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_list[selected_index]["completed"] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("No seleccionado", "Por favor, selecciona una tarea para completar.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.task_list[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("No seleccionado", "Por favor, selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
