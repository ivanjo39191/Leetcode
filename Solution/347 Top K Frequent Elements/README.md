# 347. Top K Frequent Elements

Column: March 17, 2022
Tag: Heap, Queue
Tags: Meduim
blog: published
github: published
status: Complete

# **347. Top K Frequent Elements**

## Question

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

給你一個整數數組 nums 和一個整數 k ，請你返回其中出現頻率前 k 高的元素。你可以按 任意順序 返回答案。

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints:**

- `1 <= nums.length <= 105`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

## 相關說明

使用 小頂堆 實現 優先佇列

## 思路1

### 解題詳解:

使用 map 迴圈 nums 紀錄每個數字各出現多少次。

迴圈將 map 中的元素，並使用 小頂堆 維護包含 k 個元素的優先佇列

當佇列中的元素大於 k，則佇列彈出，保持 堆 的大小一直為 k 。

返回 優先佇列中儲存的 map key。

### Big-O

時間複雜度 O(nlogk)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 48ms 

內存消耗: 18 MB

```python
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_map = {}
        for i in range(len(nums)):
            k_map[nums[i]] = k_map.get(nums[i], 0) + 1
        priority_queue = []
        
        for key, value in k_map.items():
            heapq.heappush(priority_queue, (value, key))
            if len(priority_queue) > k:
                heapq.heappop(priority_queue)

        return [k for j, k in priority_queue]
```