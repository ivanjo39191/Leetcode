# 69. Sqrt(x)

Column: December 17, 2021
Tags: Easy
status: Complete

# 69. Sqrt(x)

## Question

Given a non-negative integer `x`, compute and return *the square root of* `x`.

Since the return type is an integer, the decimal digits are **truncated**, and only **the integer part** of the result is returned.

**Note:** You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`.

給你一個非負整數 x ，計算並返回 x 的 算術平方根 。 由於返回類型是整數，結果只保留 整數部分 ，小數部分將被 捨去 。 注意：不允許使用任何內置指數函數和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

**Example 1:**

```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**

```
Input: a = "1010", b = "1011"
Output: "10101"
```

**Constraints:**

- `0 <= x <= 231 - 1`

## 相關說明

若 x 為 0 返回 0，

初始化 y 為 0 儲存相乘後的值，

初始化 y 為 0 儲存相乘後的值，

設一迴圈當 y < x 時成立，

如果剛好等於 x ，直接返回當前相乘的值，

相乘後得值大於 x，代表前一個相乘的值為開根號。

## 思路1

### 解題詳解:

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 3836ms 

內存消耗: 14.9 MB

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        y, z = 0, 0
        while y < x:
            z += 1
            y = z * z
            if x == y:
                return z
        return z - 1
```