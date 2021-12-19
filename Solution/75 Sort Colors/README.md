# 75. Sort Colors

Tags: Meduim
status: Complete

# 75. Sort Colors (Medium)

## Question

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

## 題目

給你一個有序數組 nums ，請你 原地 刪除重複出現的元素，使每個元素 最多出現兩次 ，返回刪除後數組的新長度。 不要使用額外的數組空間，你必須在 原地 修改輸入數組 並在使用 O(1) 額外空間的條件下完成。

**Example 1:**

```jsx
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Example 2 :**

```jsx
Input: nums = [2,0,1]
Output: [0,1,2]
```

**Example 3 :**

```jsx
Input: nums = [0]
Output: [0]
```

**Example 4 :**

```jsx
Input: nums = [1]
Output: [1]
```

## 相關說明

本題是經典的「荷蘭國旗問題」，由計算機科學家 Edsger W. Dijkstra 首先提出。

## 思路1

### 解題詳解:

雙指標，兩次迴圈，做兩次排序。

第一次將 0 往左移，第二次將 1 往 0 左移完後的位置左移。

設一指標 j 為 0，

第一次迴圈，從 0 開始迴圈至 nums 的長度

若該次迴圈指向的元素為 0 ，將該元素放至 j 指標，並將 j 右移一格

第二次迴圈，從 j 開始迴圈至 nums 的長度

將有 0 的放至 j 指標指向的元素，並將 j 右移一格

若該次迴圈指向的元素為 1 ，將該元素放至 j 指標，並將 j 右移一格

兩次迴圈結束即排序完畢。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

執行用時: 36 ms 

內存消耗: 15 MB

### 代碼

語言: python3

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        for k in range(j, len(nums)):
            if nums[k] == 1:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1
```

## 思路2

### 解題詳解:

三指標，

i = -1, j = 0, k = len(nums)

當 j 小於 k 時迴圈，

若 j 指向的元素為 0 ， i 先右移一格，將 j 與 i 指向的元素交換後 j 右移一格，

會將 0 換至左側。

若 j 指向的元素為 2 ， k 先左移一格，將 j 與 k 指向的元素交換，

會將 2 換至右側。

若 j 指向的元素不為 0 不為 2，j 右移一格，

會將 1 保留在中間。

迴圈結束即排序完畢。

### Big-O

時間複雜度 O(n)  

空間複雜度 O(1)  

執行用時: 32 ms 

內存消耗: 14.9 MB

### 代碼

語言: python3

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        j = 0
        k = len(nums)
        while j < k:
            if nums[j] == 0:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            elif nums[j] == 2:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                j += 1
```