class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

class Solution:
    def Serialize(self, root):
        # write code here
        return self.serialize(root)[:-1]

    def serialize(self, root):
        res = ""
        if not root: return '#,'
        res += str(root.val) + ','
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res

    def Deserialize(self, s):
        root, i = self.deserialize(s.split(","),0)
        return root

    def deserialize(self, s, i):
        if i >= len(s) or s[i] == '#':
            return None, i + 1
        root = TreeNode(int(s[i]))
        root.left, i = self.deserialize(s, i+1)
        root.right, i = self.deserialize(s, i)
        return root, i

            


s = Solution()
print(s.Serialize(root))
print(s.Deserialize("8,9,5,#,#,7,#,#,9,7,#,#,5,#,#"))
