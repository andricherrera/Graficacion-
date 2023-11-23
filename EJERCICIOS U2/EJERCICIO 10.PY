import tkinter as tk

class DibujarLineasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujar Líneas")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.punto_inicial = None
        self.punto_final = None

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if self.punto_inicial is None:
            self.punto_inicial = (event.x, event.y)
        else:
            self.punto_final = (event.x, event.y)
            self.dibujar_linea()

    def dibujar_linea(self):
        if self.punto_inicial and self.punto_final:
            x1, y1 = self.punto_inicial
            x2, y2 = self.punto_final
            self.canvas.create_line(x1, y1, x2, y2, width=2, fill="black")

            # Reiniciar puntos
            self.punto_inicial = None
            self.punto_final = None

if __name__ == "__main__":
    root = tk.Tk()
    app = DibujarLineasApp(root)
    root.mainloop()
