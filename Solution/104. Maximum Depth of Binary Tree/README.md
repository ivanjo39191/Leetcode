# 104. Maximum Depth of Binary Tree

Column: May 9, 2022  
Tag: Binary Tree, Queue  
Tags: Easy  
blog: published  
github: published  
status: Complete  

# 104. Maximum Depth of Binary Tree

## Question

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

給定一個二元樹，找出其最大深度。 二叉樹的深度為根節點到最遠葉子節點的最長路徑上的節點數。 說明: 葉子節點是指沒有子節點的節點。

**Example 1:**

```
    3
   / \
  9  20
    /  \
   15   7

Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2
```

**Example 3:**

```
Input: root = [1]
Output: [1]
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 104]`.
- `100 <= Node.val <= 100`

## 相關說明

根節點的高度就是二元樹的最大深度，

前序（中左右）可以求深度

後序（左右中）可以求高度

## 思路1

### 解題詳解:

使用遞歸三部曲，後序遍歷取跟節點高度（二元樹的深度）

1. 確認遞歸函數的參數與返回值

getdepth(root) 返回長度為 int

2. 定義終止條件

空節點時返回 0 

3.單層遍歷邏輯

先求左右子樹長度，取較大值後 + 1（算上當前中間節點） 就是目前節點為根節點時樹的深度

最後返回 depth。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 44ms 

內存消耗: 17.3 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getdepth(root):
            if not root:
                return 0
            leftdepth = getdepth(root.left)
            rightdepth = getdepth(root.right)
            return 1 + max(leftdepth, rightdepth)
        return getdepth(root)
```

## 思路2

### 解題詳解:

使用廣度優先搜尋，層序遍歷。

一層一層地往下來求二元樹的深度是非常適合的，

使用 queue 先進先出的特性來實現，

在每次 while 進入下一層時將 depth  +1

最後返回 depth 。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 44ms 

內存消耗: 16.3 MB

```python
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([root])
        depth = 0
        while que:
            size = len(que)
            depth += 1
            for _ in range(size):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return depth
```