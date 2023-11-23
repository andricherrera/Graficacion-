import tkinter as tk

class CoordenadasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Coordenadas")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.coordenadas_label = tk.Label(root, text="Coordenadas: (0, 0)")
        self.coordenadas_label.pack(pady=10)

        self.canvas.bind("<Button-1>", self.obtener_coordenadas)

    def obtener_coordenadas(self, event):
        x = event.x
        y = event.y

        self.coordenadas_label.config(text=f"Coordenadas: ({x}, {y})")

        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordenadasApp(root)
    root.mainloop()
