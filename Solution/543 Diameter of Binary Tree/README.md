# 543. Diameter of Binary Tree

Column: December 6, 2021
Tags: Easy
status: Complete

# 543. Diameter of Binary Tree

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

給定一棵二元樹，你需要計算它的直徑長度。一棵二元樹的直徑長度是任意兩個結點路徑長度中的最大值。這條路徑可能穿過也可能不穿過根結點。

## Question

**Example 1:**

```
       1
    2     3
  4   5

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `100 <= Node.val <= 100`

## 相關說明

## 思路1

因可能不會穿過根節點，過程中可能兩個子節點的距離比根節點的左子節點+右子節點深度還大。

1.  遞歸返回值：

單個節點的最大深度：取左子節點與右子節點的較大值 + 1

1.  遞歸結束條件：

節點為 None 時返回 0。

1.  單層遞歸邏輯：

初始化 max 為 0 ，

計算每個子節點的最大路徑：左子節點深度 + 右子節點深度 + 1

與 max 比較將較大值儲存至 max 。

遍歷所有節點，最後返回 max。

### 解題詳解:

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 40ms 

內存消耗: 16 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.max = 0

    def maxpath(self, node):
        if not node:
            return 0
        leftdepth = self.maxpath(node.left)
        rightdepth = self.maxpath(node.right)
        self.max = max(self.max, (leftdepth + rightdepth))
        depth = 1 + max(leftdepth, rightdepth)
        return depth

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxpath(root)
        return self.max
```