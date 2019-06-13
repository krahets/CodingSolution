class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(8)
root.left = TreeNode(6)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right = TreeNode(10)
root.right.left = TreeNode(9)
root.right.right = TreeNode(11)

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.res, self.k, self.count = None, k, 0
        self.recur(pRoot)
        return self.res
    def recur(self, root):
        if not root: return
        self.recur(root.left)
        if self.count == self.k - 1:
            if not self.res: self.res = root
            return
        self.count += 1
        self.recur(root.right)

s = Solution()
print(s.KthNode(root, 2))
        