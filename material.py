from os import PathLike

import pygame as pg
from OpenGL.GL import *


class Material:
    def __init__(self, filename: str | PathLike[str]):
        self.texture = glGenTextures(1)
        # Make this texture the current texture
        glBindTexture(GL_TEXTURE_2D, self.texture)

        # Handles what happens when the coordinates given fall out of
        # the s,t coordinate space (where everything lies between 0 and 1)
        # Here, we will repeat the texture when either s or t is over the bounds
        # hence the GL_REPEAT
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        # Here, we are handling what happens if the surface to display the
        # texture is not the same size as the intrinsic size of the texture
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Load our texture (in this case, an image) using pygame
        image = pg.image.load(filename).convert_alpha()
        image_width, image_height = image.get_rect().size

        # Convert image to a format that OpenGL can understand. Flipped is True
        # because OpenGL reads images differently from how Pygame does
        image_data = pg.image.tostring(image, "RGBA", True)

        glTexImage2D(GL_TEXTURE_2D,
                     0,
                     GL_RGBA,
                     image_width,
                     image_height,
                     0,
                     GL_RGBA,
                     GL_UNSIGNED_BYTE,
                     image_data)

        # Generates smaller images
        # for when the camera is far from the texture
        glGenerateMipmap(GL_TEXTURE_2D)

        # Make it available for use in immediate (compatibility) mode
        glEnable(GL_TEXTURE_2D)

    def use(self):
        """
        This function (as declared now) may be redundant as we have already
        run the same line in the __init__ method
        """
        # Make our texture the active texture
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def destroy(self):
        """Delete the memory allocated for the texture"""
        glDisable(GL_TEXTURE_2D)
        glDeleteTextures(1, (self.texture,))
