# 3. Longest Substring Without Repeating Characters

Column: December 9, 2021
Tags: Meduim
status: Complete

# 3. Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest substring** without repeating characters.

給定一個字符串 s ，請你找出其中不含有重複字符的 最長子串 的長度。

## Question

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Example 4:**

```
Input: s = ""
Output: 0
```

**Constraints:**

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces.

## 相關說明

## 思路1

### 解題詳解:

本題使用滑動窗口，使用 set 來記錄窗口內的值，

初始化 ans （最大值）為 0，

初始化 hash_set 為 set() ，用來記錄滑動窗口，

初始化雙指標，left, right 為 0, 0。

設第一迴圈當 右指標 < s 長度時成立，

再設第二迴圈當右指標值已在 set 中，

移除 set 移除左指標值，左指標 + 1（滑動窗口左指標前進一格），

直到沒有在右指標值沒有在 set 中時結束第二迴圈。

繼續遍歷第一迴圈，將右指標值加入 set 中，

max 比較 ans 與目前滑動窗口的長度（right - left + 1），將較大值存入 ans 。

結束第一迴圈。

最終返回 ans。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 92ms 

內存消耗: 14.2 MB

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        hash_set = set()

        left, right = 0, 0
        while right < len(s):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            ans = max(ans, (right -left) + 1)
            right += 1
        return ans
```