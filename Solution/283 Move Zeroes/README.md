# 283. Move Zeroes

Tags: Easy
status: Complete

# 283. Move Zeroes

## Question

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

## 題目

給定一個數組 nums，編寫一個函數將所有 0 移動到數組的末尾，同時保持非零元素的相對順序。

說明: 必須在原數組上操作，不能拷貝額外的數組。 盡量減少操作次數。

**Example 1:**

```jsx
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Example 2 :**

```jsx
Input: nums = [0]
Output: [0]
```

## 相關說明

1.  remove 時間複雜度是 O(n)
2. 快速排序：快速排序首先要確定一個待分割的元素做中間點 x，然後把所有小於等於 x 的元素放到 x 的左邊，大於 x 的元素放到其右邊。

## 思路1

### 解題詳解:

一次迴圈

直接對列表進行迴圈

透過 python 內置函數 remove, append 對列表進行操作 

遇到 0 時從移除移除

添加至列表最後一項

### Big-O

時間複雜度 $O(n^2)$  

空間複雜度 $O(1)$  

執行用時: 148 ms 

內存消耗: 15.3 MB

### 代碼

語言: python3

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for n in nums:
            if n == 0:
                nums.remove(n)
                nums.append(n)
```

## 思路2

### 解題詳解:

雙指標，做兩次迴圈

定義 i , j 兩指標，n 為 nums 長度

第一次迴圈 nums 紀錄非 0 的值，j 紀錄數量

第二次迴圈以 n 與 j 紀錄數量之差，將剩餘的 0 補完 

### Big-O

時間複雜度 $O(n)$  

空間複雜度 $O(1)$  

執行用時: 44 ms 

內存消耗: 15.4 MB

### 代碼

語言: python3

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(j, n):
            nums[i] = 0
```

## 思路3

### 解題詳解:

雙指標，參考快速排序的做法，以 0 當作中間點，不等於 0 放左邊，等於 0 放右邊

定義 i , j 兩指標 

nums[i]  不為 0 且 nums[i] 不相等於 nums[j] 

就將 nums[i]   ,nums[j] 交換

只要 nums[i] 不為 0，指標 j 都要 + 1 (調整要換的指標位置)

```python
[0, 1, 0, 2, 13] # nums[i] = 0, nums[j] = 0
[1, 0, 0, 2, 13] # nums[i] != 0 且 nums[i] != nums[j], 兩者交換, i = 1, j = 0 + 1
[1, 0, 0, 2, 13] # nums[i] == 0, i = 2, j = 1
[1, 2, 0, 0, 13] # nums[i] != 0 且 nums[i] != nums[j], 兩者交換, i = 3, j = 1 + 1
[1, 2, 13, 0, 0] # nums[i] != 0 且 nums[i] != nums[j], 兩者交換, i = 4, j = 2 + 1

```

### Big-O

時間複雜度 $O(n)$  

空間複雜度 $O(1)$  

執行用時: 40ms 

內存消耗: 15.3 MB

### 代碼

語言: python3

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
```

## 思路4

### 解題詳解:

一次迴圈

直接對 nums 列表進行迴圈

透過 python 內置函數 pop, append 對列表進行操作 

先定義一指標  j  為 0 

迴圈 nums 列表

若為 i 為 0 時用 pop 移除索引值 j 

並將移除的值存入暫存變數 temp

將 temp 添加至列表最後一項

若 i 不為 0，指標  j  + 1

下次 i 為 0 時，pop 會移除索引( j + 1 )

```python
[0, 1, 0, 2, 13]
[1, 0, 2, 13] # pop 移除 j = 0
[1, 0, 2, 13, 0] # append 添加 temp
[1, 0, 2, 13, 0] # j += 1
[1, 2, 13, 0] # pop 移除 j = 1
[1, 2, 13, 0, 0] # append 添加 temp
[1, 2, 13, 0, 0] # j += 1
[1, 2, 13, 0, 0] # j += 1
```

### Big-O

時間複雜度 $O(n)$  

空間複雜度 $O(1)$  

執行用時: 36ms 

內存消耗: 15.2 MB

### 代碼

語言: python3

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[j] == 0:
                temp = nums.pop(j)
                nums.append(temp)
            else:
                j += 1
```