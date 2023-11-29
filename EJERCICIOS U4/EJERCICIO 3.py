import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def dibujar_piramide(ax, desplazamiento):
    # Coordenadas de los vértices de la pirámide
    vertices = [
        [0, 0, 0],  # Vértice en la base
        [1, 0, 0],  # Vértice en la base
        [1, 0, 1],  # Vértice en la base
        [0, 0, 1],  # Vértice en la base
        [0.5, 1, 0.5]  # Vértice en la cima
    ]

    # Aplica desplazamiento a las coordenadas en X
    vertices_desplazados = [[v[0] + desplazamiento, v[1], v[2]] for v in vertices]

    # Definir las caras de la pirámide
    caras = [
        [vertices_desplazados[0], vertices_desplazados[1], vertices_desplazados[2], vertices_desplazados[3]],  # Base
        [vertices_desplazados[0], vertices_desplazados[1], vertices_desplazados[4]],  # Lado 1
        [vertices_desplazados[1], vertices_desplazados[2], vertices_desplazados[4]],  # Lado 2
        [vertices_desplazados[2], vertices_desplazados[3], vertices_desplazados[4]],  # Lado 3
        [vertices_desplazados[3], vertices_desplazados[0], vertices_desplazados[4]]   # Lado 4
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

# Crear una figura 3D
fig = plt.figure()

# Dibujar la pirámide en la primera posición
ax1 = fig.add_subplot(121, projection='3d')
dibujar_piramide(ax1, desplazamiento=0)

# Dibujar la pirámide en la segunda posición (ligeramente desplazada)
ax2 = fig.add_subplot(122, projection='3d')
dibujar_piramide(ax2, desplazamiento=0.05)

# Mostrar el gráfico
plt.show()
