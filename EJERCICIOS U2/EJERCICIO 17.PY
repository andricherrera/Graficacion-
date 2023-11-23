import tkinter as tk

class DibujarLetrasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujar Letras")
        
        self.canvas = tk.Canvas(root, width=500, height=300, bg="white")
        self.canvas.pack()

        self.text_entry = tk.Entry(root, font=("Arial", 14))
        self.text_entry.pack(pady=10)

        self.draw_button = tk.Button(root, text="Dibujar", command=self.dibujar_texto)
        self.draw_button.pack()

    def dibujar_texto(self):
        texto = self.text_entry.get()
        self.canvas.delete("all")  # Borrar el contenido actual del lienzo

        x, y = 50, 150  # Posición inicial para dibujar el texto

        for caracter in texto:
            self.canvas.create_text(x, y, text=caracter, font=("Arial", 20), anchor=tk.W)
            x += 25  # Espaciado entre caracteres

if __name__ == "__main__":
    root = tk.Tk()
    app = DibujarLetrasApp(root)
    root.mainloop()
