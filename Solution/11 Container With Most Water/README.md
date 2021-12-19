# 11. Container With Most Water

Column: December 10, 2021
Tags: Meduim
status: Complete

# 11. Container With Most Water

Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

**Notice** that you may not slant the container.

給你 n 個非負整數 a1，a2，...，an，每個數代表坐標中的一個點 (i, ai) 。在坐標內畫 n 條垂直線，垂直線 i 的兩個端點分別為 (i, ai) 和 (i, 0) 。找出其中的兩條線，使得它們與 x 軸共同構成的容器可以容納最多的水。 說明：你不能傾斜容器。

## Question

**Example 1:**

![Untitled](image/Untitled.png)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

**Example 3:**

```
Input: height = [4,3,2,1,4]
Output: 16
```

**Example 4:**

```
Input: height = [1,2,1]
Output: 2
```

**Constraints:**

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

## 相關說明

## 思路1

初始化雙指標，left, right 為 0，height 長度 - 1，

初始化 ans 為初始 left, right 的容量，

容量算法為取 left, right 較小值，乘上 (right - left) 兩者距離。

設一迴圈， left < right 時成立，

當 left指向的值 小於 right指向的值時， right 如何變動都無法再增加容量，故 left 右移一格，

反之，right 左移一格，

ans 與 新容量比較取較大值。

結束迴圈，返回 ans。

### 解題詳解:

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 716ms 

內存消耗: 27.7 MB

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = (right - left) * min(height[left], height[right])
        while left < right:
            if  height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            ans = max(ans, (right - left) * min(height[left], height[right]))
        return ans
```