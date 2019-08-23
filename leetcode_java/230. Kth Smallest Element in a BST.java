class Solution {
    private int res = Integer.MAX_VALUE, count;
    public int kthSmallest(TreeNode root, int k) {
        count = k;
        inorder(root);
        return res;
    }
    private void inorder(TreeNode root) {
        if(root == null || count == 0) return;
        inorder(root.left);
        if(--count == 0) res = root.val;
        inorder(root.right);
    }
}