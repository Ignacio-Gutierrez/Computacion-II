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
    fifo = open(fifo_00, 'w')
    mat0 = str(matrix1[0]*matrix2[0]+matrix1[2]*matrix2[1])
    fifo.write(mat0 + '\n'  )
    fifo.close()

def child_02():
    fifo = open(fifo_00, 'a')
    mat1 = str(matrix1[1]*matrix2[0]+matrix1[3]*matrix2[1])
    fifo.write(mat1 + '\n')
    fifo.close()
    
def child_03():
    fifo = open(fifo_00, 'a')
    mat2 = str(matrix1[0]*matrix2[2]+matrix1[2]*matrix2[3])
    fifo.write(mat2 + '\n')
    fifo.close()

def child_04():
    fifo = open(fifo_00, 'a')
    mat3 = str(matrix1[1]*matrix2[2]+matrix1[3]*matrix2[3])
    fifo.write(mat3 + '\n')
    fifo.close()

def parent():
    fifo_in = open(fifo_00, 'r')
    print(fifo_in.read())

if not os.path.exists(fifo_00):
    os.mkfifo(fifo_00)

pid = os.fork()

if pid != 0:
    parent()
else:
    child_01()
    child_02()
    child_03()
    child_04()