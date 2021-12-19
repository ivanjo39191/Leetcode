# 215. Kth Largest Element in an Array

Tags: Meduim
status: Complete

# 215. Kth Largest Element in an Array (Medium)

## Question

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

## 題目

給定整數數組 nums 和整數 k，請返回數組中第 k 個最大的元素。 請注意，你需要找的是數組排序後的第 k 個最大的元素，而不是第 k 個不同的元素

**Example 1:**

```jsx
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2 :**

```jsx
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## 相關說明

典型的 Top K 問題，題目要求我們取第 k 大，或著前 k 個 object。

## 思路1

### 解題詳解:

使用 heap 進行排序，當排到第 k 個即停止並返回 k 。

對 heap 沒有了解可以參考上一篇講解的 heap 堆積。

主要分為 4 個 functions，題目提供的 findKthLargest 用來接收題目資料與返回答案，

heapify 用來堆積化，build_heap 建立最大堆積，heap_sort 進行最大堆積排序。

本題的 heap_sort 不需要排序整個二元樹，只要排到題目要求的第 k 個元素即可，

將長度 n 扣除 1 轉為 指標位置，再扣除 k 即為需要排序到的節點。

findKthLargest 調用 heap_sort 傳入 nums 與 k 進行排序，

最後返回數組中第 k 個最大的元素。

### Big-O

時間複雜度 O(n log n)

空間複雜度 O(1)

執行用時: 76 ms 

內存消耗: 15.6 MB

### 代碼

語言: python3

```python
class Solution:
    def heapify(self, arr: list, n: int, i: int) -> list:
        if i >= n :
            return 
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)
    
    def build_heap(self, arr: list, n: int):
        start = n // 2 - 1
        for i in range(start, -1, -1):
            self.heapify(arr, n, i)

    def heap_sort(self, arr: list, k: int) -> list:
        n = len(arr)
        self.build_heap(arr, n)
        for i in range(n-1, n-1-k, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap_sort(nums, k)
        return nums[-k]
```