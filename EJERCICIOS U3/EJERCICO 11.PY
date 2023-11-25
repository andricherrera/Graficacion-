import numpy as np

def homogenea_a_cartesiana(coordenadas_homogeneas):
    """
    Convierte coordenadas homogéneas a coordenadas cartesianas.
    """
    return coordenadas_homogeneas[:2, :] / coordenadas_homogeneas[2, :]

def cartesiana_a_homogenea(coordenadas_cartesianas):
    """
    Convierte coordenadas cartesianas a coordenadas homogéneas.
    """
    return np.vstack([coordenadas_cartesianas, np.ones(coordenadas_cartesianas.shape[1])])

# Ejemplo con un triángulo
triangulo_homogeneo = np.array([
    [0, 1, 0.5, 0],
    [0, 0, np.sqrt(3)/2, 0],
    [1, 1, 1, 1]
])

triangulo_cartesiano = homogenea_a_cartesiana(triangulo_homogeneo)
triangulo_homogeneo_nuevo = cartesiana_a_homogenea(triangulo_cartesiano)

# Imprimir resultados
print("Coordenadas homogéneas originales:")
print(triangulo_homogeneo)
print("\nCoordenadas cartesianas:")
print(triangulo_cartesiano)
print("\nCoordenadas homogéneas después de la conversión:")
print(triangulo_homogeneo_nuevo)
