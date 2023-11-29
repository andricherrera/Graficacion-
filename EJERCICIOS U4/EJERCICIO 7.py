import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las coordenadas de los puntos que representan la silla
silla_coords = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0.5, 1, 0],
    [0.2, 1.2, 0],
    [0.8, 1.2, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
    [0.5, 1, 1],
    [0.2, 1.2, 1],
    [0.8, 1.2, 1]
]

# Configurar la figura para las proyecciones ortográficas
fig_orto = plt.figure(figsize=(8, 4))

# Vista desde arriba (proyección ortográfica)
ax_orto_top = fig_orto.add_subplot(121)
ax_orto_top.scatter([point[0] for point in silla_coords], [point[1] for point in silla_coords])
ax_orto_top.set_title('Vista desde arriba (Proyección ortográfica)')
ax_orto_top.set_aspect('equal')

# Vista desde un lado (proyección ortográfica)
ax_orto_side = fig_orto.add_subplot(122)
ax_orto_side.scatter([point[2] for point in silla_coords], [point[1] for point in silla_coords])
ax_orto_side.set_title('Vista desde un lado (Proyección ortográfica)')
ax_orto_side.set_aspect('equal')

# Configurar la figura para la perspectiva
fig_persp = plt.figure(figsize=(8, 4))
ax_persp = fig_persp.add_subplot(111, projection='3d')

# Dibujar la silla en perspectiva
ax_persp.scatter([point[0] for point in silla_coords], [point[1] for point in silla_coords], [point[2] for point in silla_coords])
ax_persp.set_title('Vista en perspectiva')

# Mostrar las figuras
plt.show()
