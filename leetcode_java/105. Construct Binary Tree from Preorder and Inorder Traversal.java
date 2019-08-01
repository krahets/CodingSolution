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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return build(preorder, 0, inorder, 0, inorder.length);
    }
    private TreeNode build(int[] preorder, int p, int[] inorder, int i, int j){
        if(i >= j) return null;
        TreeNode root = new TreeNode(preorder[p]);
        int k = 0;
        while(inorder[k] != root.val) k++;
        root.left = build(preorder, p + 1, inorder, i, k);
        root.right = build(preorder, p + 1 + k - i, inorder, k + 1, j);
        return root;
    }
}