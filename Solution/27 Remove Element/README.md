# 27. Remove Element

Tags: Easy
status: Complete

# 27. Remove Element

## Question

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

## 題目

給你一個數組 nums 和一個值 val，你需要 原地 移除所有數值等於 val 的元素，並返回移除後數組的新長度。 不要使用額外的數組空間，你必須僅使用 O(1) 額外空間並 原地 修改輸入數組。 元素的順序可以改變。你不需要考慮數組中超出新長度後面的元素。

**Example 1:**

```jsx
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2 :**

```jsx
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

## 相關說明

不須考慮數組"新長度"後面的元素

## 思路1

### 解題詳解:

雙指標，一次迴圈

i , j  指標對對同一個 nums 列表進行操作

i 指標從 0 開始迴圈右移，如果 val 不為 0

就將該數值存入 j 指標，並將 j 指針右移

最後返回 j 指標(新長度)

### Big-O

時間複雜度 $O(n)$  

空間複雜度 $O(1)$  

執行用時: 44 ms 

內存消耗: 14.8 MB

### 代碼

語言: python3

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
```

## 思路2

### 解題詳解:

雙指標，一次迴圈

left , right  指標對對同一個 nums 列表進行操作

left  指標為 0 從頭開始右移，right 指標為 列表長度 從尾開始左移

如果 left 指標指向的元素為 0 ，將 right 指標指向的元素寫入 left 指標，

left 指標不動，right 指標左移一格 ( right -1)，

如果 left 指標指向的元素不為 val ，不對元素操作，

left 指標右移一格，right 指標不動

當兩指標重合時( left < right) 即代表遍歷完所有元素結束迴圈

此時 left 指標長度內指向的元素皆不為 val 

最後返回 left 指標(新長度)

### Big-O

時間複雜度 $O(n)$  

空間複雜度 $O(1)$  

執行用時: 36 ms 

內存消耗: 14.9 MB

### 代碼

語言: python3

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)
        while (left < right):
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
        return left
```