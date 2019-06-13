# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

s = Solution()
s.maxDepth(root)