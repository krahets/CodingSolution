class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not tin: return
        root = TreeNode(pre.pop(0))
        for i in range(len(tin)):
            if root.val == tin[i]: break
        root.left = self.reConstructBinaryTree(pre, tin[:i])
        root.right = self.reConstructBinaryTree(pre, tin[i+1:])
        return root


s = Solution()
root = s.reConstructBinaryTree([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
print(root)
