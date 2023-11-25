import matplotlib.pyplot as plt
import numpy as np

# Coordenadas originales del cuadrado
x_original = np.array([0, 1, 1, 0, 0])
y_original = np.array([0, 0, 1, 1, 0])

# Traslación (por ejemplo, trasladar el cuadrado a la derecha en 1 unidad y hacia arriba en 2 unidades)
traslacion_x = 1
traslacion_y = 2

# Nuevas coordenadas después de la traslación
x_traslacion = x_original + traslacion_x
y_traslacion = y_original + traslacion_y

# Dibujar el cuadrado original y el cuadrado trasladado
plt.plot(x_original, y_original, label='Cuadrado original')
plt.plot(x_traslacion, y_traslacion, label='Cuadrado trasladado')

# Configuraciones del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Traslación del cuadrado en el plano cartesiano')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()

# Imprimir las nuevas coordenadas después de la traslación
print("Coordenadas originales del cuadrado:")
print("x:", x_original)
print("y:", y_original)
print("\nCoordenadas después de la traslación:")
print("x:", x_traslacion)
print("y:", y_traslacion)
