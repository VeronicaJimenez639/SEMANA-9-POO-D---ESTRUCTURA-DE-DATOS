# modelos/producto.py
# Clase Producto: representa la información de un producto (ID, nombre, cantidad y precio) que el inventario administra.
# Contiene atributos y métodos getters/setters.

class Producto:
    def __init__(self, producto_id: int, nombre: str, cantidad: int, precio: float): 
        # Constructor: crea un Producto y guarda sus datos usando setters.
        # Se usan setters para validar ID, nombre, cantidad y precio desde el inicio.
        self.set_id(producto_id)  
        self.set_nombre(nombre)   
        self.set_cantidad(cantidad)  
        self.set_precio(precio)    

    # Getters
    # Estos métodos permiten leer los atributos privados del producto.
    # Se usan para mantener encapsulación (no acceder directamente a __id, __nombre, etc.)

    def get_id(self) -> int:    
        return self.__id     # Devuelve el ID del producto (entero)

    def get_nombre(self) -> str:
        return self.__nombre  # Devuelve el nombre del producto (cadena)

    def get_cantidad(self) -> int:
        return self.__cantidad  # Devuelve la cantidad disponible del producto (entero)

    def get_precio(self) -> float:
        return self.__precio # Devuelve el precio del producto (flotante)


