# 劍指 Offer 09. 用兩個 Stack 實現 Queue

Tags: Easy
blog: published
status: Complete

# 劍指 Offer 09. 用兩個 Stack 實現 Queue

## Question

用兩個 stack 實現一個 Queue。隊列的聲明如下，請實現它的兩個函數 appendTail 和 deleteHead ，分別完成在 Queue 尾部插入整數和在 Queue 頭部刪除整數的功能。 (若 Queue 中沒有 Element，deleteHead 操作返回 -1 )

**Example 1:**

```
Output: [2,3,1]
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]

Input:
[null,null,3,-1]
```

**Example 1:**

```
Output:
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]

Input:
[null,-1,null,null,5,2]
```

## 相關說明

Stack 是後進先出（LIFO, Last In First Out）的線性表，

Queue 是先進先出（FIFO, First-In-First-Out）的線性表，

本題使用兩個 Stack 來 Queue 的操作。

## 思路1

### Python 解題詳解:

初始化兩個 list 分別作為 stackA, stackB 。

appendTail 方法，使用 append 在 stackA 末尾加入元素。

deleteHead 方法分別進行以下判斷：

1. 當 stackB 不為空：代表 B 中有已完成倒序的元素，直接返回 stack 首元素。
2. 當 stackA 為空：代表兩個 stack 為空，返回 -1
3. 若不符合上述條件，將 stackA 轉移至 stackB，實現倒序後返回 stackB 的 stack 首元素。

### Big-O

時間複雜度 O(1)

空間複雜度 O(n)

### 程式碼

語言: python3

執行用時: 324ms 

內存消耗: 18.7 MB

```python
class CQueue:

    def __init__(self):
        self.stackA, self.stackB = [], []

    def appendTail(self, value: int) -> None:
        self.stackA.append(value)

    def deleteHead(self) -> int:
        if self.stackB: return self.stackB.pop()
        if not self.stackA: return -1
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

### Golang 解題詳解:

1.  本題可使用 golang 的 library  list.List 實現 stack 操作，這裡提供範例不做說明。

### Big-O

時間複雜度 O(1)

空間複雜度 O(n)

### 程式碼

語言: golang

執行用時: **208 ms**

內存消耗: **8.6 MB**

```go
type CQueue struct {
    stackA, stackB *list.List
}

func Constructor() CQueue {
    return CQueue {
        stackA: list.New(),
        stackB: list.New(),
    }
}

func (this *CQueue) AppendTail(value int)  {
    this.stackA.PushBack(value)
}

func (this *CQueue) DeleteHead() int {
    if this.stackB.Len() == 0 {
        for this.stackA.Len() > 0 {
            e := this.stackA.Back()
            this.stackB.PushBack(e.Value)
            this.stackA.Remove(e)
        }
    }
    if this.stackB.Len() > 0 {
        e := this.stackB.Back()
        this.stackB.Remove(e)
        return e.Value.(int)
    }
    return -1
}

/**
 * Your CQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AppendTail(value);
 * param_2 := obj.DeleteHead();
 */
```

1.  使用自行實現 stack 的 Push 、 Pop 操作。

Push : 將傳入的 value 使用 append 加入 stack 末尾，

Pop : 取得 stack 長度，取 stack 末尾元素，將 stack 末尾元素移除，並返回取出的元素

AppendTail : 使用 Push 將 value 加入 stackA 末尾

DeleteHead : 

1.  當 stackB 不為空：代表 B 中有已完成倒序的元素，直接返回 stack 首元素。
2. 當 stackA 為空：代表兩個 stack 為空，返回 -1
3. 若不符合上述條件，將 stackA 轉移至 stackB，實現倒序後返回 stackB 的 stack 首元素。

### Big-O

時間複雜度 O(1)

空間複雜度 O(n)

### 程式碼

語言: golang

執行用時: 176 ms

內存消耗: 8.3 MB

```go
type CQueue struct {
    stackA stack
    stackB stack
}

type stack []int

func (s *stack) Push(value int) {
    *s = append(*s, value)
}

func (s *stack) Pop() int {
    n := len(*s)
    res := (*s)[n - 1]
    *s = (*s)[:n - 1]
    return res
}

func Constructor() CQueue {
    return CQueue {}
}

func (this *CQueue) AppendTail(value int)  {
    this.stackA.Push(value)
}

func (this *CQueue) DeleteHead() int {
    if len(this.stackB) > 0 {
        return this.stackB.Pop()
    } else if len(this.stackA) > 0 {
        for len(this.stackA) > 0 {
            this.stackB.Push(this.stackA.Pop())
        } 
        return this.stackB.Pop()
    }
    return -1
}

/**
 * Your CQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AppendTail(value);
 * param_2 := obj.DeleteHead();
 */
```