#!/usr/bin/env python3
"""Modulo que define la clase Square que hereda de Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado a partir de la clase Rectangle."""

    def __init__(self, size):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): Tamano del lado del cuadrado.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
