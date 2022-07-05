# 111. Minimum Depth of Binary Tree

Column: May 9, 2022
Tag: Binary Tree, Queue
Tags: Easy
blog: published
github: published
status: Complete

# 111. Minimum Depth of Binary Tree

## Question

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.

給定一個二元樹，找出其最小深度。 最小深度是從根節點到最近葉子節點的最短路徑上的節點數量。 

說明：葉子節點是指沒有子節點的節點。

**Example 1:**

```
    3
   / \
  9  20
    /  \
   15   7

Input: root = [3,9,20,null,null,15,7]
Output: 2
```

**Example 2:**

```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 105]`.
- `1000 <= Node.val <= 1000`

## 相關說明

## 思路1

### 解題詳解:

使用遞歸三部曲，後序遍歷取跟節點高度（二元樹的深度）

1. 確認遞歸函數的參數與返回值

getdepth(root) 返回長度為 int

2. 定義終止條件

空節點時返回 0 

3.單層遍歷邏輯

使用後序遍歷（左右中）

將左節點遞迴返回的結果儲存至 leftdepth

將右節點遞迴返回的結果儲存至 rightdepth

判斷以下兩種情況：

當左子樹不為空、右子樹為空，返回 1 + leftdepth

當左子樹為空、右子樹不為空，返回 1 + rightdepth

最後返回比較 leftdepth 與 rightdepth，返回較小者 + 1。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 528ms 

內存消耗: 57.3 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def getdepth(root):        
            if not root:
                return 0
            leftdepth = getdepth(root.left)
            rightdepth = getdepth(root.right)
            if root.left and not root.right:
                return 1 + leftdepth
            if not root.left and root.right:
                return 1 + rightdepth
            return 1 + min(leftdepth, rightdepth)
        return getdepth(root)
```