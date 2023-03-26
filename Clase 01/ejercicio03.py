#!/usr/bin/python3

import argparse
import sys

parser = argparse.ArgumentParser(description='Contador de palabras, líneas y longitud promedio de palabras en un archivo de texto.')

parser.add_argument('file', help='es el archivo de texto a leer.')
parser.add_argument('average', nargs='?', help='es la opción para imprimir la longitud promedio de las palabras.', default=False)
parser.add_argument('-o', '--output', help='es el archivo para escribir los errores.', default='errors.log')

args = parser.parse_args()

try:
    with open(args.file) as f:
        content = f.read()
except FileNotFoundError:
    sys.stderr = open(args.output, 'a')
    print(f'No se encontró el archivo {args.file}.', file=sys.stderr)
    sys.stderr.close()
    

words = content.split()
lines = content.split('\n')
l_words = len(words)
l_lines = len(lines)
print(f'El número de palabras es: {l_words}')
print(f'El número de líneas es: {l_lines}')

if args.average:
    length = [len(p) for p in words]
    average = sum(length) / l_words
    print(f'La longitud promedio de las palabras es: {round(average)}')