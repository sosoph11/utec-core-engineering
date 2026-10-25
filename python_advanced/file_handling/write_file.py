#!/usr/bin/env python3
"""Módulo que contiene la función write_file."""


def write_file(filename="", text=""):
    """Escribe texto en un archivo UTF-8 y retorna caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
