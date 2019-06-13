class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k < 1: return
        node1, node2 = head, head
        for _ in range(k):
            if not node1: return
            node1 = node1.next
        while node1:
            node1, node2 = node1.next, node2.next
        return node2