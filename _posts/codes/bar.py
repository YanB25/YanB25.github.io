from scipy.optimize import least_squares
import numpy as np 
M = 30
N = 20
SCALE = 10
A = SCALE * np.random.random((M, N))
b = SCALE * np.random.random(M)
b.shape = (M, )
def costFunction(x):
    return A.dot(x) - b

res = least_squares(costFunction, np.random.random(N))

print(res.cost)
