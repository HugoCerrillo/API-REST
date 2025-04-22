import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

class Nota:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

class AppNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Tablero de Avisos y Notas")

        self.notas = []

        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill='both', expand=True)

        self.boton_agregar = ttk.Button(self.frame, text="Agregar Nota", command=self.agregar_nota)
        self.boton_agregar.pack(pady=5)

        self.lista_notas = tk.Listbox(self.frame)
        self.lista_notas.pack(fill='both', expand=True)
        self.lista_notas.bind('<Double-Button-1>', self.ver_nota)

        self.boton_editar = ttk.Button(self.frame, text="Editar Nota", command=self.editar_nota)
        self.boton_editar.pack(pady=5)

        self.boton_eliminar = ttk.Button(self.frame, text="Eliminar Nota", command=self.eliminar_nota)
        self.boton_eliminar.pack(pady=5)

    def agregar_nota(self):
        titulo = simpledialog.askstring("Título", "Ingrese el título de la nota:")
        contenido = simpledialog.askstring("Contenido", "Ingrese el contenido de la nota:")
        if titulo and contenido:
            nota = Nota(titulo, contenido)
            self.notas.append(nota)
            self.actualizar_lista()

    def ver_nota(self, event):
        seleccion = self.lista_notas.curselection()
        if seleccion:
            nota = self.notas[seleccion[0]]
            messagebox.showinfo(nota.titulo, nota.contenido)

    def editar_nota(self):
        seleccion = self.lista_notas.curselection()
        if seleccion:
            nota = self.notas[seleccion[0]]
            nuevo_titulo = simpledialog.askstring("Editar Título", "Nuevo título:", initialvalue=nota.titulo)
            nuevo_contenido = simpledialog.askstring("Editar Contenido", "Nuevo contenido:", initialvalue=nota.contenido)
            if nuevo_titulo and nuevo_contenido:
                nota.titulo = nuevo_titulo
                nota.contenido = nuevo_contenido
                self.actualizar_lista()

    def eliminar_nota(self):
        seleccion = self.lista_notas.curselection()
        if seleccion:
            del self.notas[seleccion[0]]
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_notas.delete(0, tk.END)
        for nota in self.notas:
            self.lista_notas.insert(tk.END, nota.titulo)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppNotas(root)
    root.mainloop()
