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
    def __init__(self):
        self.tmp = -float('inf')
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        if not self.isValidBST(root.left): return False
        if self.tmp >= root.val: return False
        self.tmp = root.val
        if not self.isValidBST(root.right): return False



s = Solution()
print(s.isValidBST(root))
        