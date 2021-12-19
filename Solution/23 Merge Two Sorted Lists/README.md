# 23. Merge Two Sorted Lists

Column: November 10, 2021
Tags: Easy
blog: published
status: Complete

# 23. Merge Two Sorted Lists

## Question

將兩個升序鏈錶合併為一個新的 升序 鏈錶並返回。新鍊錶是通過拼接給定的兩個鏈錶的所有節點組成的。

Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.

**Example 1:**

```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**

```
Input: l1 = [], l2 = []
Output: []
```

**Example 3:**

```
Input: l1 = [], l2 = [0]
Output: [0]
```

**Constraints:**

- The number of nodes in both lists is in the range `[0, 50]`.
- `100 <= Node.val <= 100`
- Both `l1` and `l2` are sorted in **non-decreasing** order.

## 相關說明

本題為鏈結串列的問題，以下的第一個解法為簡單的迴圈解。

## 思路1

### 解題詳解:

1.  設一變數 res 為 l1，最後返回時使用
2. 判斷 l2 與 l1 皆為空 返回 空
3. 若 l2 為空返回 l1，l1 為空返回 l2
4. 迴圈 l2 
5. 若 l2 head 值小於 l1 head 值
    1. 將 l1 的 head 替換為 l2
    2. 新 l1 的 next 為原本的 l1
    3. res 起始點也更新為新的 l1
    4. l2 前進一格到 l2.next
6. 若 l2 val 值大於 l1 val 值
    1. 若 l1.next 有值且 l2 val 大於 l1.next.val，此時 l1 前進一格
    2. 否則將 [l](http://l1.next)1.next 替換為 l2 ，l1.next.next 為原本的 l1.next
    3. l2 前進一格到 l2.next
7. 最後返回 res

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 28ms 

內存消耗: 14.4 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = l1
        if l2 == None and l1 == None:
            return None
        if l2 == None:
            return l1
        if l1 == None:
            return l2
        while l2:
            if l2.val < l1.val:
                tmp = l1
                l1 = ListNode(l2.val)
                res = l1
                l1.next = tmp
                l2 = l2.next
            else:
                if l1.next and l2.val > l1.next.val:
                    l1 = l1.next
                else:
                    tmp = l1.next
                    l1.next = ListNode(l2.val)
                    l1.next.next =tmp
                    l2 = l2.next
        return res
```

語言: golang

執行用時: 0ms 

內存消耗: 2.6 MB

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil && l2 == nil {
        return nil
    }  else if l1 == nil {
        return l2
    } else if l2 == nil {
        return l1
    }
    res := l1
    for l2 != nil{
        if l2.Val < l1.Val {
            tmp := l1
            l1 = &ListNode{Val: l2.Val, Next: tmp}
            res = l1
            l2 = l2.Next
        } else {
            if l1.Next != nil && l1.Next.Val < l2.Val {
                l1 = l1.Next
            } else {
                tmp := l1.Next
                l1.Next = &ListNode{Val: l2.Val, Next: tmp}
                l1 = l1.Next
                l2 = l2.Next
            }
        }
    }
    return res
}
```