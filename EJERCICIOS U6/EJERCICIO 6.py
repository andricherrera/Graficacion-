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

translation_vector = [0.0, 0.0, 0.0]
rotation_angle = 0.0
scale_factor = 1.0

def draw_square():
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def apply_translation(vector):
    glTranslatef(vector[0], vector[1], vector[2])

def apply_rotation(angle):
    glRotatef(angle, 0, 0, 1)

def apply_scaling(factor):
    glScalef(factor, factor, 1.0)

def main():
    global translation_vector, rotation_angle, scale_factor
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

        # Traslación
        apply_translation(translation_vector)

        # Rotación
        apply_rotation(rotation_angle)

        # Escala
        apply_scaling(scale_factor)

        draw_square()

        pygame.display.flip()
        pygame.time.wait(10)

        # Actualizar parámetros para la siguiente iteración
        translation_vector[0] += 0.01
        rotation_angle += 1
        scale_factor += 0.01

if __name__ == "__main__":
    main()
