"""Programa para calcular las ventas
 totales de los productos"""
import sys
import time
import os
import json


def leer_json(nombre_archivo):
    """Lee un archivo JSON y maneja posibles errores."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(
            f"Error: El archivo {nombre_archivo} no contiene un JSON válido."
            )
        sys.exit(1)


def convertir_catalogo_a_diccionario(catalogo):
    """Convierte una lista de productos en un diccionario
    con el título como clave y el precio como valor."""
    catalogo_diccionario = {}
    for producto in catalogo:
        titulo = producto.get("title")
        precio = producto.get("price")
        if titulo and precio is not None:
            catalogo_diccionario[titulo] = precio
    return catalogo_diccionario


def calcular_total_ventas(catalogo_precios, registro_ventas):
    """Calcula el total de ventas considerando los precios del catálogo."""
    total = 0.0
    ventas_detalle = []
    for venta in registro_ventas:
        producto = venta.get("Product")
        cantidad = venta.get("Quantity", 0)
        precio = catalogo_precios.get(producto)
        if precio is None:
            print(f"Advertencia: El producto '{producto}' no tiene un precio "
                  f"en el catálogo."
                  )
            continue
        costo = precio * cantidad
        ventas_detalle.append(
            f"{producto}: {cantidad} x {precio:.2f} = {costo:.2f}"
            )
        total += costo
    return total, ventas_detalle


def guardar_resultados_en_archivo(resultados, archivo_ventas):
    """Guarda los resultados en un archivo, agregando el
    nombre del archivo de ventas al nombre del archivo de salida."""
    nombre_base = os.path.splitext(os.path.basename(archivo_ventas))[0]
    nombre_salida = f"SalesResults_{nombre_base}.txt"
    with open(nombre_salida, "w", encoding='utf-8') as archivo:
        archivo.write(resultados)


def main():
    """Función principal para calcular el total de ventas."""
    if len(sys.argv) != 3:
        print("Usar: python compute_sales.py "
              "priceCatalogue.json salesRecord.json")
        sys.exit(1)

    archivo_catalogo = sys.argv[1]
    archivo_ventas = sys.argv[2]
    tiempo_inicio = time.time()

    catalogo_lista = leer_json(archivo_catalogo)
    registro_ventas = leer_json(archivo_ventas)

    if (not isinstance(catalogo_lista, list) or
            not isinstance(registro_ventas, list)):
        print("Error: El formato de los archivos JSON no es válido.")
        sys.exit(1)

    catalogo_precios = convertir_catalogo_a_diccionario(catalogo_lista)
    total, detalle_ventas = calcular_total_ventas(
        catalogo_precios, registro_ventas)

    resultados = "Resumen de Ventas:\n"
    resultados += "\n".join(detalle_ventas)
    resultados += f"\n\nTotal de ventas: {total:.2f}\n"

    tiempo_transcurrido = time.time() - tiempo_inicio
    resultados += f"Tiempo Transcurrido: {tiempo_transcurrido:.6f} segundos\n"

    print(resultados)
    guardar_resultados_en_archivo(resultados, archivo_ventas)


if __name__ == "__main__":
    main()
