# 20. Valid Parentheses

Column: November 10, 2021
Tags: Easy
blog: published
status: Complete

# 20. Valid Parentheses

## Question

給定一個只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判斷字符串是否有效。有效字符串需滿足： 左括號必須用相同類型的右括號閉合。左括號必須以正確的順序閉合。

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example 1:**

```
Input: s = "()"
Output: true
```

**Example 2:**

```
Input: s = "()[]{}"
Output: true
```

**Example 3:**

```
Input: s = "(]"
Output: false
```

**Example 4:**

```
Input: s = "([)]"
Output: false
```

**Example 5:**

```
Input: s = "{[]}"
Output: true
```

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.

## 相關說明

本題主要使用 stack 的概念，迴圈判斷符號，左側的符號紀錄於 stack ，右側符號配對已記錄的 stack 後消除，最後stack 為空代表該字符串有效。

## 思路1

### 解題詳解:

1. 建立一 Array 為 stack 來記錄符號
2. 迴圈字符串
3. 若為左側符號紀錄於 stack 尾端
4. 若為 ")" 且 stack 長度不為 0 且 stack 尾端為 "("，移除 stack 尾端
5. 若為 "]" 且 stack 長度不為 0 且 stack 尾端為 "["，移除 stack 尾端
6. 若為 "}" 且 stack 長度不為 0 且 stack 尾端為 "{"，移除 stack 尾端 
7. 不為以上條件直接返回 False
8. 最後判斷 stack 長度是否為 0 ，如果為 0 代表成功消除完成，返回 True，反之未完成返回 False

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 28ms 

內存消耗: 14.4 MB

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            elif i == ")" and len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            elif i == "]" and len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            elif i == "}" and len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return stack == []
```

語言: golang

執行用時: 0ms 

內存消耗: 2 MB

```go
func isValid(s string) bool {
    stack := []byte{}
    for i := 0; i < len(s); i++ {
        if s[i] == '(' || s[i] == '[' || s[i] == '{' {
            stack = append(stack, s[i])
        } else if s[i] == ')' && len(stack) != 0 && stack[len(stack)-1] == '('{
            stack = stack[:len(stack)-1]
        } else if s[i] == ']' && len(stack) != 0 && stack[len(stack)-1] == '[' {
            stack = stack[:len(stack)-1]
        } else if s[i] == '}' && len(stack) != 0 && stack[len(stack)-1] == '{'{
            stack = stack[:len(stack)-1]
        } else {
            return false
        }
    }
    return len(stack) == 0
}
```