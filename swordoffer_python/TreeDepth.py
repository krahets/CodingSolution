# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot: return 0
        depth, roots= 0, [pRoot]
        while roots:
            for _ in range(len(roots)):
                r = roots.pop(0)
                if r.left: roots.append(r.left)
                if r.right: roots.append(r.right)
            depth += 1
        return depth