import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Efectos de sombreado y texturas")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Cargar una textura
texture = pygame.image.load("ejemplo.jpg")  # Reemplaza "texture.jpg" con tu propia textura

# Rectángulo
rect_width, rect_height = 100, 100
rect_x, rect_y = (width - rect_width) // 2, (height - rect_height) // 2
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el rectángulo
    pygame.draw.rect(screen, white, rect)  # Rectángulo blanco base

    # Aplicar sombreado
    shadow_rect = rect.inflate(10, 10)  # Aumentar el tamaño del rectángulo para el sombreado
    pygame.draw.rect(screen, black, shadow_rect)  # Dibujar el sombreado

    # Aplicar textura
    screen.blit(texture, rect)  # Dibujar la textura sobre el rectángulo

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de la ejecución
    pygame.time.Clock().tick(60)
