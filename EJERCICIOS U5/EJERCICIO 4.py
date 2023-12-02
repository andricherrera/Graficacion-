import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = (
    (1, 1, 0),
    (-1, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
)

rotation_angle = 0.0

def draw_square():
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def apply_rotation(angle):
    glRotatef(angle, 0, 0, 1)

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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_square()

        # Aplicar la transformación de rotación
        apply_rotation(rotation_angle)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
