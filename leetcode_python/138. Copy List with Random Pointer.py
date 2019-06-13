"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        pre, cur = Node(0, None, None), head
        while cur: # copy and merge.
            nex = cur.next
            pre.next = cur
            cur.next = Node(cur.val, None, None)
            pre = cur.next
            cur = nex
        cur = head
        while cur: # set the 'random' nodes.
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        cur, res = head, head.next
        while cur.next: # divide the two linked lists.
            nex = cur.next
            cur.next = nex.next
            cur = nex
        return res
        