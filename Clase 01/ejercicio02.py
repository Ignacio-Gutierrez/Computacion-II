#!/usr/bin/python3

import argparse

argpar = argparse.ArgumentParser(description='Repetidor de cadenas de texto n veces')

argpar.add_argument('-s', '--string', type=str, help='debe ser la cadena de texto a repetir, n veces')
argpar.add_argument('-n', type=int, help='debe ser el número de veces que se debe repetir, la cadena de texto')

args = argpar.parse_args()

for i in range(args.n):
    print(args.string)