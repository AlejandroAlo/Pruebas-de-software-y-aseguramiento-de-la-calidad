"""Programa para convertir numeros a binario
y hexadecimal"""

import sys
import time
import os
import re

def leer_numeros_desde_archivo(nombre_archivo):
    """Lee números desde un archivo y maneja datos inválidos."""
    numeros = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                valor = linea.strip()
                if re.match(r'^-?\d+$', valor):  # Verifica número válido (positivo o negativo)
                    numeros.append(int(valor))
                else:
                    print(f"Advertencia: Datos inválidos detectados y omitidos -> {valor}")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        sys.exit(1)
    return numeros

def convertir_a_binario(numero):
    """Convierte un número a su representación binaria con signo explícito."""
    if numero == 0:
        return '0'
    signo = '-' if numero < 0 else ''
    numero = abs(numero)
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return signo + binario

def convertir_a_hexadecimal(numero):
    """Convierte un número a su representación hexadecimal con signo explícito."""
    if numero == 0:
        return '0'
    signo = '-' if numero < 0 else ''
    numero = abs(numero)
    hexadecimal = ''
    hex_chars = '0123456789ABCDEF'
    while numero > 0:
        hexadecimal = hex_chars[numero % 16] + hexadecimal
        numero //= 16
    return signo + hexadecimal

def guardar_resultados_en_archivo(resultados, nombre_archivo):
    """Guarda los resultados de la conversión en un archivo."""
    nombre_base = os.path.splitext(nombre_archivo)[0]
    nombre_salida = f"ConvertionResults_{nombre_base}.txt"
    with open(nombre_salida, "w", encoding='utf-8') as archivo:
        archivo.write(resultados)

def main():
    """Función principal para convertir números a binario y hexadecimal desde un archivo."""
    if len(sys.argv) != 2:
        print("Uso: python convert_numbers.py archivoConDatos.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    tiempo_inicio = time.time()
    numeros = leer_numeros_desde_archivo(archivo_entrada)

    if not numeros:
        print("No se encontraron números válidos en el archivo.")
        sys.exit(1)

    resultados = "Resultados de conversión:\n"
    for numero in numeros:
        binario = convertir_a_binario(numero)
        hexadecimal = convertir_a_hexadecimal(numero)
        resultados += f"Número: {numero}, Binario: {binario}, Hexadecimal: {hexadecimal}\n"

    tiempo_transcurrido = time.time() - tiempo_inicio
    resultados += f"Tiempo Transcurrido: {tiempo_transcurrido:.6f} segundos\n"

    print(resultados)
    guardar_resultados_en_archivo(resultados, archivo_entrada)

if __name__ == "__main__":
    main()
