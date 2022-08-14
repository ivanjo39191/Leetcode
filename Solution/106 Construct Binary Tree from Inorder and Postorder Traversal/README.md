# 106. Construct Binary Tree from Inorder and Postorder Traversal

Column: August 13, 2022  
Tag: Binary Tree  
Tags: Meduim  
blog: published  
github: published  
status: Complete  

# **106. Construct Binary Tree from Inorder and Postorder Traversal**

## Question

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return *the binary tree*.

給定兩個整數數組 inorder 和 postorder ，其中 inorder 是二元樹的中序遍歷， postorder 是同一棵樹的後序遍歷，請你構造並返回這顆 二元樹 。

**Example 1:**

```
       3
     /   \
    9     20
         / \
        15   7
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

**Example 2:**

```
Input: inorder = [-1], postorder = [-1]
Output: [-1]
```

**Constraints:**

- `1 <= inorder.length <= 3000`
- `postorder.length == inorder.length`
- `3000 <= inorder[i], postorder[i] <= 3000`
- `inorder` and `postorder` consist of **unique** values.
- Each value of `postorder` also appears in `inorder`.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.
- `postorder` is **guaranteed** to be the postorder traversal of the tree.

## 相關說明

## 思路1

### 解題詳解:

```python
       3
     /   \
    9     20
         / \
        15   7
inorder   = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

以下六步驟：

1. 檢查空節點
    
    中序或後序其中一個為空時返回 None。
    
2. 取後序數組的最後一個元素為節點
    
    postorder = [9,15,7,20,3]，取出 3 為節點
    
    ```python
    root = TreeNode(val=postorder[-1]
    ```
    
3. 找後序數組的最後一個元素在中序數組的位置做為切割點
    
    inorder   = [9,3,15,20,7]，以 3 為切割點
    
4. 切割中序數組，切成中序左數組、中序右數組(一定要先切中序)
    
    inorder   = [9,3,15,20,7]，切割出 [9]、[15,20,7]
    
5. 使用切割後的中序數組大小來切割後序數組，切成後序左數組、後序右數組
    
    左中序數組 [9] 大小為 1 ，右中序數組 [15,20,7] 大小為 3，
    
    後序數組去除掉一開始拿出的最後一個元素 3 後為 [9,15,7,20]，
    
    按照中序數組的大小 1、3 切割後，
    
    左後序數組為 [9]，右後序數組為 [15,7,20]。
    
6. 遞歸左區間、右區間
    
    左節點傳入中序左區間與後序左區間
    
    右節點傳入中序右區間與後序右區間
    

### Big-O

時間複雜度：O(N)

空間複雜度：O(N)

### 代碼

語言: python3

執行用時: 156ms 

內存消耗: 88.3 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.traversal(inorder, postorder)

    def traversal(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 檢查空節點
        if not inorder or not postorder:
            return None
        
        # 取後序數組的最後一個元素為節點
        root = TreeNode(val=postorder[-1])

        # 找後序數組的最後一個元素在中序數組的位置做為切割點
        separator = inorder.index(postorder[-1])

        # 切割中序數組，切成中序左數組、中序右數組(一定要先切中序)
        leftinorder = inorder[0:separator]
        rightinorder = inorder[separator+1:]

        # 使用切割後的中序數組大小來切割後序數組，切成後序左數組、後序右數組
        leftpostorder = postorder[0:len(leftinorder)]
        rightpostorder = postorder[len(leftinorder):len(postorder)-1]
        
        # 遞歸左區間、右區間
        root.left = self.traversal(leftinorder, leftpostorder)
        root.right = self.traversal(rightinorder, rightpostorder)
        
        return root
```