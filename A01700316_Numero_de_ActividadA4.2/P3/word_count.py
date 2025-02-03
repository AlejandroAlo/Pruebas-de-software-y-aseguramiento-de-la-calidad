"""Programa para contar las palabras dentro
de un archivo de texto """
import sys
import time
import os
import re

def leer_palabras_desde_archivo(nombre_archivo):
    """Lee palabras desde un archivo y maneja datos inválidos."""
    palabras = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras.extend(re.findall(r'\b\w+\b', linea.lower()))
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        sys.exit(1)
    return palabras

def contar_frecuencia_palabras(palabras):
    """Cuenta la frecuencia de cada palabra en la lista."""
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def guardar_resultados_en_archivo(resultados, nombre_archivo):
    """Guarda los resultados en un archivo."""
    nombre_base = os.path.splitext(nombre_archivo)[0]
    nombre_salida = f"WordCountResults_{nombre_base}.txt"
    with open(nombre_salida, "w", encoding='utf-8') as archivo:
        archivo.write(resultados)

def main():
    """Función principal para contar palabras en un archivo."""
    if len(sys.argv) != 2:
        print("Uso: python word_count.py archivoConDatos.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    tiempo_inicio = time.time()
    palabras = leer_palabras_desde_archivo(archivo_entrada)

    if not palabras:
        print("No se encontraron palabras válidas en el archivo.")
        sys.exit(1)

    frecuencia_palabras = contar_frecuencia_palabras(palabras)

    resultados = "Conteo de palabras:\n"
    for palabra, frecuencia in sorted(frecuencia_palabras.items()):
        resultados += f"{palabra}: {frecuencia}\n"

    tiempo_transcurrido = time.time() - tiempo_inicio
    resultados += f"Tiempo Transcurrido: {tiempo_transcurrido:.6f} segundos\n"

    print(resultados)
    guardar_resultados_en_archivo(resultados, archivo_entrada)

if __name__ == "__main__":
    main()
