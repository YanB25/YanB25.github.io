from scipy.optimize import fmin
from math import sin,exp
def f(x):
    return sin(x-2)**2 * exp(-x**2)

max_x = fmin(lambda x:-f(x), 0)
print(f(max_x))