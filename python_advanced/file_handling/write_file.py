#!/usr/bin/env python3
"""Módulo que contiene la función write_file."""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo UTF-8 y retorna los caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
