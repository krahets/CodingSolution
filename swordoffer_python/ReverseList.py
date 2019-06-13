# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        return self.NextNode(pHead.next,pHead)
    def NextNode(self, node, pre_node):
        if node.next != None:
            self.NextNode(node.next,node)
        node.next = pre_node
        return node

s=Solution()