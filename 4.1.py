import math

x = float(input("x = "))


def f(_x):
    return (x + math.sin (x)) / math.log10 (math.fabs (x-math.pow (x,4))) + math.log (x, 4)


print(f(_x))
