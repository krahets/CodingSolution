# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root: return
        
    def mirror(self, l, r):
        
        self.mirror(l.left, l.right)
        self.mirror(r.left, r.right)