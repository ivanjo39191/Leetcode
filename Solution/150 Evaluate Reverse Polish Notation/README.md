# 150. Evaluate Reverse Polish Notation

Column: March 16, 2022
Tag: Stack
Tags: Meduim
github: published
status: Complete

# **150. Evaluate Reverse Polish Notation**

## Question

Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

**Note** that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

根據 逆波蘭表示法，求表達式的值。 有效的算符包括 +、-、*、/ 。每個運算對象可以是整數，也可以是另一個逆波蘭表達式。 注意 兩個整數之間的除法只保留整數部分。 可以保證給定的逆波蘭表達式總是有效的。換句話說，表達式總會得出有效數值且不存在除數為 0 的情況。

**Example 1:**

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3:**

```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

**Constraints:**

- `1 <= nums.length <= 105`
- `104 <= nums[i] <= 104`
- `1 <= k <= nums.length`

## 相關說明

使用 棧 ，要注意的本題小數位為無條件捨去。

## 思路1

### 解題詳解:

本題的算術式必定成立，所以不用處理例外情況，當取到符號時必定有兩個元素在 stack 中，

迴圈 tokens 進行判斷，

第一個 彈出的放後面，第二個彈出的放前面進行運算，

其中除法可能會有小數位需進行特殊處理，

最後算出的結果放回 stack 中等待下次運算。

迴圈結束後返回 stack 中剩下唯一的元素為計算結果。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 36ms 

內存消耗: 16.4 MB

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                second = stack.pop()
                first = stack.pop()
                if i == "+":
                    ans =  first + second
                elif i == "-":
                    ans =  first - second
                elif i == "*":
                    ans =  first * second
                elif i == "/":
                    ans =  int("%d" % (first / second))
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack.pop()
```