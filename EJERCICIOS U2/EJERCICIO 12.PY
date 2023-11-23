import tkinter as tk
import tkinter.simpledialog

class VentanaGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujar Líneas")

        # Configuración de la ventana
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Entrada de texto para ingresar el código hexadecimal del color
        self.color_entry = tk.Entry(root)
        self.color_entry.insert(0, "#000000")  # Color negro por defecto
        self.color_entry.pack(side=tk.LEFT, padx=5)

        # Botones para seleccionar grosor de la línea
        self.grosor_button = tk.Button(root, text="Grosor", command=self.seleccionar_grosor)
        self.grosor_button.pack(side=tk.LEFT, padx=5)

        # Inicialización de variables
        self.grosor = 2

        # Coordenadas iniciales y variable para dibujar
        self.x1, self.y1 = None, None
        self.dibujando = False

        # Enlace de eventos
        self.canvas.bind("<B1-Motion>", self.dibujar_linea)
        self.canvas.bind("<ButtonRelease-1>", self.fin_dibujo)

    def seleccionar_grosor(self):
        grosor = tkinter.simpledialog.askinteger("Grosor", "Ingrese el grosor de la línea:")
        if grosor is not None:
            self.grosor = grosor

    def dibujar_linea(self, event):
        if self.x1 is not None and self.y1 is not None:
            x2, y2 = event.x, event.y
            color = self.color_entry.get()
            self.canvas.create_line(self.x1, self.y1, x2, y2, fill=color, width=self.grosor)
            self.x1, self.y1 = x2, y2

    def fin_dibujo(self, event):
        self.x1, self.y1 = None, None

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaGrafica(root)
    root.mainloop()
