#!/usr/bin/env python3
"""Modulo que define la clase Square con representacion en cadena personalizada."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado con metodo de impresion personalizado."""

    def __init__(self, size):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): Tamano del lado del cuadrado.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Representacion legible en cadena de caracteres del cuadrado.

        Returns:
            str: Descripcion en formato [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
