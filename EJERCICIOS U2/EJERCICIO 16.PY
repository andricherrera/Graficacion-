import turtle

def dibujar_cuadrado(x, y, lado, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(lado)
        turtle.right(90)

    turtle.end_fill()

def main():
    turtle.speed(2)

    # Dibuja un cuadrado rojo
    dibujar_cuadrado(-50, 50, 100, "red")

    # Dibuja un cuadrado verde
    dibujar_cuadrado(-25, 25, 50, "green")

    # Dibuja un cuadrado azul
    dibujar_cuadrado(0, 0, 25, "blue")

    turtle.done()

if __name__ == "__main__":
    main()
