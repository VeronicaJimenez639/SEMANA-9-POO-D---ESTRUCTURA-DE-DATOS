# main.py
# Menú en consola: pide datos al usuario y llama a los métodos del inventario.

from modelos.producto import Producto
from servicios.inventario import Inventario

def leer_int(mensaje: str, minimo=None) -> int:
    # Pide un número entero y repite hasta que sea válido
    while True:
        try:
            valor = int(input(mensaje).strip())  # Convierte la entrada a entero
            if minimo is not None and valor < minimo:
                print(f"Debe ser un número >= {minimo}.")  # Valida el mínimo permitido
                continue  # Vuelve a pedir el dato
            return valor  # Devuelve el entero validado
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")  # Si no es entero, vuelve a pedir


def leer_texto(mensaje: str) -> str:
    """Lee texto no vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("No puede estar vacío.")


def mostrar_menu() -> None:  # Muestra el menú de opciones al usuario
    print("\n" + "=" * 40)   # Imprime una línea de separación
    print("   SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("=" * 40)          
    print("1) Añadir producto")
    print("2) Eliminar producto")
    print("3) Actualizar producto")
    print("4) Buscar producto por nombre")
    print("5) Listar inventario")
    print("6) Salir")


def main() -> None:
    inventario = Inventario()  # Crea el inventario (inicia vacío)

    while True:
        # Bucle principal del programa: muestra el menú y ejecuta la opción elegida
        mostrar_menu()
        opcion = leer_int("Elige una opción (1-6): ", minimo=1)

        if opcion == 1:
            # Opción 1: registrar un nuevo producto (con validación de datos)
            try:
                producto_id = leer_int("ID (entero positivo): ", minimo=1)
                nombre = leer_texto("Nombre: ")
                cantidad = leer_int("Cantidad (>=0): ", minimo=0)
                precio = leer_float("Precio (>=0): ", minimo=0.0)

                # Crea el objeto Producto y lo envía al inventario para guardarlo
                producto = Producto(producto_id, nombre, cantidad, precio)
                agregado = inventario.agregar_producto(producto)

                if agregado:
                    print("Producto agregado correctamente.")
            except ValueError as e:
                # Captura errores de validación lanzados por los setters de Producto
                print(f"Error: {e}")
   





