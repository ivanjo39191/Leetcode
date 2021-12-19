# 160. Intersection of Two Linked Lists

Column: November 19, 2021
Tags: Easy
blog: published
status: Complete

# 160. Intersection of Two Linked Lists

## Question

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

```python
      a1 -> a2 -> 
                  c1 -> c2 -> c3
b1 -> b2 -> b3 ->
```

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

給你兩個單鏈錶的頭節點 headA 和 headB ，請你找出並返回兩個單鏈錶相交的起始節點。如果兩個鏈錶不存在相交節點，返回 null 。 圖示兩個鏈錶在節點 c1 開始相交：

```python
      a1 -> a2 -> 
                  c1 -> c2 -> c3
b1 -> b2 -> b3 ->
```

題目數據 保證 整個鏈式結構中不存在環。注意，函數返回結果後，鏈錶必須 保持其原始結構 。自定義評測： 評測系統 的輸入如下（你設計的程序 不適用 此輸入）： intersectVal - 相交的起始節點的值。如果不存在相交節點，這一值為 0 listA - 第一個鏈錶 listB - 第二個鏈錶 skipA - 在 listA 中（從頭節點開始）跳到交叉節點的節點數 skipB - 在 listB 中（從頭節點開始）跳到交叉節點的節點數 評測系統將根據這些輸入創建鏈式數據結構，並將兩個頭節點 headA 和 headB 傳遞給你的程序。如果程序能夠正確返回相交節點，那麼你的解決方案將被 視作正確答案 。

**Example 1:**

```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
```

**Example 2:**

```
1Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

```

**Example 3:**

```
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
```

**Constraints:**

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?

## 相關說明

## 思路1

### 解題詳解:

先遍歷一次 headA 使用 set 紀錄每次的 node

再遍歷 headB ，如果 node 已在 set 中返回 set。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 124ms 

內存消耗: 30.3 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headSet = set()
        while headA:
            headSet.add(headA)
            headA = headA.next
        while headB:
            if headB in headSet:
                return headB
            headB = headB.next
```

## 思路2

### 解題詳解:

若會相交 headA + headB 與 headB + headA 的長度會相等

```python
a1 -> a2 -> c1 -> c2 -> c3 -> b1 -> b2 -> b3 -> c1
                  
b1 -> b2 -> b3 -> c1 -> c2 -> c3 -> a1 -> a2 -> c1
```

設兩個 pA, pB 為 headA, headB

同時遍歷 pA, pB，若到最後一個 node 就將 headB, headA 接在後面，

當 node 相同時返回 node。

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 132ms 

內存消耗: 29.6 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
```