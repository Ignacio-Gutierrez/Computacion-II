#!/usr/bin/python3

import os
import argparse

parser = argparse.ArgumentParser(description='Contador de palabras por línea.')
parser.add_argument('file', help='es el f de texto a leer.')
args = parser.parse_args()

r, w = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(w)
    data = os.read(r, 1024)
    file = data.decode()
    words = file.split('\n')
    count = 0
    f = 1
    for w in words:
        if w:
            count = len(w.split())
            print(f'La linea {f}, "{w}", tiene {count} palabras')
            f += 1

    #print(f'La linea {count} "{w_l}" tiene {n_words} palabras.')
    os.close(r)
else:
    os.close(r)
    with open(args.file, "r") as f:
        for line in f:
            os.write(w, line.encode())
    os.close(w)