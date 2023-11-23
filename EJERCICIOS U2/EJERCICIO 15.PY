import turtle

# Configuración inicial
turtle.speed(2)  # Velocidad de dibujo

# Función para dibujar una elipse
def draw_ellipse(a, b):
    turtle.color("orange")  # Establecer el color de la línea a naranja
    turtle.pendown()  # Levantar el lápiz para comenzar un nuevo trazo
    turtle.begin_fill()  # Iniciar el relleno de la elipse

    for _ in range(2):
        turtle.circle(a, 90)
        turtle.circle(b, 90)

    turtle.end_fill()  # Finalizar el relleno

# Posicionar la tortuga en la mitad de la ventana y un poco más abajo
turtle.penup()
turtle.goto(0, -200)  # Ajustar la posición según sea necesario

# Animación de la elipse cambiando tamaño y forma con el tiempo
for i in range(100):
    # Cambiar tamaño y forma de la elipse
    a = 50 + i  # Ajusta el valor según tus preferencias
    b = 25 + i  # Ajusta el valor según tus preferencias

    turtle.clear()  # Limpiar la pantalla antes de dibujar la siguiente elipse
    draw_ellipse(a, b)

    # Ajustar la posición para que la elipse esté centrada verticalmente
    turtle.penup()
    turtle.goto(0, -200)

# Mantener la ventana abierta después de la animación
turtle.done()
