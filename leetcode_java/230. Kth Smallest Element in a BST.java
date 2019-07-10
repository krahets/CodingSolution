class Solution {
    private int res = Integer.MAX_VALUE, count;
    public int kthSmallest(TreeNode root, int k) {
        count = k;
        inorder(root);
        return res;
    }
    private void inorder(TreeNode root) {
        if(root != null) {
            inorder(root.left);
            if(res != Integer.MAX_VALUE) return;
            if(--count == 0) res = root.val;
            inorder(root.right);
        }
    }
}