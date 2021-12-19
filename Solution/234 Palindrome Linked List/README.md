# 234. Palindrome Linked List

Column: November 30, 2021
Tags: Easy
status: Complete

# 234. Palindrome Linked List

## Question

Given the `head` of a singly linked list, return `true` if it is a palindrome.

給你一個單鍊錶的頭節點 head ，請你判斷該鍊錶是否為回文鍊錶。如果是，返回 true ；否則，返回 false 。

```
1 -> 2 -> 2 -> 1

Input: head = [1,2,2,1]
Output: true
```

**Example 2:**

```
1 -> 2

Input: head = [1,2]
Output: false
```

**Constraints:**

- The number of nodes in the list is in the range `[1, 105]`.
- `0 <= Node.val <= 9`

## 相關說明

## 思路1

### 解題詳解:

設一 stack 遍歷後記錄所有節點，

while 迴圈頭尾 i, j，

相等的時候 頭 +1 尾 -1，

相異直接返回 False，

皆無相異返回 True。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 836ms 

內存消耗: 47.5 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head != None:
            stack.append(head.val)
            head = head.next
        i, j = 0 , len(stack) - 1
        while i < j:
            if stack[i] == stack[j]:
                i += 1
                j -= 1
            else: 
                return False
        return True
```