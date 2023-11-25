import matplotlib.pyplot as plt

# Coordenadas originales del triángulo
x_original = [0, 1, 0.5, 0]  # Repetir el primer vértice para cerrar el triángulo
y_original = [0, 0, (3**0.5)/2, 0]

# Factor de escala (por ejemplo, escalar el triángulo por un factor de 2 en ambas direcciones)
factor_escala = 2

# Calcular las nuevas coordenadas después del cambio de escala
x_escala = [coord * factor_escala for coord in x_original]
y_escala = [coord * factor_escala for coord in y_original]

# Dibujar el triángulo original y el triángulo escalado
plt.plot(x_original, y_original, label='Triángulo original')
plt.plot(x_escala, y_escala, label='Triángulo escalado')

# Configuraciones del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Cambio de escala en el plano cartesiano')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()

# Imprimir las nuevas coordenadas después del cambio de escala
print("Coordenadas originales del triángulo:")
print("x:", x_original)
print("y:", y_original)
print("\nCoordenadas después del cambio de escala:")
print("x:", x_escala)
print("y:", y_escala)
