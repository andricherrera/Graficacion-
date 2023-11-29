import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def dibujar_cubo(ax):
    # Coordenadas de los vértices del cubo
    vertices = [
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # Cara inferior
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]   # Cara superior
    ]

    # Definir las caras del cubo
    caras = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[0], vertices[3], vertices[7], vertices[4]]
    ]

    # Dibujar el cubo
    ax.add_collection3d(Poly3DCollection(caras, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Configuración de ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Cubo en 3D')

    # Configuración del límite de ejes
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    # Mostrar el gráfico
    plt.show()

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el cubo
dibujar_cubo(ax)
