# 14. Longest Common Prefix

Column: December 14, 2021
Tags: Easy
status: Complete

# 14. Longest Common Prefix

## Question

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

編寫一個函數來查找字符串數組中的最長公共前綴。如果不存在公共前綴，返回空字符串 ""。

**Example 1:**

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lower-case English letters.

## 相關說明

## 思路1

### 解題詳解:

初始化 ans，

無 strs 返回空值，

strx 賦值為strs第一個值。

第一層迴圈 strx，遍歷其索引與字串，

第二層迴圈 strs (所有單字)，

判斷單字長度，若小於索引即代表沒有更多開頭相同的結果，返回 ans。

若開頭不同，返回 ans。

第二層迴圈若所有開頭相同(沒返回 ans)，ans 加上 新的 value，再次進入迴圈。

若全部一致沒有提前返回，最終要返回 ans。

### Big-O

時間複雜度 O(n*n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 32ms 

內存消耗: 15 MB

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        if not strs:
            return ""
        strx = strs[0]
        for index, value in enumerate((strx)):
            for s in strs:
                if len(s) > index:
                    if value != s[index]:
                        return ans
                else:
                    return ans
            ans = ans + value
        return ans
```