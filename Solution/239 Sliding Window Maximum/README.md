# 239. Sliding Window Maximum

Column: March 16, 2022  
Tags: Hard  
github: published  
status: Complete  

# 239. Sliding Window Maximum

## Question

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

給你一個整數數組 nums，有一個大小為 k 的滑動窗口從數組的最左側移動到數組的最右側。你只可以看到在滑動窗口內的 k 個數字。滑動窗口每次只向右移動一位。 返回 滑動窗口中的最大值 。

**Example 1:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints:**

- `1 <= nums.length <= 105`
- `104 <= nums[i] <= 104`
- `1 <= k <= nums.length`

## 相關說明

使用 單調佇列 

## 思路1

### 解題詳解:

對滑動窗口中的元素保持單調遞減 。

定義單調遞減的佇列：

初始化佇列為 deque。

若滑動窗口移除元素 pop(value)，如果移除的元素 value 等於單調隊列的出口元素，代表該移除元素在單調佇列中，所以佇列中的元素也要彈出。

若滑動窗口新增元素 push(value)，如果push的元素value大於入口元素的數值，為了要保持單調遞減來確保佇列的首元素為最大值，就將佇列入口的元素彈出，直到push元素的數值小於等於隊列入口元素的數值為止。

若要查找佇列中的最大值 front，返回佇列首元素即可。

滑動窗口最大值：

實例一個單調佇立 que = MyQueue()，

初始化一個 result 列表。

迴圈將 nums 中的前 k 個元素先加入佇列並結束迴圈。

將出次迴圈的窗口最大值存入 result 列表。

開始滑動窗口，迴圈剩下的 len(nums) - k 個元素，

每次移除窗口中的首元素，並加入窗口新元素。

將每次滑動窗口的最大值加入 result 列表。

結束迴圈後返回 result。

### Big-O

時間複雜度 O(n)

空間複雜度 O(k)

### 代碼

語言: python3

執行用時: 568ms 

內存消耗: 27.6 MB

```python
class MyQueue: # 實現遞減單調佇列
    def __init__(self):
        self.queue = collections.deque()

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()
    
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    
    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())
        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            result.append(que.front())
        return result
```