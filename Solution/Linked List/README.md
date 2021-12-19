# Linked List

[https://daniel820710.medium.com/leetcode-link-list-介紹-6d6dfe14a53b](https://daniel820710.medium.com/leetcode-link-list-%E4%BB%8B%E7%B4%B9-6d6dfe14a53b)

通常你只會知道某一個節點的位置，而題目通常會給你整個 List 的頭叫做 Head，而不知道的事情有：

1. 不知道整個 List 長度為何

2. 不知道第一個節點以外的其他節點的值與位置，而且沒辦法直接 Access

3. 連結是上一個節點接到下一個節點，以上圖來說如果現在3的位置，會不知道上一個是1

1. **不知道整個 List 的長度**可能必須先花 O(n) 的時間，Traverse 一遍 List 知道長度為何
2. **不知道上一個節點的位置**設定當前的指標 curr 以及 prev，就可以知道上一個節點的位置
3. **不知道最後一個節點(尾巴)的位置**可能必須先花 O(n) 的時間，Traverse 一輪，當 curr.next = NULL 時，及為 tail。
4. **不能直接 Access 節點**不過可以用一個 Map 去紀錄每一個 index 對應的 node，就好比能直接 Access 每一個節點 → 代價是 Space 需要用到 O(n)。
5. **更動指標的方法**A. 先找到要插入/交換的位置B. 將每一個節點的 Next 接好C. 更換每一個當前指標下面可以舉一個例子為 [0086. Partition List](https://leetcode.com/problems/partition-list)

# **小技巧**

1. **增加一個 node 叫做 pre_head 指向 head**通常題目會給你 *head* 指向第一個位置，但有時候第一個位置有時候會因題目要求不同，有可能更動，因此先新增一個 pre_head 指向 head，這樣就不會有 head 不見的問題。
2. **建立有意義名稱的指標使自己不搞混**有時候在 Traverse 整個 List 的時候，會因為不同題目有不同的作法，有時候會需要 while (curr) 有時候則是 while(curr.next)，甚至是 while(curr.next && curr.next.next)，因此有時候會錯亂這個 curr 到底指的是誰，因此可以多建立幾個指標像是 prev, next 等指標，來幫助你不會錯亂 while(curr.next) → while (next)。
3. **先把框架建立好，在寫裡面的邏輯**因為要解決一件事情的方法有無限多種可能，有好的框架可以幫助你更好的思緒該怎麼建構，