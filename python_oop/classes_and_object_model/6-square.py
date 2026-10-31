#!/usr/bin/env python3
"""Módulo que define una clase Square con tamaño y posición."""


class Square:
    """Representa un cuadrado con tamaño, posición e impresión."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): Tamaño del lado del cuadrado (por defecto es 0).
            position (tuple): Coordenadas horizontales y verticales.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Obtiene la posición del cuadrado.

        Returns:
            tuple: Coordenadas de posición del cuadrado.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición del cuadrado validando formato y valores.

        Args:
            value (tuple): Tupla de 2 enteros positivos (>= 0).

        Raises:
            TypeError: Si value no cumple con las restricciones de posición.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(type(n) is int for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calcula el área del cuadrado actual.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime en stdout el cuadrado respetando tamaño y posición."""
        print(self.pos_print(), end="")

    def pos_print(self):
        """Genera la representación en cadena del cuadrado con su posición.

        Returns:
            str: Texto representativo del cuadrado.
        """
        if self.__size == 0:
            return "\n"

        result = []
        for _ in range(self.__position[1]):
            result.append("\n")

        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size + "\n")

        return "".join(result)

    def __str__(self):
        """Define la representación formal en string del objeto cuadrado.

        Returns:
            str: Texto que representa visualmente el cuadrado.
        """
        return self.pos_print()[:-1]
