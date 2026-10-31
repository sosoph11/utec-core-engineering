#!/usr/bin/env python3
"""Módulo que define una clase Square con validación de tamaño."""


class Square:
    """Representa un cuadrado con validación de tamaño."""

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
