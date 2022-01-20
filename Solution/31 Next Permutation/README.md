# 31. Next Permutation

Column: January 12, 2022
Tags: Meduim
s: published
status: Complete

# **31. Next Permutation**

## Question

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for `arr = [1,2,3]`, the following are considered permutations of `arr`: `[1,2,3]`, `[1,3,2]`, `[3,1,2]`, `[2,3,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
- Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
- While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, *find the next permutation of* `nums`.

The replacement must be **[in place](http://en.wikipedia.org/wiki/In-place_algorithm)** and use only constant extra memory.

實現獲取 下一個排列 的函數，算法需要將給定數字序列重新排列成字典序中下一個更大的排列（即，組合出下一個更大的整數）。 如果不存在下一個更大的排列，則將數字重新排列成最小的排列（即升序排列）。 必須 原地 修改，只允許使用額外常數空間。

**Example 1:**

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Example 2:**

```
Input: nums = [3,2,1]
Output: [1,2,3]
```

**Example 3:**

```
Input: nums = [1,1,5]
Output: [1,5,1]
```

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## 相關說明

[https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order](https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order)

## 思路1

### 解題詳解:

找出下一個排列組合的步驟如下

1. 後面找回來符合 nums[k] < nums[k+1] 的最大索引
2. 如果沒有符合，依題目要求反轉陣列
3. 後面找回來符合 nums[first_index] < nums[l] 的最大索引，找不到就用最後一個索引
4. 交換兩個索引
5. 翻轉第一個最大索引後的值

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 44ms 

內存消耗: 15.4 MB

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 初始化參數
        first_index = -1
        second_index = -1
        n = len(nums)
        
        # 反轉 function
        def reverse(nums, i ,j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return nums
        # 後面找回來符合 nums[k] < nums[k+1] 的最大索引
        for k in range(n-2, -1, -1):
            if nums[k] < nums[k+1]:
                first_index = k
                break
        # 如果沒有符合，依題目要求反轉陣列
        if first_index == -1:
            reverse(nums, 0, n-1)
            return 
        # 後面找回來符合 nums[first_index] < nums[l] 的最大索引，找不到就用最後一個索引
        for l in range(n-1, first_index, -1):
            if nums[l] > nums[first_index]:
                second_index = l
                break
        # 交換兩個索引索引
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        # 翻轉第一個最大索引後的值
        reverse(nums, first_index+1, n-1)
```