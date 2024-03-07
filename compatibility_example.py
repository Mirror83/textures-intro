import pygame as pg
from OpenGL.GL import *


class CompatibilityApp:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.display_size = (800, 600)
        pg.display.set_mode(self.display_size, pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)

        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_COMPATIBILITY)

        self.resize(self.display_size[0], self.display_size[1])

    @staticmethod
    def resize(w: int, h: int):
        glViewport(0, 0, w, h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, 100.0, 0.0, 100.0, -1.0, 1.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    @staticmethod
    def draw_square():
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(20.0, 20.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(80.0, 20.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(80.0, 80.0, 0.0)
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(20.0, 80.0, 0.0)
        glEnd()
        glFlush()

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.VIDEORESIZE:
                    self.resize(event.size[0], event.size[1])

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.draw_square()
            pg.display.flip()
            self.clock.tick(60)


app = CompatibilityApp()
app.main_loop()
