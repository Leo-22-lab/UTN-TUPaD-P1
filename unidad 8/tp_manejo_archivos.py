# productos.py
import os
from pathlib import Path

NOMBRE_ARCHIVO = "productos.txt"


def leer_entero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print("Ingrese un número entero válido.")


def leer_flotante(mensaje):
    while True:
        valor = input(mensaje).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("⚠️ Ingrese un precio válido (ej: 120.5).")


def normalizar_nombre(nombre):
    return " ".join(nombre.strip().lower().split())


def inicializar_archivo():
    """Crea el archivo con 3 productos si no existe."""
    if not Path(NOMBRE_ARCHIVO).exists():
        inicial = [
            ("Lapicera", 120.5, 30),
            ("Cuaderno", 250.0, 50),
            ("Resaltador", 85.75, 20)
        ]
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
            for nombre, precio, cantidad in inicial:
                f.write(f"{nombre},{precio},{cantidad}\n")
        print(f"Se creó '{NOMBRE_ARCHIVO}' con productos iniciales.")


def leer_lineas_archivo():
    """Lee el archivo y devuelve lista de líneas (sin \n)."""
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
        lineas = [linea.strip() for linea in f if linea.strip()]
    return lineas


def parsear_linea(linea):
    """Convierte 'nombre,precio,cantidad' -> (nombre, float(precio), int(cantidad))."""
    partes = [p.strip() for p in linea.split(",")]
    if len(partes) != 3:
        return None  
    nombre = partes[0]
    try:
        precio = float(partes[1].replace(",", "."))
        cantidad = int(partes[2])
    except ValueError:
        return None
    return nombre, precio, cantidad


def cargar_productos_desde_archivo():
    """Devuelve lista de diccionarios [{'nombre':..., 'precio':..., 'cantidad':...}, ...]"""
    productos = []
    lineas = leer_lineas_archivo()
    for linea in lineas:
        p = parsear_linea(linea)
        if p is None:
            print(f"⚠️ Línea ignorada (formato incorrecto): {linea}")
            continue
        nombre, precio, cantidad = p
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    return productos


def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def agregar_producto_al_archivo(nombre, precio, cantidad):
    with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{precio},{cantidad}\n")


def buscar_producto_por_nombre(productos, nombre_buscar):
    nombre_norm = normalizar_nombre(nombre_buscar)
    for p in productos:
        if normalizar_nombre(p["nombre"]) == nombre_norm:
            return p
    return None


def guardar_productos_en_archivo(productos):
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Se guardaron los productos actualizados en el archivo.")


def main():
    inicializar_archivo()
    productos = cargar_productos_desde_archivo()
    print("\n--- Productos actuales ---")
    mostrar_productos(productos)

    respuesta = input("\n¿Desea agregar un nuevo producto? (s/n): ").strip().lower()
    while respuesta == "s":
        nombre = input("Nombre: ").strip()
        while not nombre:
            nombre = input("Nombre no puede estar vacío. Ingrese Nombre: ").strip()

        existente = buscar_producto_por_nombre(productos, nombre)
        precio = leer_flotante("Precio: ")
        cantidad = leer_entero("Cantidad: ")

        if existente:
            print(f"El producto '{existente['nombre']}' ya existe en el catálogo.")
            actualizar = input("¿Desea sumar la cantidad ingresada al stock existente? (s/n): ").strip().lower()
            if actualizar == "s":
                existente["cantidad"] += cantidad
                existente["precio"] = precio  
                print("Stock actualizado en la lista.")
            else:
                productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                print("Se agregó como nuevo producto (mismo nombre duplicado).")
        else:
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            print("Producto agregado a la lista.")

        agregar_producto_al_archivo(nombre, precio, cantidad)
        print("Producto agregado al archivo (modo append).")

        respuesta = input("\n¿Desea agregar otro producto? (s/n): ").strip().lower()

    buscar = input("\nIngrese el nombre de un producto para buscar (o Enter para omitir): ").strip()
    if buscar:
        encontrado = buscar_producto_por_nombre(productos, buscar)
        if encontrado:
            print("Producto encontrado:")
            print(f"Nombre: {encontrado['nombre']}")
            print(f"Precio: ${encontrado['precio']}")
            print(f"Cantidad: {encontrado['cantidad']}")
        else:
            print(" El producto no existe.")

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()

