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
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root: return []
        res, tmp = [], [root]
        while tmp:
            t = tmp.pop()
            res.append(t.val)
            if t.left: tmp.append(t.left)
            if t.right: tmp.append(t.right)
        return res
        

s = Solution()
s.PrintFromTopToBottom(root)