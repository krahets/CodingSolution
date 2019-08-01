import java.util.ArrayList;
import java.util.List;

import javax.swing.tree.TreeNode;

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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root == null) return new ArrayList<>();
        List<TreeNode> cur = new ArrayList<>(), nex = new ArrayList<>();
        cur.add(root);
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        while(cur.size() > 0){
            for(TreeNode r : cur) {
                tmp.add(r.val);
                if(r.left != null) nex.add(r.left);
                if(r.right != null) nex.add(r.right);
            }
            res.add(tmp);
            cur = nex;
            tmp = new ArrayList<>();
            nex = new ArrayList<>();
        }
        return res;
    }
}