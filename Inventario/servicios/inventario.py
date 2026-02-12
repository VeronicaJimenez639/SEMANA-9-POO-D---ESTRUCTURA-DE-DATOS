# servicios/inventario.py
# Clase "Inventario": contiene la lógica de gestión usando una LISTA como estructura principal.

from modelos.producto import Producto


class Inventario:
    def __init__(self):
        # Constructor: inicializa el inventario con una lista vacía de productos.
        self.__productos: list[Producto] = []