import tkinter as tk
import math

class DibujoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujo de Elipses, Hipérbolas y Parábolas")

        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()

        self.draw_ellipse_button = tk.Button(root, text="Dibujar Elipse", command=self.draw_ellipse)
        self.draw_ellipse_button.pack()

        self.draw_hyperbola_button = tk.Button(root, text="Dibujar Hipérbola", command=self.draw_hyperbola)
        self.draw_hyperbola_button.pack()

        self.draw_parabola_button = tk.Button(root, text="Dibujar Parábola", command=self.draw_parabola)
        self.draw_parabola_button.pack()

    def draw_ellipse(self):
        a = 50  # Semieje mayor
        b = 30  # Semieje menor
        x0, y0 = 250, 250  # Centro de la elipse

        self.canvas.create_oval(x0 - a, y0 - b, x0 + a, y0 + b, outline="blue")

    def draw_hyperbola(self):
        a = 50  # Distancia del vértice al centro
        b = 30  # Distancia del foco al centro
        x0, y0 = 250, 250  # Centro de la hipérbola

        for x in range(1, 360):
            y = y0 + b * math.sqrt(1 + (x - x0) ** 2 / a ** 2)
            self.canvas.create_oval(x, y, x + 1, y + 1, outline="red")

            y = y0 - b * math.sqrt(1 + (x - x0) ** 2 / a ** 2)
            self.canvas.create_oval(x, y, x + 1, y + 1, outline="red")

    def draw_parabola(self):
        p = 30  # Parámetro de la parábola
        x0, y0 = 250, 250  # Vértice de la parábola

        for x in range(1, 500):
            y = y0 - p * (x - x0) ** 2
            self.canvas.create_oval(x, y, x + 1, y + 1, outline="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = DibujoApp(root)
    root.mainloop()
