# 94. Binary Tree Inorder Traversal

Column: November 15, 2021
Tags: Easy
blog: published
status: Complete

# 94. Binary Tree Inorder Traversal

## Question

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

給定一個二元樹的根節點 root ，返回它的 中序 遍歷。

**Example 1:**

```
    1
     \
      2
     / 
    3  
Input: root = [1,null,2,3]
Output: [1,3,2]
```

**Example 2:**

```
Input: root = []
Output: []
```

**Example 3:**

```
Input: root = [1]
Output: [1]
```

**Example 4:**

```
    1
   / 
  2   
Input: root = [1,2]
Output: [2,1]
```

**Example 5:**

```
    1
     \
      2
Input: root = [1,null,2]
Output: [1,2]
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `100 <= Node.val <= 100`

## 相關說明

本題可用代碼隨想錄動態規畫的二元樹遞歸遍歷三部曲思路解題。

1. 確定遞歸函數的參數返回值
2. 確定終止條件
3. 確定單層遞歸的邏輯

## 思路1

### 解題詳解:

1. 確定遞歸函數的參數返回值
    
    傳入頭節點 root ，Array result
    
2. 確定終止條件
    
    遇到空節點時 return
    
3. 確定單層遞歸的邏輯
    
    中序遍歷(左中右):
    
    左 : 傳入左節點 root.left、Array result
    
    中 : 存入 Array
    
    右 : 傳入右節點 root.right、Array result
    

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 52ms 

內存消耗: 15 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def Traversal(root):
            if root == None:
                return result

            Traversal(root.left)
            result.append(root.val)
            Traversal(root.right)
        Traversal(root)
        return result
```