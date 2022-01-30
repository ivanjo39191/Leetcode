# 39. Find First and Last Position of Element in Sorted Array

Column: January 12, 2022
Tags: Meduim
s: published
status: Complete

# **39. Find First and Last Position of Element in Sorted Array**

## Question

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of* `candidates` *where the chosen numbers sum to* `target`*.* You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is **guaranteed** that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

給你一個 無重複元素 的整數數組 candidates 和一個目標整數 target ，找出 candidates 中可以使數字和為目標數 target 的 所有 不同組合 ，並以列表形式返回。你可以按 任意順序 返回這些組合。 candidates 中的 同一個 數字可以 無限制重複被選取 。如果至少一個數字的被選數量不同，則兩種組合是不同的。 對於給定的輸入，保證和為 target 的不同組合數少於 150 個。

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3:**

```
Input: candidates = [2], target = 1
Output: []
```

**Constraints:**

- `1 <= candidates.length <= 30`
- `1 <= candidates[i] <= 200`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 500`

## 相關說明

使用回溯搜尋算法。

## 思路1

### 解題詳解:

使用回溯搜尋算法，
初始化返回值 res、搜尋路徑 path，
為了剪枝先做排序 sort。
回溯三部曲：

1. 定義遞歸函數參數 backtrack，
傳入參數分別為 陣列 candidates ,目標值 target, 起始索引 startIndex, 加總 sum
2. 定義終止條件
當 sum 等於 target 時，儲存 path 的結果至 res，
當 sum 大於 target 時，結束搜尋。
3. 定義遞歸邏輯
設一迴圈 遍歷從 startIndex 到 candidates 長度 為 i，
剪枝，當 sum 加上 candidates[i] 大於 target 時，結束搜尋。
path 加入 candidates[i]，
sum 加上 candidates[i]，
遞歸 backtrack，傳入 candidates, target, i, sum。
回溯，
path 移除 candidates[i]，
sum 減去 candidates[i]，
結束迴圈。
初次呼叫 backtrack 初始索引與加總為0，傳入 candidates, target, 0, 0。
返回結果 res 。

### Big-O

時間複雜度 O(Ｓ)，Ｓ為所有可行解長度之合。

空間複雜度 O(target) ，空間複雜度取決於遞歸深度，最差情況需要 O(target) 層。

### 代碼

語言: python3

執行用時: 44ms 

內存消耗: 14 MB

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(candidates ,target, startIndex, sum):
            if sum == target:
                res.append(path[:])
                return
            if sum > target:
                return

            for i in range(startIndex, len(candidates)):
                path.append(candidates[i])
                sum += candidates[i]
                backtrack(candidates, target, i, sum)
                path.pop()
                sum -= candidates[i]
        backtrack(candidates, target, 0, 0)
        return res
```