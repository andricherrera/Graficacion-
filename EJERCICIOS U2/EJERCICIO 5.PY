import tkinter as tk
import math

class TransformacionesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transformaciones de Coordenadas")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.rectangulo_id = self.canvas.create_rectangle(50, 50, 150, 100, fill="blue")

        trasladar_button = tk.Button(root, text="Trasladar", command=self.trasladar)
        trasladar_button.pack(side=tk.LEFT, padx=10)
        
        rotar_button = tk.Button(root, text="Rotar", command=self.rotar)
        rotar_button.pack(side=tk.LEFT, padx=10)

        escalar_button = tk.Button(root, text="Escalar", command=self.escalar)
        escalar_button.pack(side=tk.LEFT, padx=10)

    def trasladar(self):
        # Realizar una traslación de 20 unidades en ambas coordenadas
        self.canvas.move(self.rectangulo_id, 20, 20)

    def rotar(self):
        coords = self.canvas.coords(self.rectangulo_id)

        centro_x = (coords[0] + coords[2]) / 2
        centro_y = (coords[1] + coords[3]) / 2

        angulo = math.radians(45)

        self.canvas.delete(self.rectangulo_id)
        self.rectangulo_id = self.canvas.create_rectangle(*self.rotar_punto(coords, centro_x, centro_y, angulo), fill="blue")

    def escalar(self):
        self.canvas.scale(self.rectangulo_id, 0, 0, 1.5, 1.5)

    def rotar_punto(self, punto, cx, cy, angulo):
        x, y = punto[0], punto[1]
        nx = cx + (x - cx) * math.cos(angulo) - (y - cy) * math.sin(angulo)
        ny = cy + (x - cx) * math.sin(angulo) + (y - cy) * math.cos(angulo)
        return nx, ny, nx + (punto[2] - punto[0]), ny + (punto[3] - punto[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = TransformacionesApp(root)
    root.mainloop()
