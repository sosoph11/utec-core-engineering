#!/usr/bin/env python3
"""Modulo que define la clase Rectangle con area y representacion en texto."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectangulo completo basado en BaseGeometry."""

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

    def area(self):
        """Calcula el area del rectangulo.

        Returns:
            int: El area resultante.
        """
        return self.__width * self.__height

    def __str__(self):
        """Representacion legible en cadena de caracteres del rectangulo.

        Returns:
            str: Descripcion en formato [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
