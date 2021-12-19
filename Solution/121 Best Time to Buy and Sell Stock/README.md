# 121. Best Time to Buy and Sell Stock

Column: November 15, 2021
Tags: Easy
blog: published
status: Complete

# **121. Best Time to Buy and Sell Stock**

## Question

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

給定一個數組 prices ，它的第 i 個元素 prices[i] 表示一支給定股票第 i 天的價格。你只能選擇 某一天 買入這隻股票，並選擇在 未來的某一個不同的日子 賣出該股票。設計一個算法來計算你所能獲取的最大利潤。返回你可以從這筆交易中獲取的最大利潤。如果你不能獲取任何利潤，返回 0 。

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

**Constraints:**

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

## 相關說明

## 思路1

### 解題詳解:

1. 明確 dp 數組以及下標含意
    
    dp[i][0] = 持有股票時所得最多的現金
    
    dp[i][1] = 未持有股票時所得最多的現金
    
2. 確定遞推公式
    1. dp[i][0] = 持有股票時所得最多的現金
        
        第 i-1 天已持有股票
        
        => d[i-1][0]
        
        第  i  天時買入股票 (原本現金為0，買入後為負數)
        
        => -prices[i]
        
        => dp[i][0] = max(dp[i-1][0], -prices[i])
        
    2. dp[i][1] = 未持有股票時所得最多的現金
        
        第 i-1 天不持有股票
        
        => d[i-1][1]
        
        第  i  天時賣出股票
        
        => prices[i] + d[i-1][0]
        
        => dp[i][1] = max(d[i-1][1], prices[i] + d[i-1][0])
        
3. dp 數組初始化
    
    dp[0][0] = -prices[0]
    
    dp[0][1] = 0
    
4.  確定遍歷順序
    
    dp[i] 由 dp[i-1] 推導，因此由前向後遍歷
    

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 1468ms 

內存消耗: 28.5 MB

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 明確 dp 數組以及下標含意
        '''
        dp[i][0] = 持有股票時所得最多的現金
        dp[i][1] = 未持有股票時所得最多的現金
        '''
        # 確定遞推公式
        '''
        dp[i][0] = 持有股票時所得最多的現金
            第 i-1 天已持有股票
            => d[i-1][0]
            第  i  天時買入股票 (原本現金為0，買入後為負數)
            => -prices[i]
        => dp[i][0] = max(dp[i-1][0], -prices[i])
        
        dp[i][1] = 未持有股票時所得最多的現金
            第 i-1 天不持有股票
            => d[i-1][1]
            第  i  天時賣出股票
            => prices[i] + d[i-1][0]
        => dp[i][1] = max(d[i-1][1], prices[i] + d[i-1][0])
        '''
        # dp 數組初始化
        '''
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        '''
        # 確定遍歷順序
        '''
        dp[i] 由 dp[i-1] 推導，因此由前向後遍歷
        '''
        dp = {}
        if len(prices) == 0: return 0
        dp = [[0, 0] for i in range(0, len(prices))] # 開闢空間
        dp[0] = [-prices[0], 0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return dp[len(prices)-1][1]
```