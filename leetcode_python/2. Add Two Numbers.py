# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_list(arr):
    head = ListNode(arr[0])
    node = head
    for a in arr[1:]:
        node.next = ListNode(a)
        node = node.next
    return head

def print_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
    
h1 = create_list([1,8])
h2 = create_list([1])

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        res = head
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            tmp = num1 + num2 + carry
            carry = 1 if tmp >= 10 else 0
            head.next = ListNode(tmp % 10)
            head = head.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: head.next = ListNode(1)
        return res.next

s = Solution()
s.addTwoNumbers(h1,h2)

            