#!/usr/bin/env python3
"""Modulo que define la clase Rectangle que hereda de BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectangulo validado por BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa un nuevo rectangulo.

        Args:
            width (int): Ancho del rectangulo.
            height (int): Altura del rectangulo.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
