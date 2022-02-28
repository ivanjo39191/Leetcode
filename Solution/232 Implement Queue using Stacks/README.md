# 232. Implement Queue using Stacks

Column: January 12, 2022
Tags: Easy
s: published
status: Complete

# **232. Implement Queue using Stacks**

## Question

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Notes:**

- You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

請你僅使用兩個棧實現先入先出隊列。隊列應當支持一般隊列支持的所有操作（push、pop、peek、empty）： 

實現 MyQueue 類： 

1. void push(int x) 將元素 x 推到隊列的末尾 
2. int pop() 從隊列的開頭移除並返回元素 

int peek() 返回隊列開頭的元素 

boolean empty() 如果隊列為空，返回 true ；否則，返回 false 

說明： 你 只能 使用標準的棧操作 —— 也就是只有 push to top, peek

**Example 1:**

```
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```

**Constraints:**

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
- All the calls to `pop` and `peek` are valid.

**Follow-up:**
 Can you implement the queue such that each operation is **[amortized](https://en.wikipedia.org/wiki/Amortized_analysis)**
 `O(1)`
 time complexity? In other words, performing `n`
 operations will take overall `O(n)`
 time even if one of those operations may take longer.

## 相關說明

O(1) 實現隊列，需要使用兩個 stack 。

stack_in 彈出放進 stack_out ，stack_out 出棧即為出隊。

## 思路1

### 解題詳解:

初始化 stack_in, stack_out 兩個棧。

push 方法：

stack_in append 加上新元素

empty 方法：

若 stack_in, stack_out 其中一個為空則為 True，反之為  False

pop 方法：

若 empty 為 True 返回 None，

若 stack_out 有值，則彈出並返回，

反之，將 stack_in 迴圈彈出放入 stack_out，

迴圈結束後將 stack_out 彈出並返回。

peek 方法：

呼叫 pop 方法，且儲存彈出的值，

將彈出的值重新加入 stack_out，

返回該彈出的值。

### Big-O

時間複雜度 O(1)， push 和 empty 為 O(1)，pop 和 peek 為均攤 O(1)，對於每個元素至多入棧岀棧各兩次，故均攤複雜度為O(1)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 38ms 

內存消耗: 14 MB

```python
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        
    def push(self, x: int) -> None:
        self.stack_in.append(x)
        
    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        res = self.pop()
        self.stack_out.append(res)
        return res
            
    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```