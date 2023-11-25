import matplotlib.pyplot as plt
import numpy as np

# Coordenadas originales del triángulo
x_original = np.array([0, 1, 0.5, 0])
y_original = np.array([0, 0, np.sqrt(3)/2, 0])

# Traslación (por ejemplo, trasladar el triángulo a la derecha en 2 unidades y hacia arriba en 1 unidad)
traslacion_x = 2
traslacion_y = 1

# Nuevas coordenadas después de la traslación
x_traslacion = x_original + traslacion_x
y_traslacion = y_original + traslacion_y

# Dibujar el triángulo original y el triángulo trasladado
plt.plot(x_original, y_original, label='Triángulo original')
plt.plot(x_traslacion, y_traslacion, label='Triángulo trasladado')

# Configuraciones del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Traslación del triángulo en el plano cartesiano')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()

# Imprimir las nuevas coordenadas después de la traslación
print("Coordenadas originales del triángulo:")
print("x:", x_original)
print("y:", y_original)
print("\nCoordenadas después de la traslación:")
print("x:", x_traslacion)
print("y:", y_traslacion)
