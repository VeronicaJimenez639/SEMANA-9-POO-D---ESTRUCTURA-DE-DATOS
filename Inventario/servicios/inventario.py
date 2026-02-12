# servicios/inventario.py
# Clase "Inventario": contiene la lógica de gestión usando una LISTA como estructura principal.

from modelos.producto import Producto


class Inventario:
    def __init__(self):
        # Constructor: inicializa el inventario con una lista vacía de productos.
        self.__productos: list[Producto] = []

    def _buscar_indice_por_id(self, producto_id: int) -> int:
        """
        Método interno para ubicar un producto por ID en la lista.
        Retorna el índice si existe, o -1 si no existe.
        """
        for i, producto in enumerate(self.__productos): 
            if producto.get_id() == producto_id:
                return i
        return -1
    
    def agregar_producto(self, producto: Producto) -> bool:
        """
        Agrega un producto validando que el ID no esté repetido.
        Retorna True si se agrega, False si el ID ya existe.
        """
        indice = self._buscar_indice_por_id(producto.get_id()) 
        if indice != -1:
            print("Error: El ID del producto ya existe.")
            return False
        self.__productos.append(producto)
        return True