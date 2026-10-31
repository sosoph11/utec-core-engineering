#!/usr/bin/env python3
"""Módulo que define una clase Square capaz de imprimirse."""


class Square:
    """Representa un cuadrado con tamaño, área e impresión."""

    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): Tamaño del lado del cuadrado (por defecto es 0).
        """
        self.size = size

    @property
    def size(self):
        """Obtiene el tamaño actual del cuadrado.

        Returns:
            int: El tamaño del lado del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado validando tipo y valor.

        Args:
            value (int): Nuevo tamaño del lado del cuadrado.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula el área del cuadrado actual.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime en stdout el cuadrado con el carácter '#'."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
