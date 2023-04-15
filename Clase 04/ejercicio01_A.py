#!/usr/bin/python3

#python3 ejercicio01_A.py -m1 1 2 3 4 -m2 1 2 3 4

import os
import argparse

parser = argparse.ArgumentParser(description='Ingrese dos matrices 2x2')
parser.add_argument('-m1', nargs=4, type=int, metavar=('a', 'b', 'c', 'd'), help='matriz 1 en orden a b c d')
parser.add_argument('-m2', nargs=4, type=int, metavar=('e', 'f', 'g', 'h'), help='matriz 2 en orden e f g h')

args = parser.parse_args()
matrix1 = args.m1
matrix2 = args.m2

fifo_01 = '/tmp/fifo_01'
fifo_02 = '/tmp/fifo_02'
fifo_03 = '/tmp/fifo_03'
fifo_04 = '/tmp/fifo_04'

def child_01():
    fifo = open(fifo_01, 'w')
    mat0 = str(matrix1[0]*matrix2[0]+matrix1[2]*matrix2[1])
    fifo.write(mat0)
    fifo.close()

def child_02():
    fifo = open(fifo_02, 'w')
    mat1 = str(matrix1[1]*matrix2[0]+matrix1[3]*matrix2[1])
    fifo.write(mat1)
    fifo.close()
    
def child_03():
    fifo = open(fifo_03, 'w')
    mat2 = str(matrix1[0]*matrix2[2]+matrix1[2]*matrix2[3])
    fifo.write(mat2)
    fifo.close()

def child_04():
    fifo = open(fifo_04, 'w')
    mat3 = str(matrix1[1]*matrix2[2]+matrix1[3]*matrix2[3])
    fifo.write(mat3)
    fifo.close()

def parent():
    fifo_in_01 = open(fifo_01, 'r')
    fifo_in_02 = open(fifo_02, 'r')
    fifo_in_03 = open(fifo_03, 'r')
    fifo_in_04 = open(fifo_04, 'r')

    m1 = fifo_in_01.readline().rstrip()
    m2 = fifo_in_02.readline().rstrip()
    m3 = fifo_in_03.readline().rstrip()
    m4 = fifo_in_04.readline().rstrip()

    fifo_in_01.close()
    fifo_in_02.close()
    fifo_in_03.close()
    fifo_in_04.close()

    mat = [[m1,m2],[m3,m4]]

    for m in mat:
        print(m)

if not os.path.exists(fifo_01):
    os.mkfifo(fifo_01)
if not os.path.exists(fifo_02):
    os.mkfifo(fifo_02)
if not os.path.exists(fifo_03):
    os.mkfifo(fifo_03)
if not os.path.exists(fifo_04):
    os.mkfifo(fifo_04)

pid = os.fork()

if pid != 0:
    parent()
else:
    child_01()
    child_02()
    child_03()
    child_04()