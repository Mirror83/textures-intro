import numpy as np
from OpenGL.GL import *


class Triangle:
    def __init__(self):
        # x, y, z, r, g, b (for each row)
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,  # Bottom-left
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,  # Bottom-right
            0.5, 0.5, 0.0, 0.0, 0.0, 1.0    # Top-center

        )

        # To change the data to a C-style array that OpenGL can work with
        # Type is also specified to 32-bit floating point numbers
        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 3
        self.vao = glGenVertexArrays(1)  # vao = vertex array object
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    # Cleans up any memory allocated during the createion of the triangle
    def destroy(self):
        glDeleteVertexArrays(1, [self.vao])
        glDeleteVertexArrays(1, [self.vbo])
