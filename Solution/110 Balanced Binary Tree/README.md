# 110. Balanced Binary Tree

Column: July 8, 2022
Tag: Binary Tree
Tags: Easy
blog: published
github: published
status: Complete

# **110. Balanced Binary Tree**

## Question

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
> 

給定一個二叉樹，判斷它是否是高度平衡的二叉樹。 本題中，一棵高度平衡二叉樹定義為： 一個二叉樹每個節點 的左右兩個子樹的高度差的絕對值不超過 1 。

**Example 1:**

```
    3
   / \
  9  20
    /  \
   15   7

Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2:**

```
       1
     /   \
    2     2
   /  \
  3    3
 / \
4   4
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3:**

```
Input: root = []
Output: true
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `104 <= Node.val <= 104`

## 相關說明

根節點的高度就是二元樹的最大深度，

前序（中左右）可以求深度

後序（左右中）可以求高度

## 思路1

### 解題詳解:

使用遞歸三部曲，後序遍歷取跟節點高度

1. 確認遞歸函數的參數與返回值

getheight(root) 傳入節點，返回高度為 int

2. 定義終止條件

空節點時返回 0 

3.單層遍歷邏輯

標記不平衡的結果為 -1 ，

若維持平衡則繼續取深度。

最後若深度為 -1 返回 False，反之返回 True。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 40ms 

內存消耗: 17.3 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getheight(root):
            if not root:
                return 0
            if (leftheight := getheight(root.left)) == -1:
                return -1
            if (rightheight := getheight(root.right)) == -1:
                return -1
            if abs(leftheight - rightheight) > 1:
                return -1
            return 1 + max(leftheight, rightheight)
        return getheight(root) != -1
```