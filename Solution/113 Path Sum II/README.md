# 113. Path Sum II

Column: July 28, 2022  
Tag: Binary Tree  
Tags: Easy  
blog: published  
github: published  
status: Complete  

# 113. Path Sum II

## Question

Given the `root` of a binary tree and an integer `targetSum`, return *all **root-to-leaf** paths where the sum of the node values in the path equals* `targetSum`*. Each path should be returned as a list of the node **values**, not node references*.

A **root-to-leaf** path is a path starting from the root and ending at any leaf node. A **leaf** is a node with no children.

給你二元樹的根節點 root 和一個整數目標和 targetSum ，找出所有 從根節點到葉子節點 路徑總和等於給定目標和的路徑。 葉子節點 是指沒有子節點的節點。

**Example 1:**

```
       5
     /   \
    4     8
   / \   / \
 11   2 13   4
 / \
7   2
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
```

**Example 2:**

```
  1
 / \
2   3

Input: root = [1,2,3], targetSum = 5
Output: []
```

**Example 3:**

```
Input: root = [1,2], targetSum = 0
Output: []
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `1000 <= Node.val <= 1000`
- `1000 <= targetSum <= 1000`

## 相關說明

## 思路1

### 解題詳解:

1. 確認遞歸函數的參數與返回值

root（傳入的節點）sum 節點加總，targetSum 目標值

```python
def getPathSum(root, sum, path, targetSum):
```

沒有返回值

2. 定義終止條件

這裡的終止條件是沒有節點時， return 跳出

3.單層遍歷邏輯

這裡使用前序遍歷（中、左、右）

先記錄當前 path、將節點值加總，判斷是否有葉子節點

沒有葉子節點時，判斷 sum 與 targetSum 是否相等，

相等時將當前的 path[:] 加入到 result （最終返回值）。

若有左節點，使用左節點遞歸。

若有右節點，使用右節點遞歸。

最後將 path 與 Sum 進行回溯，完成一次遍歷。

1. 使用遞歸

初始化 result 來儲存最後的返回值。

傳入根節點與預設值

```python
getPathSum(root, 0, list(), targetSum)
```

最後返回 result。

### Big-O

時間複雜度：O(N)

空間複雜度：O(N)

### 代碼

語言: python3

執行用時: 52ms 

內存消耗: 16.6 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def getPathSum(root, sum, path, targetSum):
            if not root:
                return
            path.append(root.val)
            sum += root.val
            if not root.left and not root.right and sum == targetSum:
                result.append(path[:])
            if root.left:
                getPathSum(root.left, sum, path, targetSum)
            if root.right:
                getPathSum(root.right, sum, path, targetSum)
            path.pop()
            sum -= root.val
        result = []
        getPathSum(root, 0, list(), targetSum)
        return result
```