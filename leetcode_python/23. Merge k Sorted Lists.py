# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                r = None if i == len(lists) - 1 else lists[i+1]
                tmp.append(self.merge(lists[i], r))
            lists = tmp
        return lists[0] if lists else None

    def merge(self, h1, h2):
        res = head = ListNode(0)
        while h1 and h2:
            if h1.val <= h2.val:
                head.next = h1
                h1 = h1.next
            else:
                head.next = h2
                h2 = h2.next
            head = head.next
        head.next = h1 if not h2 else h2
        return res.next