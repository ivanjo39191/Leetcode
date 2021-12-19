# 206. Reverse Linked List

Column: November 26, 2021
Tags: Easy
status: Complete

# 206. Reverse Linked List

## Question

Given the head of a singly linked list, reverse the list, and return the reversed list.

**Example 1:**

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**

```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**

```
Input: head = []
Output: []
```

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `5000 <= Node.val <= 5000`

## 相關說明

## 思路1

### 解題詳解:

設一指標 pre 紀錄上一個節點，預設為 None。

設一 while 迴圈遍歷直到 head 為 None 時結束，

每次迴圈時 tmp 紀錄 head.next （暫存給之後用），

將 head.next 改為 pre

將 pre 改為 head（下一次迴圈時要只到這個 pre）

head 改為 tmp （一開始暫存的原 head.next ），

下一次迴圈就使用新的 head 進入。

最後返回 pre 。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 61ms 

內存消耗: 15.4 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        while head != None:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre
```