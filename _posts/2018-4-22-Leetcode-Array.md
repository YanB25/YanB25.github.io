---
title: Week One Assignment
categories: Assignment
date: 2018-03-07 16:46:00 +0800
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

