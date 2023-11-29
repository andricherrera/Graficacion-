import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Inicializar pygame y OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Inicializar pygame y OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glFrustum(-1, 1, -1, 1, 1, 50)  # Reemplaza gluPerspective con glFrustum
glTranslatef(0.0, 0.0, -5)

# ... (resto del código sin cambios)

# Función para dibujar un cubo
def dibujar_cubo():
    glBegin(GL_QUADS)
    for superficie in superficies_cubo:
        for vertice in superficie:
            glVertex3fv(vertices_cubo[vertice])
    glEnd()

# Definir vértices y superficies del cubo
vertices_cubo = [
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

superficies_cubo = [
    [0, 1, 2, 3],
    [3, 2, 7, 6],
    [6, 7, 5, 4],
    [4, 5, 1, 0],
    [1, 5, 7, 2],
    [4, 0, 3, 6]
]

# Configurar interactividad y bucle principal
glEnable(GL_DEPTH_TEST)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)  # Rotar la vista

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    dibujar_cubo()
    pygame.display.flip()
    pygame.time.wait(10)
