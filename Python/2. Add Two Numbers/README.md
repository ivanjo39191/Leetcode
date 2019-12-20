# 2. Add Two Numbers

[Question](#question)  
[中文題目](#question_zh_hant)  
[解法](#answer1)  
[思路](#think1)  
[Big-O](#bigo)  
[代碼](#code)  
 

<a name="question"></a>
## Question
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two   numbers and return it as a linked list.  
You may assume the two numbers do not contain any leading zero, except the number 0 itself.  
  
<a name="question_zh_hant"></a>
## 題目
有兩個連結陣列分別代表兩個非負整數，他們的位數是反向儲存(越前面的節點位數越低)，毎一個節點代表一個位數，將這兩個連結陣列加總後以連結陣列形式回傳。  
範例：  
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)  
Output: 個位數為2與5，相加為7 ； 十位數為4+6 = 10，需要進位 ； 百位數為3 + 4 + 1(進位) = 8，結果為 7->0->8  

<a name="answer1"></a>
## 解法1  

<a name="think1"></a>
### 思路  
判斷input是否存在，轉為列表進行反轉  
轉為字串後相加，再進行反轉  
最後將結果轉為鏈表  

<a name="bigo"></a>
### Big-O  
 時間複雜度 O(N)  
 空間複雜度 O(N)  


<a name="code"></a>
### 代碼  

        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, x):
        #         self.val = x
        #         self.next = None

        class Solution:
            def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
                if not l1:
                    return l2
                if not l2:
                    return l1
                l1_list, l2_list = [l1.val], [l2.val]
                while l1.next:
                    l1_list.append(l1.next.val)
                    l1 = l1.next
                while l2.next:
                    l2_list.append(l2.next.val)
                    l2 = l2.next
                num1 = ''.join([str(i) for i in l1_list[::-1]])
                num2 = ''.join([str(i) for i in l2_list[::-1]])
                ans = str(int(num1) + int(num2))[::-1]
                res = ListNode(int(ans[0]))
                run_res = res
                for i in range(1, len(ans)):
                    run_res.next = ListNode(int(ans[i]))
                    run_res = run_res.next


                return res
