# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
root.right = TreeNode(14)
root.right.left = TreeNode(12)
root.right.right = TreeNode(16)

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        self.res, self.pre = None, None
        self.traversal(pRootOfTree)
        return pRootOfTree

    def traversal(self, root):
        if not root: return
        self.traversal(root.left)
        if self.pre: self.pre.right = root
        root.left = self.pre
        self.pre = root
        self.traversal(root.right)

s = Solution()
s.Convert(root)