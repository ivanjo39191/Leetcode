# 80. Remove Duplicates from Sorted Array II

Tags: Meduim
status: Complete

# 80. Remove Duplicates from Sorted Array II

## Question

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

## 題目

給你一個有序數組 nums ，請你 原地 刪除重複出現的元素，使每個元素 最多出現兩次 ，返回刪除後數組的新長度。 不要使用額外的數組空間，你必須在 原地 修改輸入數組 並在使用 O(1) 額外空間的條件下完成。

**Example 1:**

```jsx
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2 :**

```jsx
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## 相關說明

無

## 思路1

### 解題詳解:

一次迴圈

設 slow, fast 兩指標。

fast 從 0 開始迴圈 ，

slow 小於 2 時不用判斷直接先右移 2 格，最後右移第 3 格為待下次賦值。

若 fast 指向的新元素不等於 slow - 2 指向的元素就代表不重複，

就將 fast 指向的元素存至 slow，再右移一個待下次賦值。

迴圈結束直接返回 slow ，因包含待下次賦值的長度不須 + 1。

### Big-O

時間複雜度 $O(n)$  

空間複雜度 $O(1)$  

執行用時: 60 ms 

內存消耗: 14.8 MB

### 代碼

語言: python3

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if slow < 2 or nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
```

## 思路2

### 解題詳解:

題目延伸，原地 刪除重複出現的元素，使每個元素 最多出現 k 次 ，返回刪除後數組的新長度。 

將思路1 的做法寫一個 function 並傳入 k 值。

一次迴圈

設 slow, fast 兩指標。

fast 從 0 開始迴圈 ，

slow 小於 2 時不用判斷直接先右移 2 格，最後右移第 3 格為待下次賦值。

若 fast 指向的新元素不等於 slow - 2 指向的元素就代表不重複，

就將 fast 指向的元素存至 slow，再右移一個待下次賦值。

迴圈結束直接返回 slow ，因包含待下次賦值的長度不須 + 1。

此題為最多出現兩次，故傳入值為 2 。

### Big-O

時間複雜度 $O(n)$  

空間複雜度 $O(1)$  

執行用時: 44 ms 

內存消耗: 15 MB

### 代碼

語言: python3

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def solve(k):
            slow = 0
            for x in nums:
                if slow < 2 or x != nums[slow-2]:
                    nums[slow] = x
                    slow += 1
            return slow
        return solve(2)
```