# 劍指 Offer 05. 替換空格

Tags: Easy
blog: published
status: Complete

# 劍指 Offer 05. 替換空格

## Question

請實現一個函數，把字符串 s 中的每個空格替換成"%20"。

**Example 1:**

```
Input: s = "We are happy."
Output: "We%20are%20happy."

```

## 相關說明

本題為二分搜尋法的基礎框架，先設定搜索範圍，每次都用這範圍最中間的元素來與要查找的目標元素比大小，若無找到 target 則搜索插入位置。

## 思路1

### 解題詳解:

迴圈字串，並儲存到新的 array / string 返回

### Big-O

時間複雜度 O(n)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 28ms 

內存消耗: 15 MB

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        l = []
        for i in s:
            if i == ' ': l.append('%20')
            else: l.append(i)
        return ''.join(l
```

語言: golang

執行用時: 0ms 

內存消耗: 3.4 MB

```go
func replaceSpace(s string) string {
    var ans string = ""
    for _, e := range s {
        if e == ' ' {
            ans += "%20"
        } else {
            ans += string(e)
        }
    }
    
    return ans
}
```

## 思路2

### 解題詳解:

先統計空格個數

擴充字串大小，替換成 %20 之後的大小

設立雙指標 left, right

迴圈 left ≥ 0 成立

從最後一個字元向前替換，

left 非空格直接存至 right ， left 退一格，right 退一格

left 遇到空格替換成 %20 ，退一格，right 退三格

最後返回替換後的字串

### Big-O

時間複雜度 O(n)

空間複雜度 O(1)

### 代碼

語言: python3

執行用時: 32ms 

內存消耗: 15 MB

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        lists = list(s)
        count = s.count(' ')

        lists.extend([' '] * count * 2)
        left, right = len(s) - 1, len(lists) - 1
        while left >= 0:
            if lists[left] != ' ':
                lists[right] = lists[left]
                right -= 1
            else:
                lists[right-2:right+1] = '%20'
                right -= 3
            left -= 1
        return ''.join(lists)
```

### 代碼

語言: golang

執行用時: 0ms 

內存消耗: 1.9 MB

```go
func replaceSpace(s string) string {
    b := []byte(s)
    length := len(b)
    spaceCount := 0
    for _, v := range b {
        if v == ' ' {
            spaceCount ++
        }
    }
    resizeCount := spaceCount * 2
    tmp := make([]byte, resizeCount)
    b = append(b, tmp...)
    left := length - 1
    right := len(b) - 1
    for left >= 0 {
        if b[left] != ' ' {
            b[right] = b[left]
            left --
            right --
        } else {
            b[right - 2] = '%'
            b[right - 1] = '2'
            b[right] = '0'
            left --
            right = right - 3
        }
    }
    return string(b)
}
```