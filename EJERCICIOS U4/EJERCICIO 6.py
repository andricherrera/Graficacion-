# Coordenadas 3D de los vértices de una caja simple
vertices_caja = [
    [-1, -1, -1],  # Vértice 0
    [ 1, -1, -1],  # Vértice 1
    [ 1,  1, -1],  # Vértice 2
    [-1,  1, -1],  # Vértice 3
    [-1, -1,  1],  # Vértice 4
    [ 1, -1,  1],  # Vértice 5
    [ 1,  1,  1],  # Vértice 6
    [-1,  1,  1],  # Vértice 7
]

# Mostrar las coordenadas de los vértices
for i, vertice in enumerate(vertices_caja):
    print(f'Vértice {i}: {vertice}')
