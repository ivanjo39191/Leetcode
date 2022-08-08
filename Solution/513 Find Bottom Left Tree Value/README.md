# 513. Find Bottom Left Tree Value

Column: July 25, 2022
Tag: Binary Tree
Tags: Meduim
blog: published
github: published
status: Complete

# **513. Find Bottom Left Tree Value**

## Question

Given the `root`
 of a binary tree, return the leftmost value in the last row of the tree.

給定一個二元樹的 根節點 root，請找出該二元樹的 最底層 最左邊 節點的值。 假設二元樹中至少有一個節點。

**Example 1:**

```

  2
 / \
1   3
Input: root = [2,1,3]
Output: 1
```

**Example 2:**

```
       1
     /   \
    2     3
   /     / \
  4     5   6
       / 
      7 
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `231 <= Node.val <= 231 - 1`

## 相關說明

## 思路1

### 解題詳解:

迭代法層序遍歷是一層一層的遍歷二元樹，使用 queue 的先進先出特性來進行實現。

在 python 中需使用內建函數 deque，

每一層的第一個節點即為該層最左邊的直，

將每一層的最左值存入 result 中，

最後一層遍歷完，result 即為最底層最左邊的節點值。

### Big-O

時間複雜度：O(N)

空間複雜度：O(N)

### 代碼

語言: python3

執行用時: 44ms 

內存消耗: 17.6 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        que = deque([root])
        result = 0
        while que:
            size = len(que)
            for i in range(size):
                if i == 0:
                    result = que[i].val 
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return result
```