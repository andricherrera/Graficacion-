import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def dibujar_piramide(ax):
    # Coordenadas de los vértices de la pirámide
    vertices = [
        [0, 0, 0],  # Vértice en la base
        [1, 0, 0],  # Vértice en la base
        [1, 0, 1],  # Vértice en la base
        [0, 0, 1],  # Vértice en la base
        [0.5, 1, 0.5]  # Vértice en la cima
    ]

    # Definir las caras de la pirámide
    caras = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Base
        [vertices[0], vertices[1], vertices[4]],  # Lado 1
        [vertices[1], vertices[2], vertices[4]],  # Lado 2
        [vertices[2], vertices[3], vertices[4]],  # Lado 3
        [vertices[3], vertices[0], vertices[4]]   # Lado 4
    ]

    # Dibujar la pirámide
    ax.add_collection3d(Poly3DCollection(caras, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Configuración de ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Pirámide en 3D')

    # Configuración del límite de ejes
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    # Mostrar el gráfico
    plt.show()

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar la pirámide
dibujar_piramide(ax)
