# 劍指 Offer 06. 從尾到頭打印鏈錶

Tags: Easy
blog: published
status: Complete

# 劍指 Offer 06. 從尾到頭打印鏈錶

## Question

輸入一個鏈錶的頭節點，從尾到頭反過來返回每個節點的值（用數組返回）。

**Example 1:**

```
Input: s = head = [1,3,2]
Output: [2,3,1]

```

## 相關說明

本題為 Linked List，給初始的 head  值，返回一個反轉的 array。

## 思路1

### 解題詳解:

迴圈將每個節點的值儲存到一個 array，再將 array 反轉後返回。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 36ms 

內存消耗: 16.3 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while (head != None):
            res.append(head.val)
            head = head.next
        return res[::-1]
```

語言: golang

執行用時: 0ms 

內存消耗: 3.1 MB

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reversePrint(head *ListNode) []int {
    if head == nil {
        return nil
    }

    res := []int{}
    for head != nil {
        res = append(res, head.Val)
        head = head.Next
    }

    for i, j := 0, len(res) - 1; i < j; {
        res[i], res[j] = res[j], res[i]
        i ++
        j --
    }
    return res
}
```