# 101. Symmetric Tree

Column: November 15, 2021
Tags: Easy
blog: published
status: Complete

# 101. Symmetric Tree

## Question

Given the `root` of a binary tree, *check whether it is a mirror of itself* (i.e., symmetric around its center).

給定一個二元樹，檢查它是否是鏡像對稱的。

**Example 1:**

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
Input: root = [1,2,2,3,4,4,3]
Output: true
```

**Example 2:**

```
    1
   / \
  2   2
   \   \
   3    3
Input: root = [1,2,2,null,3,null,3]
Output: false
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 1000]`.
- `100 <= Node.val <= 100`

## 相關說明

比較節點的左子樹與右子樹，左右中與右左中是否相等。

本題可用代碼隨想錄動態規畫的二元樹遞歸三部曲思路解題。

1. 確定遞歸函數的參數返回值
2. 確定終止條件
3. 確定單層遞歸的邏輯

## 思路1

### 解題詳解:

1. 確定遞歸函數的參數返回值
    
    比較左子樹節點與右子樹節點，返回值為 bool
    
    傳入參數則是左子樹節點與右子樹節點
    
2. 確定終止條件
    
    左空右不空 不對稱 return false
    
    左不空右空 不對稱 return false
    
    左右都空     對稱    return true
    
    左右都不為空 比較節點數值，相同 return true 反之 false
    
3. 確定單層遞歸的邏輯
    
    左右都不為空且數值相同進入遞歸
    
    比較外側是否對稱(左節點左孩子與右節點右孩子)
    
    比較內側是否對稱(左節點右孩子與右節點左孩子)
    
    左右都對稱返回 true 反之 false
    

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 36ms 

內存消耗: 14.2 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(left_root, right_root):
            if left_root == None or right_root == None:
                return left_root == right_root
            if left_root.val != right_root.val:
                return False
            return rec(left_root.left, right_root.right) and rec(left_root.right, right_root.left)
        return rec(root.left, root.right)
```