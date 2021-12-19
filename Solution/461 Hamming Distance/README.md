# 461. Hamming Distance

Column: December 3, 2021
Tags: Easy
status: Complete

# 461. Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

兩個整數之間的 漢明距離 指的是這兩個數字對應二進制位不同的位置的數目。 給你兩個整數 x 和 y，計算並返回它們之間的漢明距離。

## Question

**Example 1:**

```
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
```

**Example 2:**

```
Input: x = 3, y = 1
Output: 1
```

**Constraints:**

`0 <= x, y <= 231 - 1`

## 相關說明

## 思路1

### 解題詳解:

設一 sum 初始化為 0

取得 x, y 二進制格式並比較長度，將短的前面補零，

迴圈比較兩者的差異，差異則 sum 加一，

返回 sum 。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 32ms 

內存消耗: 14 MB

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        sum = 0
        x_distance = "{0:b}".format(x)
        y_distance = "{0:b}".format(y)
        if len(x_distance) > len(y_distance):
            y_distance = y_distance.zfill(len(x_distance))
        else:
            x_distance = x_distance.zfill(len(y_distance))
        for i in range(0, len(x_distance)):
            if x_distance[i] != y_distance[i]:
                sum += 1
        return sum
```