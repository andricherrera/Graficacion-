import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
)

translation_vector = [0.0, 0.0, 0.0]

def draw_triangle():
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def apply_translation(vector):
    glTranslatef(vector[0], vector[1], vector[2])

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
        draw_triangle()

        # Aplicar la transformación de traslación
        apply_translation(translation_vector)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
