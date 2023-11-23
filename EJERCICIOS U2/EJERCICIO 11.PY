import tkinter as tk
from sympy import symbols, Eq, solve, sympify

class LineIntersectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Intersección de Líneas")

        self.label1 = tk.Label(master, text="Ecuación de la línea 1:")
        self.label1.pack()

        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.label2 = tk.Label(master, text="Ecuación de la línea 2:")
        self.label2.pack()

        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        self.calculate_button = tk.Button(master, text="Calcular Intersección", command=self.calculate_intersection)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_intersection(self):
        equation1 = self.entry1.get()
        equation2 = self.entry2.get()

        x, y = symbols('x y')
        try:
            line1 = Eq(sympify(equation1), 0)
            line2 = Eq(sympify(equation2), 0)

            intersection = solve((line1, line2), (x, y))

            if intersection:
                self.result_label.config(text=f"Intersección en x={intersection[x]}, y={intersection[y]}")
            else:
                self.result_label.config(text="Las líneas son paralelas y no se intersectan.")
        except Exception as e:
            self.result_label.config(text="Error al calcular la intersección. Verifica las ecuaciones.")

def main():
    root = tk.Tk()
    app = LineIntersectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
