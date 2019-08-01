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
    private TreeNode pre;
    public void flatten(TreeNode root) {
        if(root == null) return;
        if(pre != null){
            pre.right = root;
            pre.left = null;
        }
        pre = root;
        TreeNode right = root.right;
        flatten(root.left);
        flatten(right);
    }
}