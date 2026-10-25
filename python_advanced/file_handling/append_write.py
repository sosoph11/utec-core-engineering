#!/usr/bin/env python3
"""Módulo que contiene la función append_write."""


def append_write(filename="", text=""):
    """Añade texto al final de un archivo UTF-8."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
