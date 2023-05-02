#!/usr/bin/python3

import argparse
from multiprocessing import Process, Pipe

parser = argparse.ArgumentParser(description='Espejar lineas de un archivo de texto.')
parser.add_argument('-f', '--file', help='es el archivo de texto a leer.')
args = parser.parse_args()

file = args.file

def mirror(pipe, line):
    enil = line[::-1]
    pipe.send(enil)
    pipe.close()

try:
    with open(file) as f:
        lines = f.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].strip('\n')

    processes = []
    for line in lines:
        p, c = Pipe()
        process = Process(target=mirror, args=(c, line))
        process.start()
        processes.append((process, p))
    
    for process, pipe in processes:
        process.join()
        data = pipe.recv()
        print(data)

except IOError:
    print(f'Error al abrir el archivo: {file}')
