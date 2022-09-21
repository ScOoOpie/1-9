import math

x = float(input("x = "))


def f(_x):
    return (_x + math.sin (_x)) / math.log10 (math.fabs (_x-math.pow (_x,4))) + math.log (_x, 4)


print(f(_x))
