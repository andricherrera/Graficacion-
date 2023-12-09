import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube():
    # Definir vértices del cubo
    vertices = [
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, 1]
    ]

    # Definir caras del cubo
    edges = [
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    ]

    glBegin(GL_QUADS)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_cone():
    radius = 0.5
    height = 1.0
    slices = 20
    stacks = 20

    glColor3f(0, 0, 1)  # Color azul

    gluCylinder(gluNewQuadric(), radius, 0, height, slices, stacks)
    glTranslatef(0.0, 0.0, height)
    gluDisk(gluNewQuadric(), 0, radius, slices, stacks)

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

        glRotatef(1, 3, 1, 1)  # Rotación para animación

        # Dibujar el cubo
        glPushMatrix()
        glTranslatef(-1.5, 0.0, 0.0)
        glColor3f(1, 0, 0)  # Color rojo
        draw_cube()
        glPopMatrix()

        # Dibujar el cono
        glPushMatrix()
        glTranslatef(1.5, 0.0, 0.0)
        draw_cone()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()








