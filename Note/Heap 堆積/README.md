# Heap 堆積

## 一、何謂堆積 (heap)?

堆積是一種特別的完全二元樹，所有內部節點被完全填充，又分為最小推積（min heap）、最大堆積（max heap）

特性定義：「給定堆積中任意節點P和C，若P是C的母節點，那麼P的值會小於等於（或大於等於）C的值」

最小堆積：完全二元樹所有的父節點都比子節點要小，根節點是最大值，就屬於最小堆積。

最大堆積：完全二元樹所有的父節點都比子節點要大，堆節點是最小值，則為最大堆積。

常見的堆積有二元堆積、斐波那契堆積等。

## 二、分析堆積

```python
# 最大堆積 父節點 大於 子節點
          77(0)
       /         \
     67(1)       58(2)
    /    \       /    \
  26(3)  17(4)  7(5)  1(6)

# 最小堆積 父節點 小於 子節點
           1(0)
       /         \
     7(1)        17(2)
    /    \       /    \
  26(3)  58(4)  67(5)  77(6)

```



父節點為 0 ，子節點為 1、2

父節點為 1 ，子節點為 3、4

父節點為 2 ，子節點為 5、6

父節點為 3 ，子節點為 7、8

由此可以分析出：

父節點為 i ，左節點為 2i +1 ，右節點為 2i +2

反之，

左節點為 i ，父節點為 (i - 1)/2

右節點為 i ，父節點為 (i - 2)/2

## 三、堆積化 (Heapify)

堆積化是以進入的父節點作為起始，若有節點交換就向下繼續進行堆積，最後只有被交換過的節點符合堆積特性，無法將整個堆積都化成最大堆積、最小堆積

1. 遍歷父節點
2. 比較所有節點，最大給父節點
3. 遞迴成形

```python
"""
arr：需要排序的列表
n：列表長度
i：開始節點
"""
def heapify(arr: list, n: int, i: int) -> list:
    if i >= n:
        return
    largest = i
    lchild = 2 * i + 1
    rchild = 2 * i + 2

    if lchild < n and arr[largest] < arr[lchild]:
        largest = lchild
    if rchild < n and arr[largest] < arr[rchild]:
        largest = rchild
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

"""
          3(0)
       /        \
     2(1)       4(2)
    /    \      /   \
8(3)    1(4)  10(5)   7(6)
"""

arr = [3,2,4,8,1,10,7]
print('----brfore heapify-----')
print(arr)
heapify(arr, n , 0)  # 從根節點開始
print('----after heapify-----')
print(arr)

"""
----brfore heapify-----
[3, 2, 4, 8, 1, 10, 7]
----after heapify-----
[4, 2, 10, 8, 1, 3, 7]
"""
```


## 四、建立堆積

建立堆積的步驟可將整個二元樹化為最大堆積、最小堆積

從最後一個非葉子節點開始往根節點迴圈，逐步向上進行堆積化

```python
def buildHeap(arr, n):

    # 取得最後一個非葉子節點
    start = n // 2 - 1;

    for i in range(start, -1, -1):
        heapify(arr, n, i)

arr = [3,2,4,8,1,10,7]
n = len(arr)
print('----brfore buildHeap-----')
buildHeap(arr, n)
print('----after buildHeap-----')
print(arr)

"""
----brfore buildHeap-----
[3, 2, 4, 8, 1, 10, 7]
----after buildHeap-----
[10, 8, 7, 2, 1, 4, 3]
"""
```


## 五、堆積排序

首先進行一次建立堆積，此時根節點必定為最大、最小元素，將此元素交換至最後一個節點，形成有序區。

堆積長度扣掉建立堆積的一個有序區元素，剩下無序區元素由 n -1 進行迴圈。

將此時的根節點進行堆積化，，調整後的根節點必定又為最大最小元素，同樣將此元素交換至最後一個節點並進入有序區，直至迴圈結束即完成堆積排序。

```python
def heap_sort(arr):
    n = len(arr)
    # 建立堆積
    buildHeap(arr, n)
    # 交換一次後，進行迴圈堆積化與再次交換
    for i in range(n-1, 0, -1):
        arr[0], arr[i], = arr[i], arr[0]
        heapify(arr, i, 0)

print('----brfore heap_sort-----')
print(arr)
heap_sort(arr)
print('----after heap_sort-----')
print(arr)

"""
----brfore heap_sort-----
[10, 8, 7, 2, 1, 4, 3]
----after heap_sort-----
[1, 2, 3, 4, 7, 8, 10]
"""
```

## 六、執行效能分析

堆積排序是非穩定的排序算法

最佳時間複雜度：O(n log n)

最壞時間複雜度：O(n log n)

平均時間複雜度：O(n log n)

空間複雜度：O(1)

## 七、參考資料

[https://www.cnblogs.com/chengxiao/p/6129630.html](https://www.cnblogs.com/chengxiao/p/6129630.html)

[https://blog.csdn.net/qq_14959801/article/details/53264569](https://blog.csdn.net/qq_14959801/article/details/53264569)

[https://chihokyo.com/post/18/](https://chihokyo.com/post/18/)

[https://www.geeksforgeeks.org/building-heap-from-array/](https://www.geeksforgeeks.org/building-heap-from-array/)

[https://blog.csdn.net/guoweimelon/article/details/50904346](https://blog.csdn.net/guoweimelon/article/details/50904346)

[https://zh.wikipedia.org/wiki/堆積](https://zh.wikipedia.org/wiki/%E5%A0%86%E7%A9%8D)

[https://zhuanlan.zhihu.com/p/45725214](https://zhuanlan.zhihu.com/p/45725214)