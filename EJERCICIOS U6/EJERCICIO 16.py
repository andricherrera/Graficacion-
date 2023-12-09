import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def set_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])

    glEnable(GL_LIGHT1)

    glLightfv(GL_LIGHT1, GL_POSITION, [-1, -1, -1, 0])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [0.5, 0.5, 0.5, 1])

def mouse_pick(x, y):
    viewport = glGetIntegerv(GL_VIEWPORT)
    modelview = glGetDoublev(GL_MODELVIEW_MATRIX)
    projection = glGetDoublev(GL_PROJECTION_MATRIX)

    y = viewport[3] - y  # Invertir y para que coincida con la ventana de OpenGL

    # Desproyectar las coordenadas de la ventana a las coordenadas del mundo
    obj_x, obj_y, obj_z = gluUnProject(x, y, 0.0, modelview, projection, viewport)
    dir_x, dir_y, dir_z = gluUnProject(x, y, 1.0, modelview, projection, viewport)

    # Calcular la dirección del rayo
    ray_dir = [dir_x - obj_x, dir_y - obj_y, dir_z - obj_z]
    ray_length = 10.0  # Longitud del rayo, puedes ajustarla según tus necesidades

    # Normalizar la dirección del rayo
    length = (ray_dir[0]**2 + ray_dir[1]**2 + ray_dir[2]**2)**0.5
    ray_dir = [ray_dir[0] / length, ray_dir[1] / length, ray_dir[2] / length]

    # Calcular el punto final del rayo
    end_point = [obj_x + ray_dir[0] * ray_length, obj_y + ray_dir[1] * ray_length, obj_z + ray_dir[2] * ray_length]

    return obj_x, obj_y, obj_z, end_point[0], end_point[1], end_point[2]

def main():
    pygame.init()
    display_width, display_height = 800, 600
    pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    set_lighting()

    gluPerspective(45, (display_width / display_height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                x, y = event.pos
                obj_x, obj_y, obj_z, end_x, end_y, end_z = mouse_pick(x, y)
                print(f"Clicked at ({obj_x}, {obj_y}, {obj_z})")

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(angle, 0, 1, 0)

        glColor3f(1, 0, 0)
        draw_cube()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
