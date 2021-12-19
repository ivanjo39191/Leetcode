# 70. Climbing Stairs

Column: November 11, 2021
Tags: Easy
blog: published
status: Complete

# 70. Climbing Stairs

## Question

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:**

`1 <= n <= 45`

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
    
    dp[i]：達到第 i 階梯有 [i] 種方法
    
2.  遞推公式
    
    1階 1種方法
    
    2階 2種方法
    
    3階 從1階踏兩步 或是 從2階踏一步， 1 + 2 = 3種方法
    
    4階 從2階踏兩步 或是 從2階踏一步， 2 + 3 = 5種方法
    
    p.s. 第4階不會有第2階踏兩個一步上來的狀況，因為踏第1個一步就等同於從第3階踏一步上來了
    
    公式:
    
    dp[i] = dp[i-1] + dp[i-2]
    
3. dp 數組初始化
    
    dp[1] = 1 為第一步的時候
    
    dp[2] = 2 為第二步的時候
    
4. 確定遍歷順序 
    
    由前向後遍歷
    
    從第3階開始遍歷
    
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
    def climbStairs(self, n: int) -> int:
        dp={}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        return dp[n]
```