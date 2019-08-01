# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)


class Solution:
    def __init__(self):
        self.pre = None
    def flatten(self, root: TreeNode) -> None:
        if not root: return
        if self.pre: self.pre.right, self.pre.left = root, None
        self.pre = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)

s = Solution()
s.flatten(root)