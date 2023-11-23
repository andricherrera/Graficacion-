import numpy as np
import matplotlib.pyplot as plt

def generar_elipse(foco, excentricidad):
    # Parámetros
    a = foco / (1 + excentricidad)
    b = a * np.sqrt(1 - excentricidad**2)

    # Ángulos
    theta = np.linspace(0, 2*np.pi, 100)

    # Coordenadas polares
    r = a * (1 - excentricidad**2) / (1 - excentricidad * np.cos(theta))

    # Convertir coordenadas polares a cartesianas
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y

# Ajustar parámetros según necesidades
foco = 3.0
excentricidad = 0.7

x, y = generar_elipse(foco, excentricidad)

# Visualizar la elipse
plt.figure(figsize=(8, 8))
plt.plot(x, y, label=f'Foco: {foco}, Excentricidad: {excentricidad}')
plt.title('Generador de Elipses')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
