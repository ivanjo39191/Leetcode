# 226. Invert Binary Tree

Column: November 29, 2021  
Tags: Easy  
github: published  
status: Complete  

# 226. Invert Binary Tree

Given the `root` of a binary tree, invert the tree, and return *its root*.

翻轉一棵二元樹。

## Question

**Example 1:**

```
       4                    4
   2       7      =>    7       2
 1   3   6   9        9   6   3   1

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2:**

```
  2             2
1    3   =>   3    1

Input: root = [2,1,3]
Output: [2,3,1]
```

**Example 3:**

```
Input: root = []
Output: []
```

**Constraints:**

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

## 相關說明

## 思路1

### 解題詳解:

確定遞歸返回值，

設立終止條件， root == None 時結束遞歸。

單層遞歸邏輯，使用前序遍歷 （中左右），每次遞歸交換左右節點。

最後返回 root 即為反轉後的二元樹。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 37ms 

內存消耗: 14.2 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if node == None:
                return
            node.left, node.right = node.right, node.left  
            invert(node.left)
            invert(node.right)
        invert(root)
        return root
```

## 思路2

### 解題詳解:

深度優先遍歷（迭代法）

1. 初始化堆疊列表
2. 入堆疊
3. 迭代堆疊
4. 單次迭代邏輯與標記取值（交換左右節點）
5. 返回 root 節點

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 28ms 

內存消耗: 15 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        st = []
        st.append(root)
        while st:
            node = st.pop()
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            node.left, node.right = node.right, node.left
        return root
```