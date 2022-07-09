# 100. Same Tree

Column: July 9, 2022  
Tag: Binary Tree  
Tags: Easy  
blog: published  
github: published  
status: Complete  

# **100. Same Tree**

## Question

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

給你兩棵二元樹的根節點 p 和 q ，編寫一個函數來檢驗這兩棵樹是否相同。 如果兩個樹在結構上相同，並且節點具有相同的值，則認為它們是相同的。

**Example 1:**

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2:**

```
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3:**

```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

**Constraints:**

- The number of nodes in both trees is in the range `[0, 100]`.
- `104 <= Node.val <= 104`

## 相關說明

## 思路1

### 解題詳解:

使用遞歸三部曲，

1. 確認遞歸函數的參數與返回值

compare(p, q) 傳入要比較兩棵樹的根節點，返回 布林值

2. 定義終止條件

若兩棵樹當前節點皆為空值，代表兩棵樹相同，返回 True。

若兩棵樹當前節點一個為空一個不為空，代表兩棵樹不相同，返回 False。

若兩棵樹當前節點的值不相同，代表兩棵樹不相同，返回 True。

3.單層遍歷邏輯

後序遍歷左、右、中

當左右節點遞迴遍歷皆為 True，最後返回 True。

最後返回 compare(p, q) 布林結果。

### Big-O

時間複雜度： O(min(m,n))

其中 m 和 n 分別是兩個二元樹的節點數。對兩個二元樹同時進行深度優先搜索，只有當兩個二元樹中的對應節點都不為空時才會訪問到該節點，因此被訪問到的節點數不會超過較小的二叉樹的節點數。 

空間複雜度： O(min(m,n))

其中 m 和 n 分別是兩個二元樹的節點數。空間複雜度取決於遞迴調用的層數，遞迴調用的層數不會超過較小的二元樹的最大高度，最壞情況下，二元樹的高度等於節點數。

### 代碼

語言: python3

執行用時: 24ms 

內存消耗: 15 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def compare(p, q):
            if not q and not p:
                return True
            elif not q or not p:
                return False
            elif q.val != p.val:
                return False
            left = compare(p.left, q.left)
            right = compare(p.right, q.right)
            return left and right # if x is false, then x, else y
        return compare(p, q)
```