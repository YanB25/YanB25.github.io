---
title: Numpy Practise
categories: Assignment
date: 2018-05-19 11:31:00 +0800
published: true

---
# numpy practise
## prerequisize
> Generate matrices A, with random Gaussian entries, B, a Toeplitz matrix, where A ∈ R n×m and B ∈ R m×m ,
for n = 200, m = 500

由于各个题目中都需要用到某些矩阵。在`gen.py`中对他们做出了定义
``` python
# /gen.py
mu, sigma = 0, 10
n = 200
m = 500
A = np.random.normal(mu, sigma, (n, m))
A = np.matrix(A)
```
首先用`np.random.normal`产生一个n×m的高斯矩阵。
``` python
h = np.arange(1, m+1)

padding = np.zeros(h.shape[0] - 1, h.dtype)
first_col = np.r_[h]
first_row = np.r_[h[0], padding]

B = linalg.toeplitz(first_col, first_row)
B = np.matrix(B)
```
上述代码用来产生`Teoplizt`矩阵.以后的文件中，只需要import`gen.py`即可
## ex1
> Calculate $A + A$, $AA^T$  , $A ^TA$ and $AB$. Write a function that computes $ A(B- \lambda I) $ for any $\lambda$.
``` python
import numpy as np
from gen import A
from gen import B
Sum = A + A

T1 = A * A.transpose()
T2 = A.transpose() * A

prod = A * B

print(A)
print(B)
print(Sum)
print(T1)
print(T2)
print(prod)
```
//TODO: lack one function
在numpy中，转置用`matrix.transpose()`。乘法直接使用`*`即可。如此即可方便地做各类矩阵运算。
## ex2
> Generate a vector b with m entries and solve Bx = b.
``` python
import numpy as np
from numpy.linalg import inv
from gen import A, B, m
b = [i for i in range(m)]
b = np.array(b)
b.shape = (m, 1)

ans = inv(B) * b
print(repr(ans))
```
上述代码中，b是一个向量。语句
``` python
b.shape = (m, 1)
```
把b变为一个列向量。`b.shape`是b的一个公有成员，类型是Tuple。
求逆的函数是`numpy.linalg.inv`

于是方程组的解可以表示直接运算`inv(B) * b`

## ex3
> Compute the Frobenius norm of A: kAk F and the infinity norm of B: kBk ∞ . Also find the largest and
smallest singular values of B.

``` python
import numpy as np
from gen import A, B
res = np.multiply(A, A)
FrobeniusNorm = np.sqrt(np.sum(res))
print('FrobeniusNorm', FrobeniusNorm)

InfinityNorm = np.max(np.abs(B))
print('infinity norm', InfinityNorm)
```
例用`numpy`对矩阵的特殊支持，可以化简上述的运算。

对`FrobeniusNorm`而言，其值为$$\sqrt{\sum_i\sum_ja_{ij}^2}$$
于是可以使用`np.multiply(A, A)`，让矩阵中每个元素变为原来的平方。
再采用`np.sqrt(np.sum(res))`作矩阵范围内的求和。并对和值求平方根。

对于`InfinityNorm`而言，其值就是所有元素的绝对值的最大值。
`np.max(np.abs(B))`即可直接求出该值。

## ex4
> Generate a matrix Z, n × n, with Gaussian entries, and use the power iteration to find the largest
eigenvalue and corresponding eigenvector of Z. How many iterations are needed till convergence?
Optional: use the time.clock() method to compare computation time when varying n.

//TODO: clock()
``` python
# power iteration
#TODO: maybe bugs
import numpy as np
from random import random
mu, sigma = 0, 50
SIZE = 200
size = (SIZE, SIZE)
Z = np.random.normal(mu, sigma, size)
Z = np.matrix(Z)
epsilon = 1e-10
def Norm(matrix):
    '''
    return infinity norm
    '''
    #return np.sqrt(np.sum(np.multiply(matrix, matrix)))
    return np.linalg.norm(matrix)

INIT_X = np.array(np.random.randn(SIZE))
INIT_X.shape = (SIZE, 1)
INIT_LAMBDA = random() * 100
x = INIT_X
lamb = 3
times = 0
while True:
    times+=1
    tmp = Z * x
    #print('tmp', tmp)
    norm = Norm(tmp)
    nlamb = norm
    x = np.divide(tmp, norm)
    if times % 10000 == 0:
        print('{} iteration'.format(times))
        print(x)
        print(lamb)

    if abs(nlamb - lamb) < epsilon:
        break
    lamb = nlamb

    if times == 1e10:
        break
    
print(lamb)
print(x)
if times == 1e10:
    print('no solution')
else:
    print('use time {} iteratons'.format(times))

```
`INIT_X`和`INIT_LAMBDA`采用随机数的方式选择迭代初值。
`while True`是整个程序的核心，它按照`Power Iterator`算法的定义，直接迭代出所求的值。

当检测到相邻两次迭代的$\lambda$相差小于一个常数(`1e-4`)时，算法终止。

## ex5
> Generate an n × n matrix, denoted by C, where each entry is 1 with probability p and 0 otherwise. Use
the linear algebra library of Scipy to compute the singular values of C. What can you say about the
relationship between n, p and the largest singular value?

``` python
import numpy as np
n = 50
def gen(p):
    raw = np.random.random((n, n))
    return [
        [1 if i <= p else 0 for i in rows] 
            for rows in raw
    ]
def gen_matrix(p):
    return np.matrix(gen(p))

for idx, i in enumerate(np.arange(0, 1, 0.01)):
    ms = 0
    for t in range(1000):
        m = gen_matrix(i)
        u, s, vh = np.linalg.svd(m)
        ms += np.max(s)
    ms /= 1000
    print('#{}, {}, {}'.format(idx, i, ms))
```
`gen`和`gen_matrix`函数用来产生一个符合题意的随机的矩阵。
其思路是，首先随机产生一个值随机地介于`[0, 1]`的矩阵。然后对其作二值化。将`[0, p]`映射到1，将`[p, 1]`映射到0.

在得到该矩阵后，使用`np.linalg.svd`得到`SVD`分解的三个矩阵。
使用`np.max`函数得到特征值的最大值。

## ex6 
> Write a function that takes a value z and an array A and finds the element in A that is closest to z. The
function should return the closest value, not index.
Hint: Use the built-in functionality of Numpy rather than writing code to find this value manually. In
particular, use brackets and argmin.
``` python
import numpy as np
A = np.arange(40)
z = 12.39

def NearestNeighbour(A, z):
    tmp = np.abs(np.subtract(A, z))
    idx = np.argmin(tmp)
    return A[idx]

print(NearestNeighbour(A, z))
```
同样利用`numpy`内置支持的矩阵运算。
`np.subtract`会将向量（矩阵）中的每个元素都减去同一个值。
`np.argmin`返回向量（矩阵）中最小的元素的坐标。
最后的`return A[idx]`将坐标转化为向量中的值。