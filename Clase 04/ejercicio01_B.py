#!/usr/bin/python3

#python3 ejercicio01_B.py -m1 1 2 3 4 -m2 1 2 3 4

import os
import argparse

parser = argparse.ArgumentParser(description='Ingrese dos matrices 2x2')
parser.add_argument('-m1', nargs=4, type=int, metavar=('a', 'b', 'c', 'd'), help='matriz 1 en orden a b c d')
parser.add_argument('-m2', nargs=4, type=int, metavar=('e', 'f', 'g', 'h'), help='matriz 2 en orden e f g h')

args = parser.parse_args()
matrix1 = args.m1
matrix2 = args.m2

fifo_00 = '/tmp/my_fifo.'

def child_01():
    fifo = open(fifo_00, 'a')
    mat0 = '00:' + str(matrix1[0]*matrix2[0]+matrix1[2]*matrix2[1])
    fifo.write(mat0 + '\n')
    fifo.close()

def child_02():
    fifo = open(fifo_00, 'a')
    mat1 = '01:' +  str(matrix1[1]*matrix2[0]+matrix1[3]*matrix2[1])
    fifo.write(mat1 + '\n')
    fifo.close()
    
def child_03():
    fifo = open(fifo_00, 'a')
    mat2 = '10:' +  str(matrix1[0]*matrix2[2]+matrix1[2]*matrix2[3])
    fifo.write(mat2 + '\n')
    fifo.close()

def child_04():
    fifo = open(fifo_00, 'a')
    mat3 = '11:' +  str(matrix1[1]*matrix2[2]+matrix1[3]*matrix2[3])
    fifo.write(mat3 + '\n')
    fifo.close()

def parent():
    fifo_in = open(fifo_00, 'r')

    data1 = str(fifo_in.readline().strip())
    data2 = str(fifo_in.readline().strip())
    data3 = str(fifo_in.readline().strip())
    data4 = str(fifo_in.readline().strip())

    data = [data1, data2, data3, data4]

    for d in data:
        if d[:3] == '00:':
            m00 = d[3:]
        elif d[:3] == '01:':
            m01 = d[3:]
        elif d[:3] == '10:':
            m10 = d[3:]
        elif d[:3] == '11:':
            m11 = d[3:]

    mat = [[m00,m01],[m10,m11]]

    for m in mat:
        print(m)

if not os.path.exists(fifo_00):
    os.mkfifo(fifo_00)


pid1 = os.fork()
if pid1 == 0:
    parent()

    pid2 = os.fork()
    if pid2 == 0:
        child_02()
    else:
        pid3 = os.fork()
        if pid3 == 0:
            child_03()
        else:
            pid4 = os.fork()
            if pid4 == 0:
                child_04()
else:
    child_01()