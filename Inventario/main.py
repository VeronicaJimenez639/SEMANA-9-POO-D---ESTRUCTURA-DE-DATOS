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


