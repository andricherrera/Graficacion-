import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi, cos, sin  # Agrega la importación de pi, cos y sin

def draw_cube():
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

    glBegin(GL_TRIANGLES)
    for i in range(slices):
        angle1 = i * 2 * pi / slices
        angle2 = (i + 1) * 2 * pi / slices

        x1, y1, z1 = radius * cos(angle1), radius * sin(angle1), 0
        x2, y2, z2 = radius * cos(angle2), radius * sin(angle2), 0
        x3, y3, z3 = 0, 0, height

        glNormal3f(x1, y1, z1)
        glVertex3f(x1, y1, z1)
        glNormal3f(x2, y2, z2)
        glVertex3f(x2, y2, z2)
        glNormal3f(x3, y3, z3)
        glVertex3f(x3, y3, z3)

    glEnd()

def set_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])

def main():
    pygame.init()
    display_width, display_height = 800, 600
    pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
    gluPerspective(45, (display_width / display_height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    set_lighting()

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 3, 1, 1)

        glPushMatrix()
        glTranslatef(-1.5, 0.0, 0.0)
        glColor3f(1, 0, 0)
        draw_cube()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(1.5, 0.0, 0.0)
        glColor3f(0, 0, 1)
        draw_cone()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

