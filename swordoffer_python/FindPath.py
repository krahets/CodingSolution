class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)
root.right = TreeNode(12)


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        self.res, self.path = [], []
        self.search(root, expectNumber)
        return self.res

    def search(self, root, target):
        if not root: return
        target -= root.val
        self.path.append(root.val)
        if not (root.left or root.right or target):
            self.res.append([p for p in self.path])
        self.search(root.left, target)
        self.search(root.right, target)
        self.path.pop()


s = Solution()
print(s.FindPath(root, 22))
