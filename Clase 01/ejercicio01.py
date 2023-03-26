#!/usr/bin/python3

import argparse

argpar = argparse.ArgumentParser(description='Generador de números impares')

argpar.add_argument('n', type=int, help='debe ser un número entero positivo')

args = argpar.parse_args()

if args.n <= 0:
    print('n debe ser un número entero positivo')
else:
    odd = [2*i+1 for i in range(args.n)]
    print(odd)