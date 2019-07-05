# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return
        pre = None
        while head.next:
            nex = head.next
            head.next = pre
            pre = head
            head = nex
        head.next = pre
        return head