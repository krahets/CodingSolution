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
    
h1 = create_list([1,2,3,4])

class Solution:
    def swapPairs1(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        res = pre
        while head and head.next:
            nex = head.next.next
            pre.next = head.next
            pre = head
            head.next.next = head
            head = nex
        pre.next = head
        return res.next
    
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return
        nex = head.next
        head.next = self.swapPairs(nex.next)
        nex.next = head
        return nex
    


s = Solution()
print(s.swapPairs(h1))
