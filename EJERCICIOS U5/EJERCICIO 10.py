import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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

def set_perspective_projection():
    gluPerspective(45, (display_width / display_height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def set_orthographic_projection():
    glOrtho(-2, 2, -2, 2, 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def main():
    global display_width, display_height
    pygame.init()
    display_width, display_height = 800, 600
    pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    # Cambiar entre perspectiva y proyección ortográfica
                    glMatrixMode(GL_PROJECTION)
                    glLoadIdentity()

                    if glIsEnabled(GL_DEPTH_TEST):
                        set_orthographic_projection()
                        glDisable(GL_DEPTH_TEST)
                    else:
                        set_perspective_projection()
                        glEnable(GL_DEPTH_TEST)

                    glMatrixMode(GL_MODELVIEW)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(1, 3, 1, 1)

        draw_cube()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
