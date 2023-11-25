import matplotlib.pyplot as plt
import numpy as np

# Coordenadas homogéneas del triángulo
triangulo_homogeneo = np.array([
    [0, 1, 0.5, 0],
    [0, 0, np.sqrt(3)/2, 0],
    [1, 1, 1, 1]
])

# Matriz de traslación homogénea (trasladar el triángulo a la derecha en 2 unidades y hacia arriba en 1 unidad)
matriz_traslacion = np.array([
    [1, 0, 2],
    [0, 1, 1],
    [0, 0, 1]
])

# Aplicar la transformación de traslación
triangulo_trasladado_homogeneo = np.dot(matriz_traslacion, triangulo_homogeneo)

# Convertir de coordenadas homogéneas a cartesianas dividiendo por la última coordenada
triangulo_trasladado_cartesiano = triangulo_trasladado_homogeneo[:2, :] / triangulo_trasladado_homogeneo[2, :]

# Dibujar el triángulo original y el triángulo trasladado
plt.plot(triangulo_homogeneo[0, :], triangulo_homogeneo[1, :], label='Triángulo original')
plt.plot(triangulo_trasladado_cartesiano[0, :], triangulo_trasladado_cartesiano[1, :], label='Triángulo trasladado')

# Configuraciones del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Transformación con coordenadas homogéneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()
