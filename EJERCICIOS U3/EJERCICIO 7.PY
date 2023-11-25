import matplotlib.pyplot as plt

# Coordenadas de los vértices del triángulo
x = [0, 1, 0.5, 0]  # Repetir el primer vértice para cerrar el triángulo
y = [0, 0, (3**0.5)/2, 0]

# Dibujar el triángulo
plt.plot(x, y, label='Triángulo')

# Configuraciones del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Polígono simple en el plano cartesiano')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()
