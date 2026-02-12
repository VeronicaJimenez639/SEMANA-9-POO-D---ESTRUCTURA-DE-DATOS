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
    
    # Setters
    # Estos métodos permiten modificar los atributos privados del producto.
    # Se usan para validar los datos antes de asignarlos a los atributos.
    
    def set_id(self, producto_id: int) -> None:
        # ID debe ser entero positivo (y será único en Inventario).
        if not isinstance(producto_id, int) or producto_id <= 0:
            raise ValueError("El ID debe ser un entero positivo.")
        self.__id = producto_id

    def set_nombre(self, nombre: str) -> None:
        # Nombre no debe ser vacío.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()

    def set_cantidad(self, cantidad: int) -> None:
        # Cantidad debe ser entero >= 0.
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero mayor o igual a 0.")
        self.__cantidad = cantidad

    def set_precio(self, precio: float) -> None:  
        # Precio debe ser número >= 0.
        if not isinstance(precio, (int, float)) or float(precio) < 0:
            raise ValueError("El precio debe ser un número mayor o igual a 0.")
        self.__precio = float(precio)    


