# 33. Search in Rotated Sorted Array

Column: January 12, 2022
Tags: Meduim
s: published
status: Complete

# **33. Search in Rotated Sorted Array**

## Question

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

整數數組 nums 按升序排列，數組中的值 互不相同 。在傳遞給函數之前，nums 在預先未知的某個下標 k（0 <= k < nums.length）上進行了 旋轉，使數組變為 [nums[k], nums[k 1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下標 從 0 開始 計數）。例如， [0,1,2,4,5,6,7] 在下標 3 處經旋轉後可能變為 [4,5,6,7,0,1,2] 。給你 旋轉後 的數組 nums 和一個整數 target ，如果 nums 中存在這個目標值 target ，則返回它的下標，否則返回 -1 。

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3:**

```
Input: nums = [1], target = 0
Output: -1
```

**Constraints:**

- `1 <= nums.length <= 5000`
- `104 <= nums[i] <= 104`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `104 <= target <= 104`

## 相關說明

使用二分搜尋法，先判斷是否為部分有序區間，再判斷邊界值

## 思路1

### 解題詳解:

使用二分搜尋法，

設一迴圈找出 mid，如果找到 target 就返回。

將 nums[0] 與 nums[mid] 比較，

若 mid 值大於等於 第0項 的值，代表小於 mid 為部分有序的區間，

判斷 target 是否介於 nums[0] 與 nums[mid] 之間，

有的話右邊界調整為 mid - 1 ，反之左邊屆為 mid + 1。

若 mid 值小於 第0項的值，代表大於 mid 為部分有序的區間，

判斷 target 是否介於 nums[mid] 與 nums[r] 之間，

有的話左邊界調整為 mid + 1 ，反之右邊屆為 mid - 1。

若以上判斷沒找到 target ，返回 -1。

### Big-O

時間複雜度 O(logn)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 52ms 

內存消耗: 14.7 MB

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r - l)//2 + l 
            if nums[mid] == target:
                return mid
            
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
```