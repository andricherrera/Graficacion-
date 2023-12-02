import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    display_width, display_height = 800, 600
    pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
    gluPerspective(45, (display_width / display_height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Cambiar el color de fondo a un tono de verde (R, G, B, Alpha)
        glClearColor(0.2, 0.8, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(1, 3, 1, 1)  # Rotación para animación

        # Aquí puedes agregar tu código de dibujo
        glBegin(GL_QUADS)
        glVertex3f(-1, -1, 0)
        glVertex3f(1, -1, 0)
        glVertex3f(1, 1, 0)
        glVertex3f(-1, 1, 0)
        glEnd()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
