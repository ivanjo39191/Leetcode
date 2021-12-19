# 141. Linked List Cycle

Column: November 19, 2021
Tags: Easy
blog: published
status: Complete

# 141. Linked List Cycle

## Question

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

給你一個鏈錶的頭節點 head ，判斷鏈表中是否有環。如果鏈錶中有某個節點，可以通過連續跟蹤 next 指針再次到達，則鏈錶中存在環。為了表示給定鏈錶中的環，評測系統內部使用整數 pos 來表示鏈錶尾連接到鏈錶中的位置（索引從 0 開始）。如果 pos 是 -1，則在該鏈錶中沒有環。注意：pos 不作為參數進行傳遞，僅僅是為了標識鏈錶的實際情況。如果鏈錶中存在環，則返回 true 。否則，返回 false 。

**Example 1:**

```
3 -> 2 -> 0 -> -4
     ↑----------↓
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2:**

```
1 -> 2
↑----↓
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3:**

```
1
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list
```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 104]`.
- `105 <= Node.val <= 105`
- `pos` is `1` or a **valid index** in the linked-list.

## 相關說明

## 思路1

### 解題詳解:

slow 指針一次走一格，fast  指針一次兩兩格，

若為環形鏈表必定會重疊。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 48ms 

內存消耗: 18.2 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next != None:
            slow, fast = slow.next, fast.next.next
            if slow == fast: return True
        return False
```

## 思路2

### 解題詳解:

原地標記，將已到過的節點值改為特殊標記

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 52ms 

內存消耗: 17.4 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        while head != None:
            if head.val =='zz':
                return True
            head.val = 'zz'
            i += 1
            head = head.next
        return False
```