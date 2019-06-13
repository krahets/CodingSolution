class Solution {
    long tmp = Long.MIN_VALUE;
    public boolean isValidBST(TreeNode root) {
        if(root == null) return true;
        if (isValidBST(root.left)) {
            if (tmp < root.val) {
                tmp = root.val;
                return isValidBST(root.right);
            }
        }
        return false;
   }
}