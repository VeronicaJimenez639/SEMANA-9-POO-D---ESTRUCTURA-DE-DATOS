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


def leer_float(mensaje: str, minimo=None) -> float:
    # Pide un número decimal y repite hasta que sea válido
    while True:
        try:
            valor = float(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"Debe ser un número >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingresa un número decimal (ej: 2.50).")


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


        elif opcion == 2:
            # Opción 2: eliminar un producto usando su ID
            producto_id = leer_int("ID del producto a eliminar: ", minimo=1)
            eliminado = inventario.eliminar_producto(producto_id)  # El inventario intenta eliminarlo y devuelve True/False según exista o no

            if eliminado:
                print("Producto eliminado correctamente.")

         
        elif opcion == 3:
            # Opción 3: actualizar un producto existente usando su ID
            producto_id = leer_int("ID del producto a actualizar: ", minimo=1)

            #El usuario elige qué datos actualizar (cantidad, precio o ambos)
            print("¿Qué deseas actualizar?")
            print("1) Cantidad")
            print("2) Precio")
            print("3) Ambos")
            sub_opcion = leer_int("Elige una opción (1-3): ", minimo=1)

            try:
                #Se inicializan en None para actualizar solo lo que el usuario elija
                nueva_cantidad = None
                nuevo_precio = None

                if sub_opcion == 1:
                    nueva_cantidad = leer_int("Nueva cantidad (>=0): ", minimo=0)
                elif sub_opcion == 2:
                    nuevo_precio = leer_float("Nuevo precio (>=0): ", minimo=0.0)
                elif sub_opcion == 3:
                    nueva_cantidad = leer_int("Nueva cantidad (>=0): ", minimo=0)
                    nuevo_precio = leer_float("Nuevo precio (>=0): ", minimo=0.0)
                else:
                    print("Opción inválida.")
                    continue # Regresa al menú principal

                # Llama al inventario para aplicar el cambio (retorna True/False)
                actualizado = inventario.actualizar_producto(producto_id, nueva_cantidad=nueva_cantidad, nuevo_precio=nuevo_precio)

                if actualizado:
                    print("Producto actualizado correctamente.")

            except ValueError as e:
                print(f"Error: {e}") # Captura errores de validación de cantidad negativa o precio inválido       

        elif opcion == 4:
            # Opción 4: buscar productos por nombre (permite escribir solo una parte del nombre)
            texto = leer_texto("Ingresa nombre o parte del nombre: ")

            # El inventario devuelve una lista con los productos que coinciden con la búsqueda
            encontrados = inventario.buscar_por_nombre(texto)

            # Muestra el resultado de la búsqueda en consola
            if not encontrados:
                print("No se encontraron productos con ese nombre.")
            else:
                print(f"Se encontraron {len(encontrados)} producto(s):")
                for producto in encontrados:
                    print(" -", producto)  # Imprime el producto usando __str__


        elif opcion == 5:
            # Opción 5: listar todos los productos del inventario
            productos = inventario.listar_productos()  # El inventario devuelve la lista de productos

            if not productos:
                print("El inventario está vacío.")
            else:
                print("Productos en inventario:")
                for producto in productos:
                    print(" -", producto)  









