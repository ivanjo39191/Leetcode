# 222. Count Complete Tree Nodes

Column: July 7, 2022  
Tag: Binary Tree  
Tags: Meduim  
blog: published  
github: published  
status: Complete  

# 222. Count Complete Tree Nodes

## Question

Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.

According to **[Wikipedia](http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees)**, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `1` and `2h` nodes inclusive at the last level `h`.

Design an algorithm that runs in less than `O(n)` time complexity.

給你一棵 完全二元樹 的根節點 root ，求出該樹的節點個數。

完全二元樹 的定義如下：在完全二元樹中，除了最底層節點可能沒填滿外，其餘每層節點數都達到最大值，並且最下面一層的節點都集中在該層最左邊的若干位置。若最底層為第 h 層，則該層包含 1~ 2h 個節點。

**Example 1:**

```
     3
   /   \
  9    20
 / \   /
15  7 6

Input: root = [1,2,3,4,5,6]
Output: 6
```

**Example 2:**

```
Input: root = []
Output: 0
```

**Example 3:**

```
Input: root = [1]
Output: 1
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5 * 104]`.
- `0 <= Node.val <= 5 * 104`
- The tree is guaranteed to be **complete**.

## 相關說明

根節點的高度就是二元樹的最大深度，

前序（中左右）可以求深度

後序（左右中）可以求高度

## 思路1

### 解題詳解:

使用遞歸三部曲，後序遍歷取跟節點數量

1. 確認遞歸函數的參數與返回值

getcount(root) 返回節點數量為 int

2. 定義終止條件

空節點時返回 0 

3.單層遍歷邏輯

相加左右節點數量，再加上當前節點

最後返回節點數量。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 88ms 

內存消耗: 22 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def getcount(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            leftcount = getcount(root.left)
            rightcount = getcount(root.right)
            return 1 + leftcount + rightcount
        return getcount(root)
```

## 思路2

### 解題詳解:

使用標記迭代法，

定義 count 儲存結底數量， st 為堆疊。

首先將 根節點 入堆疊，

使用 while 迭代 st (堆疊)，

取出 st (堆疊)中的節點 node，

若 node 有值，依據中右左入堆疊(與遞歸相反)，中入堆疊後加入 None 標記。

若 node 為 None，代表為標記，將下一個節點數量加入到 count。

st (堆疊) 中的值全部彈出後，返回 count。

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 96ms 

內存消耗: 21.9 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        st = []
        count = 0
        if root:
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
                count += 1
        return count

        return count
```

## 思路3

### 解題詳解:

利用完全二元樹特性，與滿二元樹的特性。

滿二元樹若深度為 h ，則該樹包含 1 ~ 2^(h -1) 個節點。

而完全二元樹只有兩種情況，

情況一是滿二元樹，直接用 2^(h -1) 計算節點數量。

情況二是最後一層葉子節點沒有滿，這時分別遞迴左右孩子，

直到某一深度會是滿二元樹，就回到情況一。

最後返回節點數量。

### Big-O

時間複雜度 O(log n × log n)

空間複雜度 O(log n)

### 代碼

語言: python3

執行用時: 72ms 

內存消耗: 22 MB

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftcount = 0
        rightcount = 0
        left = root.left
        right = root.right
        while left:
            left = left.left
            leftcount += 1
        while right:
            right = right.right
            rightcount += 1
        if leftcount == rightcount:
            return (2 ** (leftcount + 1)) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
```