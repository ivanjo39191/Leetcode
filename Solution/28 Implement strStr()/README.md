# 28. Implement strStr()

Column: December 15, 2021
Tags: Easy
status: Complete

# 28. Implement strStr()

## Question

Implement [strStr()](http://www.cplusplus.com/reference/cstring/strstr/).

Return the index of the first occurrence of needle in haystack, or `-1` if `needle` is not part of `haystack`.

**Clarification:**

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).

實現 strStr() 函數。 給你兩個字符串 haystack 和 needle ，請你在 haystack 字符串中找出 needle 字符串出現的第一個位置（下標從 0 開始）。如果不存在，則返回 -1 。 說明： 當 needle 是空字符串時，我們應當返回什麼值呢？這是一個在面試中很好的問題。 對於本題而言，當 needle 是空字符串時我們應當返回 0 。這與 C 語言的 strstr() 以及 Java 的 indexOf() 定義相符。

**Example 1:**

```
Input: haystack = "hello", needle = "ll"
Output: 2
```

**Example 2:**

```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

**Example 3:**

```
Input: haystack = "", needle = ""
Output: 0
```

**Constraints:**

- `0 <= haystack.length, needle.length <= 5 * 104`
- `haystack` and `needle` consist of only lower-case English characters.

## 相關說明

## 思路1

### 解題詳解:

neeld 為 "" 時，返回 0，

遍歷 haystack，

用 slice 查詢 i 到 (i + needle 長度) 區間是否完全符合 needle，

若符合，返回 i (當前索引值)，

皆不符合，返回 -1。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 60ms 

內存消耗: 14.5 MB

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(0, len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```