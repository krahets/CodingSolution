class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not inorder: return
        root = TreeNode(preorder.pop(0))
        i = inorder.index(root.val)
        root.left = self.build(preorder, inorder[:i])
        root.right = self.build(preorder, inorder[i+1:])
        return root
