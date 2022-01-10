# 17. Letter Combinations of a Phone Number

Column: January 10, 2022
Tags: Meduim

# 17. Letter Combinations of a Phone Number

## Question

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

給定一個僅包含數字 2-9 的字符串，返回所有它能表示的字母組合。答案可以按 任意順序 返回。 給出數字到字母的映射如下（與電話按鍵相同）。注意 1 不對應任何字母。

```python
# 電話
1 (    ) 2(abc ) 3(def )
4 (ghi ) 5(jkl ) 6(mno )
7 (pqrs) 8(tuv ) 9(wxyz )
```

**Example 1:**

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2:**

```
Input: digits = ""
Output: []
```

**Example 3:**

```
Input: digits = "2"
Output: ["a","b","c"]
```

**Constraints:**

- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## 相關說明

## 思路1

### 解題詳解:

使用 hashmap 紀錄數字 1-9 對應的英文字，

處理 digits 長度為 0 或 1 時的返回值。

設一 res 用來儲存組合後的字母，預設為最後一個數字

設從倒數第二的數字開始的逆序第一迴圈，

若當前值等於 digits 長度，則無新字母需組合，返回 res 。

初始化 tmp 儲存新的組合字母，

設第二迴圈將當前迴圈的字串與 res 的組合字母進行組合並存至 tmp，

第二迴圈完畢後將 tmp 更新為 res 。

第一迴圈結束，返回 res 。

### Big-O

時間複雜度 O(3^m*4^n)

空間複雜度 O(3^m*4^n)

### 代碼

語言: python3

執行用時: 28ms 

內存消耗: 15 MB

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], 
            '9': ['w', 'x', 'y', 'z'],
        }
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return n[digits]
        else:
            res = n[digits[-1]]
            for l in range(1, len(digits) + 1):
                if l == len(digits):
                    return res
                tmp = []
                for i in n[digits[-(l + 1)]]:
                    for j in res:
                        tmp.append(i+j)
                res = tmp
            return res
```