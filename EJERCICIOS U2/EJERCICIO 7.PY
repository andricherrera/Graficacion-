import tkinter as tk
from math import sqrt

class DibujarPuntosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujar Puntos y Calcular Distancia")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.puntos = []

        self.canvas.bind("<Button-1>", self.agregar_punto)
        self.calculo_distancia_btn = tk.Button(root, text="Calcular Distancia", command=self.calcular_distancia)
        self.calculo_distancia_btn.pack()

    def agregar_punto(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")
        self.puntos.append((x, y))

    def calcular_distancia(self):
        if len(self.puntos) >= 2:
            punto1, punto2 = self.puntos[-2:]
            distancia = sqrt((punto2[0] - punto1[0]) ** 2 + (punto2[1] - punto1[1]) ** 2)
            tk.messagebox.showinfo("Distancia", f"La distancia entre los dos últimos puntos es: {distancia}")
        else:
            tk.messagebox.showwarning("Advertencia", "Debe haber al menos dos puntos para calcular la distancia.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DibujarPuntosApp(root)
    root.mainloop()
