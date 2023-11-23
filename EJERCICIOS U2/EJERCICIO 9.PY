import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Patrón de Puntos Aleatorios")

# Función para generar puntos aleatorios
def generar_puntos(num_puntos):
    puntos = []
    for _ in range(num_puntos):
        x = random.randint(0, width)
        y = random.randint(0, height)
        puntos.append((x, y))
    return puntos

# Función para dibujar los puntos en la ventana
def dibujar_puntos(puntos):
    for punto in puntos:
        pygame.draw.circle(window, (255, 255, 255), punto, 3)

# Bucle principal del programa
def main():
    clock = pygame.time.Clock()
    puntos = generar_puntos(100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill((0, 0, 0))  # Limpiar la ventana
        dibujar_puntos(puntos)  # Dibujar los puntos en la ventana

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
