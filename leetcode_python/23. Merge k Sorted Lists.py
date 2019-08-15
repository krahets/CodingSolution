class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while len(lists) > 1:
            lists.append(self.merge(lists.pop(0), lists.pop(0)))
        return lists[0] if lists else None
    def merge(self, h1, h2):
        res = head = ListNode(0)
        while h1 and h2:
            if h1.val <= h2.val: head.next, h1 = h1, h1.next
            else: head.next, h2 = h2, h2.next
            head = head.next
        head.next = h1 if not h2 else h2
        return res.next