---
title: Leetcode Array
categories: Assignment
date: 2018-4-22 16:46:00 +0800
published: true

---
# 561 数组拆分
## 题面
> 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:
输入: 
```
[1,4,3,2]
```
输出: 
```
4
```
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
提示:
n 是正整数,范围在 [1, 10000].
数组中的元素范围在 [-10000, 10000].

## 题解

``` python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s = 0
        for i in nums[::2]:
            s += i
        return s
```
本题可以用贪心来做。因为局部最优必定是全局最优。

所以此处先对整个列表做排序
``` python
sums.sort()
```
随后，每两个数字为一组，取其最小值加和。
故和是第0, 2, 4, ..., 2k个数字
所以这里采用列表切片
``` python
nums[::2]
```
取出偶数个元素。
此处的列表切片等价于
``` python
nums[0:len:2]
```


# 766. 托普利茨矩阵
## 题面
> 如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。
给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。
示例 1:
输入: matrix = \[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
输出: True
解释:
1234
5123
9512
在上面这个矩阵中, 对角线分别是 "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", 各条对角线上的所有元素都相同, 因此答案是True。
示例 2:
输入: matrix = \[[1,2],[2,2]]
输出: False
解释: 
对角线, 比如: "[1, 2]" 上有不同的元素。

注意:
 matrix (矩阵)是一个包含整数的二维数组。
matrix 的行数和列数均在 [1, 20]范围内。
matrix[i][j] 包含的整数在 [0, 99]范围内。
# 题解
用暴力的方法可以解决这题。题解如下所示。
``` python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        k = min(m, n)
        for i in range(0, m):
            first = matrix[i][0]
            for t in range(min(m-i, n)):
                if matrix[i+t][t] != first:
                    print('row', i+t, t, matrix[i+t], first)
                    return False
        for j in range(0, n):
            first = matrix[0][j]
            for t in range(min(n-j, m)):
                if matrix[t][j+t] != first:
                    return False
        return True

```
首先定义了`m`, `n`, `k`, 这三个变量的初始值为矩阵的行、列和行列的最小值。

第一个`for`的作用是扫描第一列，检查第一列为起始的每个对角线是否满足托普利茨性质。若存在一个对角线不满足，直接返回`False`。

第二个`for`同理，只是它从第一行的每个元素起始的对角线开始扫面。

两个`for`循环体中的都有类似于
```python
for t in range(min(m-i, n)):
```
这一语句。其中`t`的作用是作为偏移量，让`m[i+t][t]`这一元素族扫过某个对角线。

尤其需要注意上述的`min`函数的使用，若不采用min很可能会出现数组越界的结果。

# 485. 最大连续1的个数
## 题面
> 给定一个二进制数组， 计算其中最大连续1的个数。
示例 1:

```
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
```
**注意：**
输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
## 题解
整体代码十分短。解决只需要`O(n)`即可。

最容易想到的是`O(n^2)`的暴力算法。扫描整个数组的每一个元素，对每个元素，扫描其后紧接着的1的个数。但这个实现速度太慢。

最优解如下。
变量`m`记录着（全局的）最大连续1的个数。
变量`tmp`记录着目前（在该元素上的）连续的1的个数。
``` python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        tmp = 0
        for i in nums:
            if i == 1:
                tmp += 1
                m = max(m, tmp)
            else:
                tmp = 0
        return m
```
扫描整个数组。若该元素是1，则将`tmp`加1.同时，`m = max(m, tmp)`，即让`m`一直保持着”全局最大“的连续的1的个数。

若扫描到一个元素0，则将`tmp`置为0，因为目前连续的1已经”断开“了。可以省略这步中的`m = max(m, tmp)`，因为可以确保`0`一定不大于`m`。

# 283. 移动零 
## 题面
> 给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。
例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。

**注意事项:**
必须在原数组上操作，不要为一个新数组分配额外空间。
尽量减少操作总数。

## 题解
这里采用类似于（某个实现的）快速排序的思路。由于快排中有一步是，将所有小于`pivot`的值移到数组的一边，大于等于`pivot`的值移动到另一边。若特别地，取`pivot`为0，则快排的代码刚好可以实现本题的操作。
``` python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                tmp = nums[index]
                nums[index] = nums[i]
                nums[i] = tmp
```
[0, index）这个区间的元素都不为0.扫描一遍数组，不断维护index，做交换。当扫描完毕后，index为不为零的元素总数，且顺序不变地存储在列表的最左侧。