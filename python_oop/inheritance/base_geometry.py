#!/usr/bin/env python3
"""Modulo que define la clase base BaseGeometry."""


class BaseGeometry:
    """Clase base para geometrias que define comportamiento comun."""

    def area(self):
        """Calcula el area de la figura geometrica.

        Raises:
            Exception: Indica que el calculo no esta implementado.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero mayor que cero.

        Args:
            name (str): Nombre del parametro a validar.
            value (int): Valor a validar.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor o igual a cero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
