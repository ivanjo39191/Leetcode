# 35. Search Insert Position

Tags: Easy
blog: published
status: Complete

# 35. Search Insert Position (Easy)

## Question

給定一個排序數組和一個目標值，在數組中找到目標值，並返回其索引。如果目標值不存在於數組中，返回它將會被按順序插入的位置。

請必須使用時間複雜度為 O(log n) 的算法。

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2

```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1

```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4

```

**Example 4:**

```
Input: nums = [1,3,5,6], target = 0
Output: 0

```

**Example 5:**

```
Input: nums = [1], target = 0
Output: 0
```

## 相關說明

本題為二分搜尋法的基礎框架，先設定搜索範圍，每次都用這範圍最中間的元素來與要查找的目標元素比大小，若無找到 target 則搜索插入位置。

## 思路1

### 解題詳解:

設 left right 兩個指標，

設一迴圈當 left ≤ right 時成立(左閉右閉)。

計算 mid ，right - left 除 2 取整數，再加上 left

例如 left 為 2，right 為 12，(12 -2) / 2 + 2 = 7，mid 為 7

當 mid 指向的元素等於 target 時，返回 mid 

當 mid 指向的元素大於 target 時縮小 right 範圍，right = mid - 1

當 mid 指向的元素小於 target 時縮小 left 範圍，left = mid + 1

while 迴圈結束時皆不符合上述條件，target 的插入位置即為 left

### Big-O

時間複雜度 O(log n)

空間複雜度 O(1)

執行用時: 44ms 

內存消耗: 15.1 MB

### 代碼

語言: python3

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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
        return left
```