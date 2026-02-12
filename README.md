# Sistema de Gestión de Inventarios (Python)

Programa en consola para administrar el inventario de una tienda. Permite **añadir**, **eliminar**, **actualizar**, **buscar por ID** y **listar** productos.

## Estructura del proyecto
- `modelos/producto.py`: clase `Producto` (ID, nombre, cantidad, precio) con getters/setters.
- `servicios/inventario.py`: clase `Inventario` con la lógica de gestión usando una lista.
- `main.py`: menú interactivo en consola.

## Cómo ejecutar
1. Abre la terminal en la carpeta del proyecto.
2. Ejecuta:
   ```bash
   python main.py
