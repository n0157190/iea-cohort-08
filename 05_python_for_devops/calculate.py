import sys
from math import log
i1 = sys.argv[1]
i2 = sys.argv[2]
oper = sys.argv[3]

def calculate(i1, i2, oper ):
    try:
        i1 = int(i1)
        i2 = int(i2)
    except TypeError:
        print('Math Type error!')
    
    if oper == '+':
        x = i1 + i2
    if oper == '-':
        x = i1 - i2 
    if oper == '/':
        if i2 > 0:
            x = i1 / i2 
        else:
            x = ''
            print('You cannot divide by zero!')
            exit
    if oper == '*':
        x = i1 * i2
    if oper == 'log':
        try:
            x = log(i1)/log(i2)
        except ValueError:
            print('Math domain error!')
            x = ''
        else:
            print('Everything OK')
    print(x)
    return

calculate(i1, i2, oper)
