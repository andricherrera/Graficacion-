import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, radians

vertices = []
radius = 1.0
scale_factor = 1.0

def draw_circle():
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    for i in range(360):
        x = radius * cos(radians(i))
        y = radius * sin(radians(i))
        glVertex3f(x, y, 0)
    glEnd()

def apply_scaling(factor):
    glScalef(factor, factor, 1.0)

def main():
    global scale_factor
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
        draw_circle()

        # Aplicar la transformación de escala
        apply_scaling(scale_factor)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

