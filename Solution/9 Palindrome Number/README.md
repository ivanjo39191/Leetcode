# 9. Palindrome Number

Column: December 13, 2021
Tags: Easy
status: Complete

# 9. Palindrome Number

## Question

Given an integer `x`, return `true` if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward.

- For example, `121` is a palindrome while `123` is not.

給你一個整數 x ，如果 x 是一個回文整數，返回 true ；否則，返回 false 。 回文數是指正序（從左向右）和倒序（從右向左）讀都是一樣的整數。例如，121 是回文，而 123 不是。

**Example 1:**

```
Input: x = 121
Output: true
```

**Example 2:**

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Example 4:**

```
Input: x = -101
Output: false
```

**Constraints:**

`231 <= x <= 231 - 1`

## 相關說明

## 思路1

### 解題詳解:

根據題目，負數不是回文，0 是回文。

strx 為數值轉為字串，

初始化雙指標 i, j 為 0, strx 長度 - 1，

設一迴圈 i < j 時成立，

若 i 指向的值 等於 j 指向的值， i 右移一格，j 左移一格，

若不得於，直接返回 False，

迴圈成功結束，代表全部相等=回文，返回 True，

若沒進迴圈，x < 0，返回 False。

### Big-O

時間複雜度 O(n*n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 60ms 

內存消耗: 14.9 MB

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        while x >= 0:
            strx = f"{x}"
            i, j = 0, len(strx) - 1
            while i < j:
                if strx[i] == strx[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        return False
```