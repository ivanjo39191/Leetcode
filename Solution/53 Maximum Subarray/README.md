# 53. Maximum Subarray

Column: November 10, 2021
Tags: Easy
blog: published
status: Complete

# 53. Maximum Subarray

## Question

給定一個整數數組 nums ，找到一個具有最大和的連續子數組（子數組最少包含一個元素），返回其最大和。

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.

A **subarray** is a **contiguous** part of an array.

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Example 2:**

```
Input: nums = [1]
Output: 1
```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]
Output: 23
```

**Constraints:**

- `1 <= nums.length <= 105`
- `104 <= nums[i] <= 104`

## 相關說明

本題有可用暴力解、動態規劃、分治法，暴力解的解法，只要判斷了當前加總值加上下一個值<當前值即可結束當次迴圈，時空方面都還能取得不錯的成績

## 思路1

### 解題詳解:

l 為 nums 長度

tmp 紀錄當前的加總，初始為 nums[0]

result 為最後要返回的值，初始為 tmp

1. 使用 range(1, l) 進行迴圈
2. 當前加總值加上下一個值<當前加總

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 696ms 

內存消耗: 27.9 MB

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        tmp = nums[0]
        result = tmp
        for i in range(1, l):
            if nums[i] < tmp + nums[i]:
                tmp = tmp + nums[i]
                if result < tmp:
                    result = tmp
            else:
                if result < nums[i]:
                    result = nums[i]
                if result < nums[i] + tmp:
                    result = nums[i] + tmp
                tmp = nums[i]
        return result
```