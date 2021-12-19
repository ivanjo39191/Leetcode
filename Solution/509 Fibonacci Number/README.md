# 509. Fibonacci Number

Column: November 11, 2021
Tags: Easy
blog: published
status: Complete

# 509. Fibonacci Number

## Question

斐波那契數，通常用 F(n) 表示，形成的序列稱為 斐波那契數列 。該數列由 0 和 1 開始，後面的每一項數字都是前面兩項數字的和。也就是：

```
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
```

給你 n ，請計算 F(n) 。

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```

Given `n`, calculate `F(n)`.

**Example 1:**

```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

**Example 2:**

```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

**Example 3:**

```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

**Constraints:**

- `0 <= n <= 30`

## 相關說明

本題可用代碼隨想錄動態規畫的動規五部曲思路解題。

1. 明確 dp 數組以及下標含意
2. 遞推公式
3. dp 數組初始化
4. 確定遍歷順序 
5. 打印 dp 數組

## 思路1

### 解題詳解:

1.  設定 dp[i] 含意
    
    dp[i]：第 i 個斐波那契數值為 dp[i]
    
2.  遞推公式
    
    題目已說明
    
    dp[i] = dp[i-1] + dp[i-2]
    
3. dp 數組初始化
    
    題目已說明
    
    dp[0] = 0
    
    dp[1] = 1
    
4. 確定遍歷順序 
    
    由前向後遍歷
    
5. 打印 dp 數組 (debug使用)

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 20ms 

內存消耗: 15 MB

```python
class Solution:
    def fib(self, n: int) -> int:
        dp={}
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        return dp[n]
```