# 83. Remove Duplicates from Sorted List

Column: December 19, 2021
Tags: Easy
status: Complete

# 83. Remove Duplicates from Sorted List

## Question

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

存在一個按升序排列的鏈錶，給你這個鏈錶的頭節點 head ，請你刪除所有重複的元素，使每個元素 只出現一次 。 返回同樣按升序排列的結果鏈錶。

**Example 1:**

```
Input: head = [1,1,2]
Output: [1,2]
```

**Example 2:**

```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

**Constraints:**

- The number of nodes in the list is in the range `[0, 300]`.
- `100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.

## 相關說明

## 思路1

### 解題詳解:

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 32ms 

內存消耗: 14.2 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 儲存頭節點為最終返回值
        ans = head
        # 當節點存在時第一迴圈成立
        while head:
            # 當下一個節點存在時，第二迴圈成立
            while head.next:
                # 若下一個節點與當前節點值相等，將下一個節點指向到下下一個節點
                if head.next.val == head.val:
                    head.next = head.next.next
                # 不相等時結束第二迴圈
                else:
                    break
            # 繼續遍歷第一迴圈
            head = head.next
        # 返回一開始儲存的節點
        return ans
```