# 448. Find All Numbers Disappeared in an Array

Column: December 2, 2021
Tags: Easy
status: Complete

# 448. Find All Numbers Disappeared in an Array

## Question

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

給你一個含 n 個整數的數組 nums ，其中 nums[i] 在區間 [1, n] 內。請你找出所有在 [1, n] 範圍內但沒有出現在 nums 中的數字，並以數組的形式返回結果。

**Example 1:**

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

**Example 2:**

```
Input: nums = [1,1]
Output: [2]
```

**Constraints:**

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

## 相關說明

## 思路1

### 解題詳解:

nums 使用 set 去除重複，

建一個 1 至 nums 長度的 Array，

返回兩 set 之差集。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 352ms 

內存消耗: 25.5 MB

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set([i for i in range(1, len(nums) + 1)]) - set(nums))
```