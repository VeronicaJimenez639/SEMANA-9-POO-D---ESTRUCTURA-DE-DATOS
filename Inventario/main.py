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





