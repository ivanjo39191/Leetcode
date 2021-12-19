# 617. Merge Two Binary Trees

Column: December 7, 2021
Tags: Easy
status: Complete

# 617. Merge Two Binary Trees

## Question

You are given two binary trees `root1` and `root2`.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return *the merged tree*.

**Note:** The merging process must start from the root nodes of both trees.

給定兩個二元樹，想像當你將它們中的一個覆蓋到另一個上時，兩個二元樹的一些節點便會重疊。 你需要將他們合併為一個新的二元樹。合併的規則是如果兩個節點重疊，那麼將他們的值相加作為節點合併後的新值，否則不為 NULL 的節點將直接作為新二元樹的節點。

**Example 1:**

```
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
```

**Example 2:**

```
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
```

**Constraints:**

- The number of nodes in both trees is in the range `[0, 2000]`.
- `104 <= Node.val <= 104`

## 相關說明

## 思路1

### 解題詳解:

1.  確定遞歸返回值
    
    有 root1 無 root2 時 返回 root1
    
    有 root2 無 root1 時 返回 root2
    
    兩者皆有時 返回新節點 TreeNode(val=root1.val + root2.val)
    
2.  確定遞歸終止條件
    
    無 root1, root2 時結束遞歸
    
3.  單層遞歸邏輯
    
    前序遍歷 中>左>右
    
    建立 Node val 為 root1.val + root2.val
    
    左節點傳入(root1.left, root2.left)
    
    右節點傳入(root1.right, root2.right)
    
    返回  res
    

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 84ms 

內存消耗: 15.3 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 == None and root2 == None:
            return
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        res = TreeNode(val=root1.val+root2.val)
        res.left = self.mergeTrees(root1.left, root2.left)
        res.right = self.mergeTrees(root1.right, root2.right)

        return res
```