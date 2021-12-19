# 58. Length of Last Word

Column: December 16, 2021
Tags: Easy
status: Complete

# 58. Length of Last Word

## Question

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

給你一個字符串 s，由若干單詞組成，單詞前後用一些空格字符隔開。返回字符串中最後一個單詞的長度。 單詞 是指僅由字母組成、不包含任何空格字符的最大子字符串。

**Example 1:**

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

**Example 2:**

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

**Example 3:**

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

**Constraints:**

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

## 相關說明

## 思路1

### 解題詳解:

從結尾逆序查找，反著找到的第一個字長度即為答案。

初始化指標 i 為 1，為逆序的索引的起點，

初始化指標 j 為 -1，為第一個字的長度， - 1 用來辨識是否為尚未找到字串(可能先遇到空格)。

設一迴圈 s 長度，逆續的索引需 + 1，

尚未找到字串時，找到字串將 j 設為 1，

已找到字串，下一個值為字串時 j + 1，下一個值為空格，返回 j (儲存的字串長度)。

若未提前返回，i 前進一格進入下一次迴圈，

後續沒有空格時，返回 j。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 38ms 

內存消耗: 14.2 MB

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, j  = 1, -1
        while i < len(s) + 1:
            if j == -1:
                if s[-i] != ' ':
                    j = 1
            elif j:
                if s[-i] != ' ':
                    j += 1
                else:
                    return j
            i += 1
        return j
```

## 思路2

### 解題詳解:

使用 slice 切片，移除空值與空格，返回最後一個值的長度。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 20ms 

內存消耗: 14.4 MB

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([i for i in s.split(' ') if i != ' ' and i != ''][-1])
```