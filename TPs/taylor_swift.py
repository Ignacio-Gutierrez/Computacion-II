import math
import threading as th

def taylor(n, x):
    global list_t
    list_t.append(((-1)**n/math.factorial(2*n+1))*x**(float(2*n+1)))

def suma():
    global list_t
    global s
    s = 0
    for i in list_t:
        s += i

if __name__ =='__main__':
    list_t = []
    s = 0
    n = int(input('Insert number of terms: '))
    x = float(input('Insert x value: '))
    th_l =[]

    for i in range(n):
        th1 = th.Thread(target= taylor, args=(n,x))
        th1.start()
        th_l.append(th1)

    for i in th_l:
        th1.join()

    th2 = th.Thread(target=suma)
    th2.start()
    th2.join()

    print(f'Number of terms: {n}')
    print(f'X = {s}')
    print(f'Reference value: {math.sin(x)}')
    print(f'Error: {abs(s-math.sin(x))}')
