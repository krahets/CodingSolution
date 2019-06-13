# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        if not pNode.next: return None
        if pNode.next.left == pNode: return pNode.next
        while pNode.next.right == pNode:
            pNode = pNode.next
            if not pNode.next: return None
        return pNode.next