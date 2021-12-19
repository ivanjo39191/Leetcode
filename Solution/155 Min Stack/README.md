# 155. Min Stack

Tags: Easy
blog: published
status: Complete

# 155. Min Stack

## Question

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

**Example 1:**

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## 相關說明

stack 為後進先出。

## 思路1

### Python 解題詳解:

定義兩個 stack, min 為堆疊

使用 min 來記錄 stack 放入元素時的最小值，

push function，先將傳入值與 min 頂元素比較，比 min 小則取代存入，比 min 大則再存入一次 min

pop function，將 stack, min 的頂元素同時移除

top function，取出 stack 頂元素，

getMin function，取出 min 頂元素。

### Big-O

時間複雜度 O(1)

空間複雜度 O(n)

### 程式碼

語言: python3

執行用時: 112ms 

內存消耗: 16.7 MB

```python
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min:
            if val <= self.min[-1]:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
        else:
            self.min.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else: 
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

### Golang 解題詳解:

MinStack  定義兩個 stack, min 為堆疊

使用 min 來記錄 stack 放入元素時的最小值，

Push func，先將傳入值與 min 頂元素比較，比 min 小則取代存入，比 min 大則在存入一次 min

Pop func 將 stack, min 的頂元素同時移除

Top func，取出 stack 頂元素，

GetMin func，取出 min 頂元素。

### Big-O

時間複雜度 O(1)

空間複雜度 O(n)

### 程式碼

語言: golang

執行用時: 16**ms**

內存消耗: 8.3 **MB**

```go
type MinStack struct {
    stack []int
    min []int
}

func Constructor() MinStack {
    return MinStack {
        stack: []int{},
        min: []int{math.MaxInt64},
    }
}

func (this *MinStack) Push(val int)  {
    this.stack = append(this.stack, val)
    this.min = append(this.min, min(val, this.min[len(this.min)-1]))
}

func (this *MinStack) Pop()  {
    this.stack = this.stack[:len(this.stack)-1]
    this.min = this.min[:len(this.min)-1]
}

func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1]

}

func (this *MinStack) GetMin() int {
    return this.min[len(this.min)-1]
}

func min(x, y int) int {
    if  x < y {
        return x
    }
    return y
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
```