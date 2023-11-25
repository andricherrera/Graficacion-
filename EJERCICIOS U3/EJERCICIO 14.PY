import matplotlib.pyplot as plt
import numpy as np

# Definir un polígono irregular en coordenadas homogéneas
poligono_homogeneo = np.array([
    [2, 4, 5, 3, 2],
    [1, 1, 3, 4, 1],
    [1, 1, 1, 1, 1]
])

# Definir una región de recorte rectangular en coordenadas homogéneas
recorte_homogeneo = np.array([
    [1, 3, 3, 1, 1],
    [0, 0, 2, 2, 0],
    [1, 1, 1, 1, 1]
])

# Aplicar la transformación de recorte (utilizando la transposición)
resultado_homogeneo = np.dot(recorte_homogeneo.T, poligono_homogeneo)

# Convertir las coordenadas resultantes a coordenadas cartesianas
resultado_cartesiano = resultado_homogeneo[:2, :] / resultado_homogeneo[2, :]

# Dibujar el polígono original, la región de recorte y el resultado recortado
plt.plot(poligono_homogeneo[0, :], poligono_homogeneo[1, :], label='Polígono original')
plt.plot(recorte_homogeneo[0, :], recorte_homogeneo[1, :], label='Región de recorte')
plt.plot(resultado_cartesiano[0, :], resultado_cartesiano[1, :], label='Resultado recortado')

# Configuraciones del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Transformación de recorte con coordenadas homogéneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()
