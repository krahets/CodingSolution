# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        self.dfs(root, p, q)
        return self.res
    def dfs(self, root, p, q):
        if not root: return 0
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right,p ,q)
        mid = int(root == p or root == q)
        if left + right + mid > 1: self.res = root
        return left or right or mid