# 112. Path Sum

Column: July 9, 2022  
Tag: Binary Tree  
Tags: Easy  
blog: published  
github: published  
status: Complete  

# **112. Path Sum**

## Question

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

A **leaf** is a node with no children. A **left leaf** is a leaf that is the left child of another node.

給你二元樹的根節點 root 和一個表示目標和的整數 targetSum 。判斷該樹中是否存在 根節點到葉子節點 的路徑，這條路徑上所有節點值相加等於目標和 targetSum 。如果存在，返回 true ；否則，返回 false 。

葉子節點 是指沒有子節點的節點。

**Example 1:**

```
       5
     /   \
    4     8
   / \   / \
 11   2 13   4
 / \
7   2
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
```

**Example 2:**

```
  1
 / \
2   3

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
```

**Example 3:**

```
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `1000 <= Node.val <= 1000`

## 相關說明

## 思路1

### 解題詳解:

1. 確認遞歸函數的參數與返回值

root（傳入的節點）sum 節點加總，targetSum 目標值

```python
def sumPath(self, root, sum, targetSum)
```

返回值為布林值，True 、 False

2. 定義終止條件

這裡的終止條件是沒有節點時，返回 False

沒有葉子節點時，判斷 sum 與 targetSum 是否相等，相等返回 True，反之為 False。

3.單層遍歷邏輯

這裡使用前序遍歷（中、左、右）

先將節點值加總，判斷是否有葉子節點

若有左節點，判斷遞歸返回值是否為 True，是則直接返回 True。

若有右節點，判斷遞歸返回值是否為 True，是則直接返回 True。

### Big-O

時間複雜度：O(N)

空間複雜度：O(N)

### 代碼

語言: python3

執行用時: 48ms 

內存消耗: 16.2 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.sumPath(root, 0, targetSum)
    def sumPath(self, root, sum, targetSum):
        if not root:
            return False
        sum += root.val
        if not root.left and not root.right:
            if sum == targetSum:
                return True
            else:
                return False
        if root.left and self.sumPath(root.left, sum, targetSum):
            return True
        if root.right and self.sumPath(root.right, sum, targetSum):
            return True
        return False
```