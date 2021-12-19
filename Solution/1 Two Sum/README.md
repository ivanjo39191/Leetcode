# 1. Two Sum

Column: December 13, 2021
Tags: Easy
status: Complete

# 1. Two Sum

## Question

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

給定一個整數數組 nums 和一個整數目標值 target，請你在該數組中找出 和為目標值 target 的那 兩個 整數，並返回它們的數組下標。 你可以假設每種輸入只會對應一個答案。但是，數組中同一個元素在答案裡不能重複出現。 你可以按任意順序返回答案。

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**

- `2 <= nums.length <= 104`
- `109 <= nums[i] <= 109`
- `109 <= target <= 10`

## 相關說明

## 思路1

### 解題詳解:

初始化 hash 表 hashmap ，

迴圈 nums (index 索引，num 值)，

由於一開始迴圈 hashmap 是空的，

因此 index 為最終返回的第二個值，反過來找第一個值，

target - num = 需要查找的第一個返回值 ，

若已找到，返回 [找到的值，迴圈到的索引]。

本次迴圈無找到則將這次的 num, index 儲存進 hashmap (要被查找的第一個返回值)。

結束迴圈皆無找到結果，返回空陣列。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 24ms 

內存消耗: 15.7 MB

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if (target - num) in hashmap:
                return [hashmap[target - num], index]
            hashmap[num] = index
        return []
```