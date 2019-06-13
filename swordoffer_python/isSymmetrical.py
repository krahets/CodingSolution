class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(8)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(7)
root.right.right = TreeNode(5)


class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot: return True
        return self.match(pRoot.left, pRoot.right)
    def match(self, lef, rig):
        if not lef and not rig: return True
        if not lef or not rig or lef.val != rig.val: return False
        return self.match(lef.left, rig.right) and self.match(lef.right, rig.left)

s = Solution()
print(s.isSymmetrical(root))