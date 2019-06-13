# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.getDepth(pRoot) != -1
    def getDepth(self, pRoot):
        if not pRoot: return 0
        dl = self.getDepth(pRoot.left)
        dr = self.getDepth(pRoot.right)
        return max(dl,dr) + 1 if dl != -1 and dr != -1 and -2 < dl - dr < 2 else -1