# 1047. Remove All Adjacent Duplicates In String

Column: March 5, 2022
Tags: Easy
status: Complete

# **1047. Remove All Adjacent Duplicates In String**

## Question

You are given a string `s` consisting of lowercase English letters. A **duplicate removal** consists of choosing two **adjacent** and **equal** letters and removing them.

We repeatedly make **duplicate removals** on `s` until we no longer can.

Return *the final string after all such duplicate removals have been made*. It can be proven that the answer is **unique**.

給出由小寫字母組成的字符串 S，重複項刪除操作會選擇兩個相鄰且相同的字母，並刪除它們。 

在 S 上反复執行重複項刪除操作，直到無法繼續刪除。 

在完成所有重複項刪除操作後返回最終的字符串。答案保證唯一。

**Example 1:**

```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
```

**Example 2:**

```
Input: s = "azxxzy"
Output: "ay"
```

**Constraints:**

- `1 <= s.length <= 105`
- `s` consists of lowercase English letters.

## 相關說明

使用 stack

## 思路1

### 解題詳解:

初始化 stack 為空 list。

迴圈 s 字串為 ch，

若 stack 中有值，ch 等於 stack 最後一個值，代表有重複的兩個字，

此時 ch 不加入 stack，還要將 stack 最後一個值移除。

若 ch 不等於 stack 最後一個值，則將 ch 加入 stack。

迴圈結束後，將 stack 轉為字串並返回。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 85ms 

內存消耗: 14.9 MB

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = list()

        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)
```