#!/usr/bin/env python3
"""Módulo que define una clase Square con cálculo de área."""


class Square:
    """Representa un cuadrado con tamaño y cálculo de área."""

    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): Tamaño del lado del cuadrado (por defecto es 0).

        Raises:
            TypeError: Si size no es un entero.
            ValueError: Si size es menor que 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcula el área del cuadrado actual.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size ** 2
