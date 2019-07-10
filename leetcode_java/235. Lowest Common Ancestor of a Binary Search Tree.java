class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int pv = Math.min(p.val, q.val), qv = Math.max(p.val, q.val);
        while (root != null) {
            if (root.val < pv) root = root.right;
            else if (root.val > qv) root = root.left;
            else return root;
        }
        return null;
    }
}