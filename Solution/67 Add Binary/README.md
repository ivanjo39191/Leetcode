# 67. Add Binary

Column: December 17, 2021
Tags: Easy
status: Complete

# 67. Add Binary

## Question

Given two binary strings a and b, return their sum as a binary string.

給你兩個二進製字符串，返回它們的和（用二進製表示）。 輸入為 非空 字符串且只包含數字 1 和 0。

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

- `1 <= a.length, b.length <= 104`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

## 相關說明

## 思路1

### 解題詳解:

先將 a, b 轉換為10進位相加，在轉換回二進位返回。

### Big-O

時間複雜度 O(n+m)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 24ms 

內存消耗: 14.2 MB

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2)+int(b, 2))
```