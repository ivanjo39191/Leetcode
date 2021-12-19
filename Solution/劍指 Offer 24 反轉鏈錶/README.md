# 劍指 Offer 24. 反轉鏈錶

Tags: Easy
blog: published
status: Complete

# 劍指 Offer 24. 反轉鏈錶

## Question

給你單鏈錶的頭節點 head ，請你反轉鍊錶，並返回反轉後的鍊錶。

Given the head of a singly linked list, reverse the list, and return the reversed list.

**Example 1:**

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

## 相關說明

無特別說明

## 思路1

### Python 解題詳解:

要反轉鏈表 1 → 2 → 3 → None 為 3 → 2 → 1 → None

設一指標 pre 預設為 None 

設一迴圈，當 head 為 None 時結束，

tmp 用來儲存當前 head 的 next 節點（稍後會使用到）

當前 head 的 next 節點儲存 pre （也就是 1 → None 或是 2 → 1）

pre 用來儲存當前 head 節點（下次迴圈時會使用 這個 pre）

當前 head 節點更新為 tmp （一開始存的 head.next，也就是進到下一個節點進行迴圈）

迴圈結束，返回  pre 新鏈表

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 程式碼

語言: python3

執行用時: 36ms 

內存消耗: 15.4 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while (head != None):
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
            
        return pre
```

### Golang 解題詳解:

1.  同 Python

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 程式碼

語言: golang

執行用時: **0ms**

內存消耗: 2.5 **MB**

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var pre *ListNode
    for head != nil {
        tmp := head.Next
        head.Next = pre
        pre = head
        head = tmp
    }
    return pre

}
```