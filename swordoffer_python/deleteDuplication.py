class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def cre_linked_list(arr):
    head = ListNode(arr[0])
    res = head
    for a in arr[1:]:
        tmp = ListNode(a)
        head.next, head = tmp, tmp
    return res


head = cre_linked_list([1, 1, 2, 2, 3, 3, 4, 4])


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return
        pre, h1, h2 = ListNode(pHead.val - 1), pHead, pHead
        res, pre.next = pre, h2
        while h2:
            while h2 and h1.val == h2.val:
                tmp, h2 = h2, h2.next
            if tmp == h1: pre.next, pre = tmp, h1
            h1 = h2
        pre.next = None
        return res.next
 
    def deleteDuplication1(self, pHead):
        # write code here
        dic, head = {}, pHead
        while head:
            if head.val not in dic:
                dic[head.val] = []
            dic[head.val].append(head)
            head = head.next
        head, pre, res = pHead, None, None
        while head:
            tmp = head.next
            if len(dic[head.val]) == 1:
                if not res:
                    res = head
                else:
                    pre.next = head
                pre, head.next = head, None
            head = tmp
        return res


s = Solution()
print(s.deleteDuplication(head))
