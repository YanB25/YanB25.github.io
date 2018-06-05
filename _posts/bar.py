from scipy.optimize import least_squares
import numpy as np 
M = 30
N = 20
A = np.matrix(np.random.random((M, N)))
b = np.random.random(M)
b.shape = (M, 1)
def costFunction(x):
