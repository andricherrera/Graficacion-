import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define las dimensiones de la ventana como variables globales
display_width, display_height = 800, 600

def draw_cube():
    glBegin(GL_QUADS)
    # ... (código del cubo)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(45, (display_width / display_height), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    
    # Rotar el cubo
    glRotatef(1, 3, 1, 1)

    draw_cube()
    pygame.display.flip()

def main():
    global display_width, display_height  # Hacer que las variables sean globales
    pygame.init()
    pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
    gluPerspective(45, (display_width / display_height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display()

if __name__ == "__main__":
    main()
