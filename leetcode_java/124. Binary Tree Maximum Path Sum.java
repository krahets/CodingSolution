/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        maxPath(root);
        return max;
    }
    private int maxPath(TreeNode root){
        if(root == null) return 0;
        int left = maxPath(root.left);
        int right = maxPath(root.right);
        max = Math.max(root.val + left + right, max);
        int tmp = Math.max(left, right) + root.val;
        return tmp > 0 ? tmp : 0;
    }
}