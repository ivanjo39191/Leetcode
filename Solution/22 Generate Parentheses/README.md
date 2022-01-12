# 22. Generate Parentheses

Column: January 12, 2022
Tags: Meduim
s: published
status: Complete

# **22. Generate Parentheses**

## Question

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

數字 n 代表生成括號的對數，請你設計一個函數，用於能夠生成所有可能的並且有效的括號組合。

**Example 1:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**

```
Input: n = 1
Output: ["()"]
```

**Constraints:**

`1 <= n <= 8`

## 相關說明

## 思路1

### 解題詳解:

使用插入法：

.(.).

.(.).(.).

初始化 n = 1 回傳 ["()"]，

設第一迴圈從 i = 2 開始，

設一 array儲存當次迴圈的結果，

迴圈當前的 res 陣列中的所有元素，

初始化雙指標 j, k 分別指向左右括號，

設 space 為添加空白間隔並轉換為 list 的元素，才可使用下標進行插入，

設第二迴圈添加間隔後的元素，

k 初始化為  j 右移兩格（跳過已有值的位置）。

設第三迴圈，將指標 k 往後移並存至 tmp，

每次迴圈最後k 右移兩格並初始化 space，

結束第三回圈。

j 右移兩格，新增插入法無法判斷到的頭尾完整括號，

結束第二回圈。

去除重複後儲存至 res，

i 右移一格，

結束第一迴圈。

返回 res。

### 代碼

語言: python3

執行用時: 93ms 

內存消耗: 15.2 MB

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 插入法
        # .(.).
        # .(.).(.).
        
        # 初始化 n = 1 回傳 ["()"]
        res  = ["()"]
        # 從 2 開始迴圈
        i = 2
        while i <= n:
            # 設一 array儲存當次迴圈的結果
            tmp = []
            # 迴圈當前的 res 陣列中的所有元素
            for r in res:
                # 初始化雙指標 j, k 分別指向左右括號
                j,k = 0, 0
                # 設 space 為添加空白間隔並轉換為 list 的元素，才可使用下標進行插入
                space = list(" " + " ".join(r) + " ")
                # 迴圈添加間隔後的元素
                while j <= len(r):
                    # k 為 j 右移兩格（跳過已有值的位置）
                    k = j + 2
                    # 設一迴圈，將指標 k 往後移並存至 tmp
                    while k <= len(r) + 1:
                        space[j] = "("
                        space[k] = ")"
                        tmp.append("".join(space).replace(' ',''))
                        # 右移兩格
                        k += 2
                        # 初始化 space
                        space = list(" " + " ".join(r) + " ")
                    # k 右移到底, j 指標右移兩格
                    j += 2
                # 新增插入法無法判斷到的頭尾完整括號
                tmp.append(r + "()")
                tmp.append("()" + r)
            # 去除重複後儲存至 res
            res = list(set(tmp))
            # 進入下一個 n 的迴圈
            i += 1
        return res
```