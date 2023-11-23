import tkinter as tk
from PIL import Image, ImageTk

def cerrar_ventana():
    ventana.destroy()

imagen_path = "gtr.png"

ventana = tk.Tk()
ventana.title("IMAGEN DEL EJERCICIO 1")

imagen = Image.open(imagen_path)
imagen_tk = ImageTk.PhotoImage(imagen)

etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
etiqueta_imagen.pack(padx=10, pady=10)

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack(pady=10)

ventana.mainloop()
