# 19. Remove Nth Node From End of List

Column: January 10, 2022
Tags: Meduim
s: published
status: Complete

# 19. Remove Nth Node From End of List

## Question

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

給你一個鏈錶，刪除鏈錶的倒數第 n 個結點，並且返回鏈錶的頭結點。

```python
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 1:**

```
Input: head = [1], n = 1
Output: []
```

**Example 2:**

```
Input: head = [1,2], n = 1
Output: [1]
```

**Constraints:**

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## 相關說明

## 思路1

### 解題詳解:

設一變數 res 記錄頭節點，

設一 array 儲存每次迴圈的節點，

遍歷一次所有節點並儲存至 array，

當 array 長度為 1 代表只有一個值且會被移除，返回 None，

當 array  等於 n ，代表移除頭節點，移動頭節點，

當 -n +1 等於 0 ，代表刪除的是最後一個節點，將倒數第二個節點的 next 指向 None，

不滿足上述條件，將倒數 -n-1 節點的 next 指向 -n+1 節點 (移除 -n 節點)，

最後返回 res。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 36ms 

內存消耗: 15 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        res = head
        head_array = []
        while head:
            head_array.append(head)
            head = head.next
            
        if len(head_array) == 1:
            return None
        elif len(head_array) == n:
            res = head_array[-n+1]
        elif -n + 1 == 0:
            head_array[-n-1].next = None
        else:
            head_array[-n-1].next = head_array[-n+1]
        return res
```