"""Programa que calcula las estadisticas básicas de 
una lista de números
"""

import sys
import time
import os
import re
from collections import Counter

def leer_numeros_desde_archivo(nombre_archivo):
    """Lee números desde un archivo y maneja datos inválidos."""
    numeros = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                valor = linea.strip()
                if re.match(r'^-?\d+(\.\d+)?$', valor):  # Verifica si es un número válido
                    numeros.append(float(valor))
                else:
                    print(f"Advertencia: Datos inválidos detectados y omitidos -> {valor}")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        sys.exit(1)
    return numeros

def calcular_media(numeros):
    """Calcula la media de una lista de números."""
    return sum(numeros) / len(numeros) if numeros else 0

def calcular_mediana(numeros):
    """Calcula la mediana de una lista de números."""
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2
    return numeros_ordenados[medio]

def calcular_moda(numeros):
    """Calcula la moda de una lista de números."""
    conteo = Counter(numeros)
    max_conteo = max(conteo.values())
    modas = [num for num, frecuencia in conteo.items() if frecuencia == max_conteo]
    return modas if len(modas) < len(numeros) else []

def calcular_varianza(numeros, media):
    """Calcula la varianza de una lista de números."""
    return sum((x - media) ** 2 for x in numeros) / len(numeros) if numeros else 0

def calcular_desviacion_estandar(varianza):
    """Calcula la desviación estándar basada en la varianza."""
    return varianza ** 0.5

def guardar_resultados_en_archivo(resultados, nombre_archivo):
    """Guarda los resultados estadísticos en un archivo con un sufijo único."""
    nombre_base = os.path.splitext(nombre_archivo)[0]
    nombre_salida = f"{nombre_base}_estadisticas.txt"
    with open(nombre_salida, "w", encoding='utf-8') as archivo:
        archivo.write(resultados)

def main():
    """Función principal para calcular estadísticas desde un archivo."""
    if len(sys.argv) != 2:
        print("Uso: python compute_Statistics.py archivoConDatos.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    tiempo_inicio = time.time()
    numeros = leer_numeros_desde_archivo(archivo_entrada)

    if not numeros:
        print("No se encontraron números válidos en el archivo.")
        sys.exit(1)

    cantidad_elementos = len(numeros)
    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    varianza = calcular_varianza(numeros, media)
    desviacion_estandar = calcular_desviacion_estandar(varianza)
    tiempo_transcurrido = time.time() - tiempo_inicio

    resultados = (f"Estadísticas Descriptivas:\n"
                  f"Cantidad de elementos: {cantidad_elementos}\n"
                  f"Media: {media}\n"
                  f"Mediana: {mediana}\n"
                  f"Moda: {moda if moda else 'Sin moda única'}\n"
                  f"Varianza: {varianza}\n"
                  f"Desviación Estándar: {desviacion_estandar}\n"
                  f"Tiempo Transcurrido: {tiempo_transcurrido:.6f} segundos\n")

    print(resultados)
    guardar_resultados_en_archivo(resultados, archivo_entrada)

if __name__ == "__main__":
    main()
