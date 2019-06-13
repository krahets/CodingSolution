class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(8)
root.left = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(7)
root.right.right = TreeNode(5)

class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        self.res = []
        self.reprint([pRoot], False)
        return self.res
    def reprint(self, roots, reverse):
        if not roots: return
        tmp = []
        for _ in range(len(roots)):
            r = roots.pop(0)
            tmp.append(r.val)
            if r.left: roots.append(r.left)
            if r.right: roots.append(r.right)
        if reverse: tmp.reverse()
        self.res.append(tmp)
        self.reprint(roots, not reverse)
            


s = Solution()
s.Print(root)


