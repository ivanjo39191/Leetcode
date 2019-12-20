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
        