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
    
h1 = create_list([-10,-9,-6,-4,1,9,9])
h2 = create_list([-5,-3,0,7,8,8])

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        res = head
        while l1 and l2:
            if l1.val <= l2.val: head.next, l1 = l1, l1.next
            else: head.next, l2 = l2, l2.next
            head = head.next
        head.next = l1 if not l2 else l2
        return res.next

s = Solution()
print(print_list(s.mergeTwoLists(h1,h2)))

        

            
                

            