from scipy.spatial import distance
import numpy as np
N = 20
M = 3
SCALE = 10
coords = SCALE * np.random.random((N, M))
print(coords)
m = distance.cdist(coords, coords, 'euclidean')
print(m)