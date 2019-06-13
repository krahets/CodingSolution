# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        tmp = ListNode(0)
        head = tmp
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                tmp.next, pHead1 = pHead1, pHead1.next
            else:
                tmp.next, pHead2 = pHead2, pHead2.next
            tmp = tmp.next
        if not pHead1: tmp.next = pHead2
        else: tmp.next = pHead1
        return head.next