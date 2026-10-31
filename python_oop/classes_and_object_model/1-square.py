#!/usr/bin/env python3
"""Módulo que define una clase Square con tamaño privado."""


class Square:
    """Representa un cuadrado con un tamaño específico."""

    def __init__(self, size):
        """Inicializa un nuevo cuadrado.

        Args:
            size: Tamaño del lado del cuadrado.
        """
        self.__size = size
