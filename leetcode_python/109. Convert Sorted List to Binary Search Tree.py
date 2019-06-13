# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.head = None
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        n, self.head = 0, head
        while head:
            head = head.next
            n += 1
        return self.to_bst(0, n - 1)
    def to_bst(self, left, right):
        if left > right: return
        m = (left + right) // 2
        left_child = self.to_bst(left, m - 1)
        father = TreeNode(self.head.val)
        self.head = self.head.next
        father.left = left_child
        father.right = self.to_bst(m + 1, right)
        return father
