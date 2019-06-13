# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here 
        p1, p2, step= pHead, pHead, 0
        while p1 != p2 or step == 0:
            if not p1.next or not p2.next.next: return None
            p1, p2 = p1.next, p2.next.next
            step += 1
        p1, p2 = pHead, pHead
        for _ in range(step):
            p1 = p1.next
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1