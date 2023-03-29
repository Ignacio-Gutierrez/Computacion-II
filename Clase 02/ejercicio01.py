#!/usr/bin/python3

import argparse
import os
import cmath

parser= argparse.ArgumentParser(description='Calcular raices')

parser.add_argument('n', type=int, help='debe ser un número')
parser.add_argument('-r', '--root', action='store_true', help='es la opción para hallar, también, la raíz negativa')

args = parser.parse_args()


r_ans = cmath.sqrt(args.n)

if args.root:
    rt = os.fork()
                                   
    if rt > 0:
        print(f'La raíz positiva es: {r_ans}')
        print('SOY PADRE (PID: %d -- PPID: %d)' % (os.getpid(), os.getppid()))

    elif rt == 0:
        print(f'La raíz negativa es: {-r_ans}')
        print('SOY HIJO (PID: %d -- PPID: %d)' % (os.getpid(), os.getppid()))

if not args.root:
    print(f'La raíz positiva es: {r_ans}')




# Realizar un programa que implemente fork junto con el parseo de argumentos. 
# Deberá realizar relizar un fork si -f aparece entre las opciones al ejecutar el programa.
# El proceso padre deberá calcular la raiz cuadrada positiva de un numero y el hijo la raiz negativa.