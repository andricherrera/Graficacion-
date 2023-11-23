import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujando Formas")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.shape_type = tk.StringVar()
        self.shape_type.set("line")  


        shape_label = tk.Label(root, text="Selecciona una forma:")
        shape_label.pack()

        line_button = tk.Radiobutton(root, text="Línea", variable=self.shape_type, value="line")
        line_button.pack()

        rectangle_button = tk.Radiobutton(root, text="Rectángulo", variable=self.shape_type, value="rectangle")
        rectangle_button.pack()

        circle_button = tk.Radiobutton(root, text="Círculo", variable=self.shape_type, value="circle")
        circle_button.pack()

        clear_button = tk.Button(root, text="Borrar todo", command=self.clear_canvas)
        clear_button.pack()

        self.canvas.bind("<Button-1>", self.draw_shape)

    def draw_shape(self, event):
        x, y = event.x, event.y
        shape_type = self.shape_type.get()

        if shape_type == "line":
            self.canvas.create_line(x - 10, y - 10, x + 10, y + 10, fill="black")
        elif shape_type == "rectangle":
            self.canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10, outline="black")
        elif shape_type == "circle":
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, outline="black")

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
