# 704. Binary Search

Tags: Easy
blog: published
status: Complete

# 704. Binary Search (Easy)

## Question

給定一個 n 個元素有序的（升序）整型數組 nums 和一個目標值 target ，寫一個函數搜索 nums 中的 target，如果目標值存在返回下標，否則返回 -1。

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

```

**Example 2:**

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

## 相關說明

本題為二分搜尋法的基礎框架，先設定搜索範圍，每次都用這範圍最中間的元素來與要查找的目標元素比大小。

## 思路1

### 解題詳解:

設 left right 兩個指標，

設一迴圈當 left ≤ right 時成立。

計算 mid ，right - left 除 2 取整數，再加上 left

例如 left 為 2，right 為 12，(12 -2) / 2 + 2 = 7，mid 為 7

當 mid 指向的元素等於 target 時，返回 mid 

當 mid 指向的元素大於 target 時縮小 right 範圍，right = mid - 1

當 mid 指向的元素小於 target 時縮小 left 範圍，left = mid + 1

while 迴圈結束時皆不符合上述條件，返回 -1

### Big-O

時間複雜度 O(log n)

空間複雜度 O(1)

執行用時: 236 ms 

內存消耗: 15.7 MB

### 代碼

語言: python3

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1
```