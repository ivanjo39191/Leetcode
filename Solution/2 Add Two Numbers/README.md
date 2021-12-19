# 2. Add Two Numbers

Column: December 8, 2021
Tags: Meduim
status: Complete

# 2. Add Two Numbers

## Question

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

給你兩個 非空 的鏈錶，表示兩個非負的整數。它們每位數字都是按照 逆序 的方式存儲的，並且每個節點只能存儲 一位 數字。 請你將兩個數相加，並以相同形式返回一個表示和的鏈錶。 你可以假設除了數字 0 之外，這兩個數都不會以 0 開頭。

**Example 1:**

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:**

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

**Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## 相關說明

## 思路1

### 解題詳解:

設一新鏈表頭節點為 l3，並儲存頭節點為 ans (最終返回時使用)

設一 while 迴圈 ，當 l1, l2 存在時進入迴圈

若 l1, l2 皆存在，判斷 l1, l2, l3 節點的值相加是否進位，

無進位時將加總值儲存至 l3，l3.next 初始化為 0，

有進位時將加總值的個位數儲存至 l3，l3.next 初始化為 1。

l1 進入下一個節點 l1.next

l2 進入下一個節點 l2.next

若 l1 存在 l2 不存在，判斷 l1, l3 節點的值相加是否進位，

無進位時將加總值儲存至 l3，l3.next 初始化為 0，

有進位時將加總值的個位數儲存至 l3，l3.next 初始化為 1。

l1 進入下一個節點 l1.next

若 l2 存在 l1 不存在，判斷 l2, l3 節點的值相加是否進位，

無進位時將加總值儲存至 l3，l3.next 初始化為 0，

有進位時將加總值的個位數儲存至 l3，l3.next 初始化為 1。

l2 進入下一個節點 l2.next

迴圈的最後， l3 進入下一個節點 l3.next。

迴圈結束後，返回 ans (l3 的頭節點)。

### Big-O

時間複雜度 O(max(m, n))

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 68ms 

內存消耗: 14.4 MB

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(val=0, next=None)
        ans = l3
        while l1 or l2:
            if l1 and l2:
                if l3.val + l1.val + l2.val > 9:
                    l3.val = (l3.val + l1.val + l2.val) % 10
                    l3.next = ListNode(val=1, next=None)
                else:
                    l3.val = l3.val + l1.val + l2.val
                    if l1.next or l2.next:
                        l3.next = ListNode(val=0, next=None)
                l1 = l1.next
                l2 = l2.next
            else:
                if l1:
                    if l3.val + l1.val > 9:
                        l3.val = (l3.val + l1.val) % 10
                        l3.next = ListNode(val=1, next=None)
                    else:
                        l3.val = l3.val + l1.val
                        if l1.next:
                            l3.next = ListNode(val=0, next=None)
                    l1 = l1.next
                if l2:
                    if l3.val + l2.val > 9:
                        l3.val = (l3.val + l2.val) % 10
                        l3.next = ListNode(val=1, next=None)
                    else:
                        l3.val = l3.val + l2.val
                        if l2.next:
                            l3.next = ListNode(val=0, next=None)
                    l2 = l2.next
            l3 = l3.next
        
        return ans
```