# 144. Binary Tree Preorder Traversal

Column: April 25, 2022  
Tag: Binary Tree, Stack  
Tags: Easy  
blog: published  
github: published  
status: Complete  

## Question

Given the `root` of a binary tree, return *the preorder traversal of its nodes' values*

給你二元樹的根節點 root ，返回它節點值的 前序 遍歷。

**Example 1:**

```
Input: root = [1,null,2,3]
Output: [1,2,3]
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

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `100 <= Node.val <= 100`

## 相關說明

## 思路1

### 解題詳解:

使用遞歸三部曲，

定義 result 儲存結果。

定義 traversal 函數的參數為 root ，無返回值。

當 root 為 None 時終止。

前序遍歷的單層邏輯為 中 > 左 > 右。

最後調用 traversal 傳入 root。

返回 result。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 6ms 

內存消耗: 15 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        # 確認函數的參數與返回值
        def traversal(self, root: Optional[TreeNode]) -> List[int]:
            # 確認終止條件
            if root == None:
                return
            # 確認單層遞歸邏輯，前序(中左右)
            result.append(root.val)
            traversal(self, root.left)
            traversal(self, root.right)
        traversal(self, root)
        return result
```

## 思路2

### 解題詳解:

使用標記迭代法，

定義 result 儲存結果， st 為棧。

首先將 根節點 入棧，

使用 while 迭代 st (棧)，

取出 st (棧)中的節點 node，

若 node 有值，依據右左中入棧(與遞歸相反)，中入棧後加入 None 標記。

若 node 為 None，代表為標記，將下一個值加入到 result。

st (棧) 中的值全部彈出後，返回 result。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 40ms 

內存消耗: 14.8 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        st = []
        if root != None:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
                st.append(node)
                st.append(None)
            else:
                node = st.pop()
                result.append(node.val)
        return result
```