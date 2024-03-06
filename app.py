from os import PathLike

import pygame as pg
from OpenGL.GL import *
import sys

from OpenGL.GL.shaders import compileProgram, compileShader, ShaderProgram

from triangle import Triangle


class App:
    """This class uses pygame as the windowing system instead of the more conventional GLFW or GLUT"""
    FRAME_RATE = 60

    def __init__(self) -> None:
        pg.init()
        self.clock = pg.time.Clock()
        # The pg.OPENGL flag creates an OpenGL context
        # and pg.DOUBLEBUF tells pygame to use a double buffer for drawing
        pg.display.set_mode(pg.Vector2(600, 600), pg.OPENGL | pg.DOUBLEBUF)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_COMPATIBILITY)
        glClearColor(1, 1, 1, 1)

        self.shader = self.create_shaders("shaders/shaders.vert", "shaders/shaders.frag")
        glUseProgram(self.shader)

        self.triangle = Triangle()
        self.main_loop()

    @staticmethod
    def create_shaders(vert_shader_path: PathLike[str] | str, frag_shader_path: PathLike[str] | str) -> ShaderProgram:
        with open(vert_shader_path, "r") as f:
            vert_source = f.readlines()

        with open(frag_shader_path, "r") as f:
            frag_source = f.readlines()

        shader = compileProgram(
            compileShader(vert_source, GL_VERTEX_SHADER),
            compileShader(frag_source, GL_FRAGMENT_SHADER)
        )

        return shader

    def main_loop(self) -> None:
        while True:
            # Event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()

            # Screen update
            glClear(GL_COLOR_BUFFER_BIT)
            # self.draw_square_annulus()
            glUseProgram(self.shader)
            glBindVertexArray(self.triangle.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.triangle.vertex_count)

            pg.display.flip()

            self.clock.tick(self.FRAME_RATE)

    def quit(self):
        self.triangle.destroy()
        glDeleteProgram(self.shader)
        # Perform pygame cleanup
        pg.quit()
        # Immediately terminate the app
        sys.exit()

    @staticmethod
    def draw_square_annulus():
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(30.0, 30.0, 0.0)  # Vertex 0
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(10.0, 10.0, 0.0)  # Vertex 1
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(70.0, 30.0, 0.0)  # Vertex 2
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(90.0, 10.0, 0.0)  # Vertex 3
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(70.0, 70.0, 0.0)  # Vertex 4
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(90.0, 90.0, 0.0)  # Vertex 5
        glColor3f(0.0, 1.0, 1.0)
        glVertex3f(30.0, 70.0, 0.0)  # Vertex 6
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(10.0, 90.0, 0.0)  # Vertex 7
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(30.0, 30.0, 0.0)  # Vertex 8 = Vertex 0
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(10.0, 10.0, 0.0)  # Vertex 9 = Vertex 1
        glEnd()

        glFlush()
