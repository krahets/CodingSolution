# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

s = Solution()
print(s.kthSmallest(root, 3))


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res, self.count = None, k
        def inorder(root):
            if not (root and self.count): return
            inorder(root.left)
            self.count -= 1
            if not self.count: self.res = root.val
            inorder(root.right)
        inorder(root)
        return self.res
        
    