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
    
    def eliminar_producto(self, producto_id: int) -> bool:
        """
        Elimina un producto por ID.
        Retorna True si se elimina, False si no existe.
        """
        indice = self._buscar_indice_por_id(producto_id)
        if indice == -1:
            print("Error: No existe un producto con ese ID.")
            return False

        self.__productos.pop(indice)
        return True

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None) -> bool:
        """
        Actualiza cantidad y/o precio de un producto por ID.
        Retorna True si actualiza, False si no existe.
        """
        indice = self._buscar_indice_por_id(producto_id)
        if indice == -1:
            print("Error: No existe un producto con ese ID.")
            return False

        producto = self.__productos[indice]  

        # Solo se actualiza lo que el usuario envía (cantidad, precio o ambos)
        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad) 

        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        return 
    
    def buscar_por_id(self, producto_id: int):
        """
        Busca un producto por su ID.
        Retorna el producto si existe, o None si no existe.
        """
        indice = self._buscar_indice_por_id(producto_id)
        if indice == -1:
            print("Error: No existe un producto con ese ID.")
            return None
        return self.__productos[indice]
    
    def listar_productos(self):
        """
        Retorna una copia de la lista de productos para mostrar en el main.
        """
        return self.__productos.copy() # Devuelve una copia para no modificar la lista original del inventario.
    

