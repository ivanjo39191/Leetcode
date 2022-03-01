# 225. Implement Stack using Queues

Column: March 1, 2022
Tags: Easy
s: published
status: Complete

# **225. Implement Stack using Queues**

## Question

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

**Notes:**

- You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

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
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

**Constraints:**

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.
- All the calls to `pop` and `top` are valid.

**Follow-up:** Can you implement the stack using only one queue?

## 相關說明

python 使用雙向佇列，可使用 popleft() 與索引

## 思路1

### 解題詳解:

初始化 queue_in, queue_out 雙向佇列。

push 方法：

queue_in 使用 append 加上新元素

empty 方法：

若 queue_in 為空返回 True

pop 方法：

若 empty 為 True 返回 None，

迴圈使用 popleft() 彈出 queue_in 至倒數第二個元素，並將彈出的元素存放至 queue_out。

將 queue_in 與 queue_out 互換，

使用 popleft() 彈出 queue_out 剩餘的最後一個元素並返回。

top 方法：

若 empty 為 True 返回 None，

使用索引返回最後一個元素。

### Big-O

時間複雜度 pop 為 O(n)，其餘為 O(1)

空間複雜度 O(n)

### 代碼

語言: python3

執行用時: 28ms 

內存消耗: 15.2 MB

```python
from collections import deque

class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)
        

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue_in[-1]
        

    def empty(self) -> bool:
        return not self.queue_in
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```