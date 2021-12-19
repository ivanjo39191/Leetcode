# 169. Majority Element

Column: November 25, 2021
Tags: Easy
status: Complete

# 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

給定一個大小為 n 的數組，找到其中的多數元素。多數元素是指在數組中出現次數 大於 n / 2

## Question

**Example 1:**

```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `231 <= nums[i] <= 231 - 1`

## 相關說明

## 思路1

### 解題詳解:

設 max 紀錄最多出現的數字與次數

遍歷題目的 Array，使用 dict 紀錄。

判斷是否已在 dict  中，無則初始化為 1

每次遍歷時與 max 比較。

最終返回 max 紀錄的數字。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 187ms 

內存消耗: 15.6 MB

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in range(0, len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        max = [0, 0]
        for k, v in nums_dict.items():
            if v > max[1]:
                max = [k, v]
        return max[0]
```