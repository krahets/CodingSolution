class Solution {
    public boolean isSymmetric(TreeNode root) {
        return match(root, root);
    }
    private boolean match(TreeNode l, TreeNode r) {
        if (l == null && r == null) return true;
        if (l == null || r == null) return false;
        return l.val == r.val && 
            match(l.left, r.right) && 
            match(l.right, r.left);
    }
}