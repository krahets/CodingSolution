# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        cur, nex, tmp, res = [root], [], [], []
        while cur:
            for r in cur:
                tmp.append(r.val)
                if r.left: nex.append(r.left)
                if r.right: nex.append(r.right)
            res.append(tmp[:])
            cur, nex, tmp = nex, [], []
        return res
            

