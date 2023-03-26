#!/usr/bin/python3

import os

while True:
    leido = (os.read(0,1024)).decode('utf-8')
    if len(leido) < 1024:
        os.write(1, leido.encode('utf-8'))
        break
    else:
        os.write(1, leido.encode('utf-8'))