# 338. Counting Bits

Column: December 1, 2021
Tags: Easy
status: Complete

# 338. Counting Bits

## Question

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

給你一個整數 n ，對於 0 <= i <= n 中的每個 i ，計算其二進製表示中 1 的個數 ，返回一個長度為 n + 1 的數組 ans 作為答案。

**Example 1:**

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

**Example 2:**

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

**Constraints:**

`0 <= n <= 105`

## 相關說明

## 思路1

### 解題詳解:

設一 Array ans，

迴圈題目給的整數，

使用 bit 與 count 計算轉換為二進制後 1 的個數，並加入 ans，

最後返回 ans。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 84ms 

內存消耗: 20.9 MB

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            ans.append(bin(i).count('1'))
        return ans
```