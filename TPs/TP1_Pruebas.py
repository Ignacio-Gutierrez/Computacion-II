#!/usr/bin/python3

import os
import argparse

parser = argparse.ArgumentParser(description='Espejar lineas de un archivo de texto.')
parser.add_argument('-f', '--file', help='es el archivo de texto a leer.')
args = parser.parse_args()

file = args.file

r2, w2 = os.pipe()

try:
    with open(file) as f:
        lines = f.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].rstrip('\n')

        for i in range(1, len(lines)):
            if not '\n' in lines[i]:
                lines[i] += '\n'

    for line in lines:

        r1, w1 = os.pipe()

        pid = os.fork()
        if pid == 0:  #Hijo
            print(f'Hijo:{os.getpid()} -de:{os.getppid()} RECIBE')
            os.close(w1)
            data = os.read(r1, 1024)
            data_d = data.decode()[::-1]
            os.close(r1)

            print(f'Hijo:{os.getpid()} -de:{os.getppid()} MANDA')
            os.close(r2)
            os.write(w2, data_d.encode())
            os.close(w2)

            exit(0)  # Salir del proceso hijo

        elif pid < 0:  #Error
            print('Error al hacer fork')
            exit(1)  # Salir con código de error

        else:  #Padre
            print(f'Padre:{os.getpid()} MANDA')
            os.close(r1)
            os.write(w1, line.encode())
            os.close(w1)

            os.waitpid(pid, 0)

except IOError:
    print(f'Error al abrir el archivo: {file}')

os.close(w2)

print(f'Padre:{os.getpid()} IMPRIME')
while True:
    data = os.read(r2, 1024)
    if not data:
        break
    print(data.decode())

os.close(r2)