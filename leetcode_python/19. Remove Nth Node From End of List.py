class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        front = head
        for _ in range(n):
            front = front.next
        if not front: return head.next
        rear = head
        while front.next:
            front = front.next
            rear = rear.next
        rear.next = rear.next.next
        return head


# no leetcode solution