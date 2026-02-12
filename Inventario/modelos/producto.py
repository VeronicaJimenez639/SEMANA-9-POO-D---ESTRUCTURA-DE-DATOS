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


