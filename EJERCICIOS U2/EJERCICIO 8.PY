import numpy as np
import matplotlib.pyplot as plt

def generar_grafico(ecuacion, rango):
    # Generar valores x en el rango dado
    x = np.linspace(rango[0], rango[1], 1000)
    
    # Evaluar la ecuación para obtener los valores y
    y = ecuacion(x)
    
    # Crear el gráfico
    plt.plot(x, y, label=ecuacion.__name__)
    plt.scatter(x, y, color='red', s=5)  # Puntos
    
    # Configurar el gráfico
    plt.title('Gráfico de ' + ecuacion.__name__)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    
    # Mostrar el gráfico
    plt.show()

# Ejemplo de ecuación: y = x^2
def ecuacion_cuadratica(x):
    return x**2

# Definir el rango en el que quieres generar puntos
rango_x = (-10, 10)

# Generar el gráfico para la ecuación cuadrática
generar_grafico(ecuacion_cuadratica, rango_x)
