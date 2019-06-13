# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        length1 = length2 = 0
        head1, head2 = pHead1, pHead2
        while head1:
            head1 = head1.next
            length1 += 1
        while head2:
            head2 = head2.next
            length2 += 1
        [k, lon, sho] = [length1 - length2, pHead1, pHead2] if length1 > length2 else [length2 - length1, pHead2, pHead1]
        for _ in range(k):
            lon = lon.next
        while lon:
            if lon == sho:
                return lon
            lon, sho = lon.next, sho.next
        