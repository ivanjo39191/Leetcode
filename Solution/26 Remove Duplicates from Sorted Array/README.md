# 26. Remove Duplicates from Sorted Array

Tags: Easy
status: Complete

# 26. Remove Duplicates from Sorted Array

## Question

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

## 題目

給你一個有序數組 nums ，請你 原地 刪除重複出現的元素，使每個元素 只出現一次 ，返回刪除後數組的新長度。 不要使用額外的數組空間，你必須在 原地 修改輸入數組 並在使用 O(1) 額外空間的條件下完成。

**Example 1:**

```jsx
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2 :**

```jsx
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## 相關說明

有序數組為已排序的數組，

不須考慮數組"新長度"後面的元素。

## 思路1

### 解題詳解:

雙指標，一次迴圈。

i , j  指標對對同一個 nums 列表進行操作。

nums 第 0 個元素一定會被保留，故 j 指標從 1 開始，

i 指標從 0 開始迴圈右移，

當 i 大於 0，且 i 與 i -1 指向的元素不同時， 

就將該數值存入 j 指標，並將 j 指針右移，

迴圈結束後返回 j 指標(新長度)。

### Big-O

時間複雜度 $O(n)$  

空間複雜度 $O(1)$  

執行用時: 44 ms 

內存消耗: 15.4 MB

### 代碼

語言: python3

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if i > 0:
                if nums[i] != nums[i-1]:
                    nums[j] = nums[i]
                    j += 1
        return j
```

## 思路2

### 解題詳解:

雙指標，一次迴圈，

i , j  指標對對同一個 nums 列表進行操作。

i 指標從 0 開始，

nums 第 0 個元素一定會被保留，故 j 指標從 1 開始。

當 nums 長度為 0 時直接返回 0。

設一迴圈，當 j 指標大於 nums 列表長度時結束。

每次迴圈先將 i 指標右移一位，

若右移後指向的元素與 j 指標指向的元素不相等，

就將該數值存入 j 指標，並將 j 指針右移，

當 j 指標大於 nums 列表長度時結束迴圈，

並返回 i + 1(指標從 0 開始，返回長度須補 1 )

### Big-O

時間複雜度 $O(n)$  

空間複雜度 $O(1)$  

執行用時: 52 ms 

內存消耗: 15.2 MB

### 代碼

語言: python3

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        if len(nums) == 0:
            return 0
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
```