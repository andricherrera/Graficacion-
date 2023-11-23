import matplotlib.pyplot as plt

def ingresar_coordenadas():
    coordenadas = []
    while True:
        try:
            x = float(input("Ingresa la coordenada x (o cualquier letra para salir): "))
            y = float(input("Ingresa la coordenada y: "))
            coordenadas.append((x, y))
        except ValueError:
            break
    return coordenadas

def mostrar_grafico(coordenadas):
    x = [punto[0] for punto in coordenadas]
    y = [punto[1] for punto in coordenadas]

    plt.scatter(x, y)
    plt.title('Gráfico de Coordenadas')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Introduce las coordenadas. Para salir, introduce una letra.")
    coordenadas = ingresar_coordenadas()

    if coordenadas:
        mostrar_grafico(coordenadas)
    else:
        print("No se ingresaron coordenadas.")
