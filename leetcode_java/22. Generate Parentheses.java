class Solution {
    List<String> res = new ArrayList<String>();
    public List<String> generateParenthesis(int n) {
        dfs(n, 0, 0, "");
        return res;       
    }
    private void dfs(int n, int i, int j, String tmp) {
        if(i + j == 2 * n) {
            res.add(tmp);
            return;
        }
        if(i < n) dfs(n, i + 1, j, tmp + '(');
        if(j < i) dfs(n, i, j + 1, tmp + ')');
    }
}