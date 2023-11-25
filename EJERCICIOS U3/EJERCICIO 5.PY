import matplotlib.pyplot as plt
import numpy as np

# Coordenadas originales del cuadrado
x_original = np.array([0, 1, 1, 0, 0])
y_original = np.array([0, 0, 1, 1, 0])

# Ángulo de rotación en radianes (por ejemplo, rotar 45 grados en sentido antihorario)
angulo_rotacion = np.radians(45)

# Matriz de rotación en sentido antihorario
matriz_rotacion = np.array([[np.cos(angulo_rotacion), -np.sin(angulo_rotacion)],
                            [np.sin(angulo_rotacion), np.cos(angulo_rotacion)]])

# Aplicar la rotación a las coordenadas originales
coordenadas_rotadas = np.dot(matriz_rotacion, np.vstack((x_original, y_original)))

# Dibujar el cuadrado original y el cuadrado rotado
plt.plot(x_original, y_original, label='Cuadrado original')
plt.plot(coordenadas_rotadas[0], coordenadas_rotadas[1], label='Cuadrado rotado')

# Configuraciones del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Rotación del cuadrado en el plano cartesiano')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()

# Imprimir las nuevas coordenadas después de la rotación
print("Coordenadas originales del cuadrado:")
print("x:", x_original)
print("y:", y_original)
print("\nCoordenadas después de la rotación:")
print("x:", coordenadas_rotadas[0])
print("y:", coordenadas_rotadas[1])
