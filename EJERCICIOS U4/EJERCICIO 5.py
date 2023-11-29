import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Inicializar pygame y OpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Inicializar pygame y OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Establecer la proyección usando gluPerspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

# Posicionar la cámara
glTranslatef(0.0, 0.0, -5)



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

# Definir vértices y superficies de la pirámide
vertices_piramide = [
    [1, -1, -1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, -1, -1],
    [0, 1, 0]
]

superficies_piramide = [
    [0, 1, 4],
    [1, 2, 4],
    [2, 3, 4],
    [3, 0, 4],
    [0, 1, 2, 3]
]

# Función para dibujar un objeto
def dibujar_objeto(vertices, superficies):
    glBegin(GL_QUADS)
    for superficie in superficies:
        for vertice in superficie:
            glVertex3fv(vertices[vertice])
    glEnd()

# Configurar interactividad y bucle principal
glEnable(GL_DEPTH_TEST)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)  # Rotar la vista

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Dibujar el cubo
    glPushMatrix()
    glTranslatef(-2, 0, 0)
    dibujar_objeto(vertices_cubo, superficies_cubo)
    glPopMatrix()

    # Dibujar la pirámide
    glPushMatrix()
    glTranslatef(2, 0, 0)
    dibujar_objeto(vertices_piramide, superficies_piramide)
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)
