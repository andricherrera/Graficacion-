import matplotlib.pyplot as plt
import numpy as np

def codificacion_punto(x, y, xmin, ymin, xmax, ymax):
    codigo = 0
    if x < xmin:
        codigo |= 1
    elif x > xmax:
        codigo |= 2
    if y < ymin:
        codigo |= 4
    elif y > ymax:
        codigo |= 8
    return codigo

def recorte_cohen_sutherland(poligono, xmin, ymin, xmax, ymax):
    resultado = []

    for i in range(0, len(poligono[0])-1, 2):
        x1, y1, w1 = poligono[:, i]
        x2, y2, w2 = poligono[:, i+1]

        c1 = codificacion_punto(x1/w1, y1/w1, xmin, ymin, xmax, ymax)
        c2 = codificacion_punto(x2/w2, y2/w2, xmin, ymin, xmax, ymax)

        dentro = False
        while True:
            # Ambos puntos dentro de la ventana de recorte
            if c1 == 0 and c2 == 0:
                dentro = True
                break

            # Ambos puntos fuera de la ventana de recorte
            elif (c1 & c2) != 0:
                break

            # Al menos un punto fuera de la ventana, se realiza la intersección
            else:
                codigo_externo = c1 if c1 != 0 else c2
                x, y, w = 0, 0, 0

                if codigo_externo & 1:
                    x = xmin
                    y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                    w = w1 + (w2 - w1) * (xmin - x1) / (x2 - x1)
                elif codigo_externo & 2:
                    x = xmax
                    y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                    w = w1 + (w2 - w1) * (xmax - x1) / (x2 - x1)
                elif codigo_externo & 4:
                    y = ymin
                    x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                    w = w1 + (w2 - w1) * (ymin - y1) / (y2 - y1)
                elif codigo_externo & 8:
                    y = ymax
                    x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                    w = w1 + (w2 - w1) * (ymax - y1) / (y2 - y1)

                if codigo_externo == c1:
                    x1, y1, w1 = x, y, w
                    c1 = codificacion_punto(x1/w1, y1/w1, xmin, ymin, xmax, ymax)
                else:
                    x2, y2, w2 = x, y, w
                    c2 = codificacion_punto(x2/w2, y2/w2, xmin, ymin, xmax, ymax)

        if dentro:
            resultado.extend([x1, y1, w1, x2, y2, w2])

    return np.array(resultado).reshape(3, -1)

# Definir un polígono irregular en coordenadas homogéneas
poligono_homogeneo = np.array([
    [2, 4, 5, 3, 2],
    [1, 1, 3, 4, 1],
    [1, 1, 1, 1, 1]
])

# Definir la región de recorte rectangular
xmin, ymin, xmax, ymax = 1, 0, 3, 2

# Aplicar el algoritmo de recorte de Cohen-Sutherland
resultado_recorte = recorte_cohen_sutherland(poligono_homogeneo, xmin, ymin, xmax, ymax)

# Convertir las coordenadas resultantes a coordenadas cartesianas
resultado_cartesiano = resultado_recorte[:2, :] / resultado_recorte[2, :]

# Dibujar el polígono original y el resultado recortado
plt.plot(poligono_homogeneo[0, :], poligono_homogeneo[1, :], label='Polígono original')
plt.plot(resultado_cartesiano[0, :], resultado_cartesiano[1, :], label='Resultado recortado')

# Configuraciones del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Recorte de polígono con algoritmo de Cohen-Sutherland')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()

