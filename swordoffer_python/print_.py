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
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res = []
        self.line(res, [pRoot])
        return res

    def line(self, res, roots):
        tmp, re = [], []
        for r in roots:
            re.append(r.val)
            if r.left: tmp.append(r.left)
            if r.right: tmp.append(r.right)
        if tmp:
            res.append(re)
            self.line(res, tmp)

s = Solution()
s.Print(root)
        