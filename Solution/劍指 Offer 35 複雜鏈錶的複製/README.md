# 劍指 Offer 35. 複雜鏈錶的複製

Tags: Meduim
blog: published
status: Complete

# 劍指 Offer 35. 複雜鏈錶的複製

## Question

請實現 copyRandomList 函數，複製一個複雜鏈錶。在複雜鏈錶中，每個節點除了有一個 next 指針指向下一個節點，還有一個 random 指針指向鏈錶中的任意節點或者 null。

**Example 1:**

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Example 2:**

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

**Example 3:**

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

**Example 4:**

```
Input: head = []
Output: []
```

## 相關說明

本題難點為再複製鏈表的過程建立各節點的 Random 指向。普通鏈表的深拷貝可以按順序創建表節點，但因 Random 指向的節點可能尚未建立，因此需要變換思路。

## 思路1

### 解題詳解:

使用拼接與拆分的方式，

1. 先在原節點後複製新節點構建拼接鏈表，

將 old1 → old2 → old3 調整為 old1 → new1 → old2 → new2 → old3 → new3

new1 使用 old1 的 val 建立 node，

old1 的 next 指到 new1 ，new1 的 next 指到 old2。

1. 指定 new 的 Random 為 old 的 Random 的 next

例如 old1.random 為 old3，old1.random.next 就會是 new3，再賦值回 new1.random

1. 拼接完鏈表的 new Next Random 後，接著要拆分鏈表並只返回 new 的部分，

設 res 紀錄 new 的頭節點，將 new 拆分後返回 res。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 36ms 

內存消耗: 15.9 MB

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        cur = head
        while cur != None:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur = head
        while cur != None:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        pre = head
        cur = head.next
        res = cur # 最後要返回頭節點
        while cur.next != None:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None # 處理原鏈表結尾
        return res
```

語言: golang

執行用時: 0ms 

內存消耗: 3.4 MB

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    if head == nil {
        return nil
    }
    for cur := head; cur != nil; cur = cur.Next.Next {
        cur.Next = &Node{Val: cur.Val, Next: cur.Next}
    }
    for cur := head; cur != nil; cur = cur.Next.Next {
        if cur.Random != nil {
            cur.Next.Random = cur.Random.Next
        }
    }
    res := head.Next
    for cur := head; cur != nil;  cur = cur.Next {
        curNew := cur.Next
        cur.Next = cur.Next.Next
        if curNew.Next != nil {
            curNew.Next = curNew.Next.Next
        }
    }
    return res
```