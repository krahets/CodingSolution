class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        res = tail = ListNode(0)
        pre, cur = None, head
        while cur:
            tmp = left = cur
            for _ in range(k - 1):
                tmp = tmp.next
                if not tmp:
                    tail.next = cur
                    return res.next
            for _ in range(k):
                nex, cur.next = cur.next, pre
                pre, cur = cur, nex
            tail.next, tail = pre, left
        tail.next = None
        return res.next