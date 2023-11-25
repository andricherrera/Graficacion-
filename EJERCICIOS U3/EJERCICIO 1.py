import matplotlib.pyplot as plt
import numpy as np

# Coordenadas de los vértices del triángulo
x = np.array([0, 1, 0.5, 0])
y = np.array([0, 0, np.sqrt(3)/2, 0])

# Dibujar el triángulo
plt.plot(x, y, label='Triángulo original')

# Configuraciones del gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Triángulo en el plano cartesiano')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()
