# 572. Subtree of Another Tree

Column: July 9, 2022  
Tag: Binary Tree  
Tags: Easy  
blog: published  
github: published  
status: Complete  

# **572. Subtree of Another Tree**

## Question

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

給你兩棵二元樹 root 和 subRoot 。檢驗 root 中是否包含和 subRoot 具有相同結構和節點值的子樹。如果存在，返回 true ；否則，返回 false 。 

二元樹 tree 的一棵子樹包括 tree 的某個節點和這個節點的所有後代節點。 tree 也可以看做它自身的一棵子樹。

**Example 1:**

```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

**Example 2:**

```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

**Constraints:**

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `104 <= root.val <= 104`
- `104 <= subRoot.val <= 104`

## 相關說明

## 思路1

### 解題詳解:

對 compare 使用遞歸三部曲定義比較兩棵樹的函數 ，

1. 確認遞歸函數的參數與返回值

compare(p, q) 傳入要比較兩棵樹的根節點，返回 布林值

2. 定義終止條件

若兩棵樹當前節點皆為空值，代表兩棵樹相同，返回 True。

若兩棵樹當前節點一個為空一個不為空，代表兩棵樹不相同，返回 False。

若兩棵樹當前節點的值不相同，代表兩棵樹不相同，返回 True。

3.單層遍歷邏輯

後序遍歷左、右、中

當左右節點遞迴遍歷皆為 True，最後返回 True。

最後返回 compare(p, q) 布林結果。

對 isSubtree 使用遞歸三部曲 ，

前序遍歷中、左、右，

若 comare 為 True 返回 True，

判斷左節點遞歸 isSubtree 傳入左節點與子樹，若為 True 返回 True，

判斷右節點遞歸 isSubtree 傳入右節點與子樹 ，若為 True 返回 True，

若上述情況都沒有返回 True，最後返回 False。

### Big-O

時間複雜度：O(S *min(S,T))

分為 isSubtree 與 compare 兩個部分

compare 其中 S 和 T 分別是兩個二元樹的節點數。對兩個二元樹同時進行深度優先搜索，只有當兩個二元樹中的對應節點都不為空時才會訪問到該節點，因此被訪問到的節點數不會超過較小的二元樹的節點數，所以時間複雜度為 min(S,T)。

isSubtree 遍歷二元樹的節點數 S，最壞情況會在每個節點進行一次 compare，所以最終的時間複雜度為 O(S *min(S,T))。

空間複雜度：O(min(S,T))

其中 S 和 T 分別是兩個二元樹的節點數。空間複雜度取決於遞歸調用的層數，遞歸調用的層數不會超過較小的二元樹的最大高度，最壞情況下，二元樹的高度等於節點數。

### 代碼

語言: python3

執行用時: 116ms 

內存消耗: 16.1 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if self.compare(root, subRoot):
            return True
        else:
            if root.left:
                left = self.isSubtree(root.left, subRoot)
                if left:
                    return True
            if root.right:
                right = self.isSubtree(root.right, subRoot)
                if right:
                    return True
            return False

    def compare(self, root, subRoot):
        if root and not subRoot:
            return False
        elif not root and subRoot:
            return False
        elif not root and not subRoot:
            return True
        elif root.val != subRoot.val:
            return False
        left = self.compare(root.left, subRoot.left) 
```