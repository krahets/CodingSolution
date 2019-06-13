# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, head):
        # write code here
        if not head: return
        h = head
        while h:
            tmp = RandomListNode(h.label)
            nex = h.next
            h.next, h, tmp.next = tmp, nex, nex
        h = head
        while h.next.next:
            if h.random: h.next.random = h.random.next
            h = h.next.next
        h, res = head, head.next
        while h.next:
            tmp = h.next
            h.next, h = h.next.next, tmp
        return res