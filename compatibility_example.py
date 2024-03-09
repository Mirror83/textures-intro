from math import cos, sin, pi
import pygame as pg
from OpenGL.GL import *

from material import Material


class CompatibilityApp:
    # The number of vertices used to draw the circle
    N = 40

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.display_size = (600, 600)
        pg.display.set_mode(self.display_size, pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)

        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_COMPATIBILITY)

        self.resize(self.display_size[0], self.display_size[1])

        self.circle_attr = (-3, 1, 0, 4)
        self.vertices = self.generate_circle_points(
            self.circle_attr[0],
            self.circle_attr[1],
            self.circle_attr[2],
            self.circle_attr[3]
        )

        self.rocket_texture = Material("textures/launch.bmp")

    @staticmethod
    def resize(w: int, h: int):
        glViewport(0, 0, w, h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-10.0, 10.0, -10.0, 10.0, -1.0, 1.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.destroy()

                if event.type == pg.VIDEORESIZE:
                    self.resize(event.size[0], event.size[1])

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.draw_circle()
            glFlush()
            pg.display.flip()
            self.clock.tick(60)

    def draw_circle(self):
        glBegin(GL_TRIANGLE_FAN)
        for vertex in self.vertices:
            glTexCoord2f(vertex[3], vertex[4])
            glVertex3f(vertex[0], vertex[1], vertex[2])

        glEnd()

    def generate_circle_points(self, x, y, z, r):
        vertices = []

        for i in range(self.N + 1):
            angle = 2 * pi * i / self.N

            # s and t are the texture coordinates
            s = 0.5 + 0.5 * cos(angle)
            t = 0.5 + 0.5 * sin(angle)

            vertices.append((x + r * cos(angle), y + r * sin(angle), z, s, t))

        return vertices

    def destroy(self):
        self.rocket_texture.destroy()
        pg.quit()
        quit()


app = CompatibilityApp()
app.main_loop()
