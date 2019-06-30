# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return
        tail, cut, length = head, head, 0
        while tail.next:
            tail = tail.next
            length += 1
        k %= length + 1
        for i in range(length - k): cut = cut.next
        tail.next = head
        res, cut.next = cut.next, None
        return res