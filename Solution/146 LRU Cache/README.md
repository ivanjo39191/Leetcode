# 146. LRU Cache

Column: January 12, 2022
Tags: Meduim
s: published
status: Complete

# 146. LRU Cache

## Question

Design a data structure that follows the constraints of a **[Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

請你設計並實現一個滿足 LRU (最近最少使用) 緩存 約束的數據結構。實現 LRUCache 類： LRUCache(int capacity) 以 正整數 作為容量 capacity 初始化 LRU 緩存 int get(int key) 如果關鍵字 key 存在於緩存中，則返回關鍵字的值，否則返回 -1 。 void put(int key, int value) 如果關鍵字 key 已經存在，則變更其數據值 value ；如果不存在，則向緩存中插入該組 key-value 。如果插入操作導致關鍵字數量超過 capacity ，則應該 逐出 最久未使用的關鍵字。函數 get 和 put 必須以 O(1) 的平均時間複雜度運行。

**Example 1:**

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

**Constraints:**

- `1 <= capacity <= 3000`
- `0 <= key <= 104`
- `0 <= value <= 105`
- At most 2 `* 105` calls will be made to `get` and `put`.

## 相關說明

使用 hashmap 與 雙向鏈錶。

## 思路1

### 解題詳解:

定義 ListNode 包含四個值，key, value, pre, next。

定義 LRUCache 包含三個方法 get, put, move_node_to_tail。

初始化 LRUCache，

self.capacity = capacity 為緩存最大長度
self.hashmap = {}            初始化哈希表
self.head = ListNode()    頭節點
self.tail = ListNode()        尾節點
self.head.next = self.tail  頭節點後接上尾節點
self.tail.pre = self.head    尾節點前接上頭節點

1. put 方法

    為放入新的資料進入緩存，外部傳入兩個參數值分別為 key, value

    * hashmap 判斷 key 存在，

        該 key 儲存的 node 中的 value 值

        調用 move_node_to_tail 將該 key 移動到 node 尾端

    * hashmap 判斷 key 不存在，

        * 若 hashmap 長度已達 capacity 緩存最大長度

            hashmap pop 移除雙向鏈表的頭節點的下一個節點

            頭節點的 next 接到 next.next

            新的 next 的 pre 接到 head

        使用外部傳入的 key, value 建立新的 node

        將新 node 插入雙向鏈表的尾節點前

        新 node 的 pre 接到尾節點的前一個節點

        新 node 的 next 接到尾節點

        尾節點的前一個節點的 next 接到 node

        尾節點的前一個節點換為 node

        最後在 hashmap[key] 儲存 node 

    結束 put 方法

1. move_node_to_tail 方法
    
    將 node 移至雙向鏈表的尾端，外部傳入一個參數值為 key
    
    從 hashmap[key] 取得 node 
    
    1.  將 node 從原本的位置移除
        
        node 前一個節點的 next 改為 node 後一個節點
        
        node 後一個節點的 pre 改為 node 前一個節點
        
    2. 將 node 插入到尾節點前
        
        node 的 pre 改為尾節點的前一個節點
        
        node 的 next 改為尾節點
        
        尾節點的前一個節點的 next 改為 node
        
        尾節點的 pre 改為 node
        
2.  get 方法
    
    取得傳入 key 的 value，外部傳入一個參數值為 key，若沒有該 key 則回傳 -1
    
    判斷該 key 在 hashmap
    
    調用 move_node_to_tail 將 key 移至雙向鏈表的尾端
    
    返回該 hashmap[key] 的個 node 中的 value
    
    判斷該 key 不在 hashmap
    
    返回 -1
    

### Big-O

時間複雜度 O(1)

空間複雜度 O(capacity) ，因為 hashmap 與雙向鏈表最多儲存 capacity + 1 個元素

### 代碼

語言: python3

執行用時: 596ms 

內存消耗: 72 MB

```python
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_node_to_tail(self, key):
        node = self.hashmap[key]
        # 移除
        node.pre.next = node.next
        node.next.pre = node.pre
        # 插入
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_tail(key)
            return self.hashmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.pre = self.head
            node = ListNode(key=key, value=value)
            node.pre = self.tail.pre
            node.next = self.tail
            self.tail.pre.next = node
            self.tail.pre = node
            self.hashmap[key] = node
```