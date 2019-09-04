// Recursive.
class Solution {
    int ls, lp;
    public boolean isMatch(String s, String p) {
        ls = s.length();
        lp = p.length();
        return match(s, p, 0, 0);
    }
    private boolean match(String s, String p, int i, int j) {
        if(j == lp) return i == ls;
        if(j < lp - 1 && p.charAt(j + 1) == '*') {
            if(i < ls && (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)))
                return match(s, p, i + 1, j) || match(s, p, i, j + 2);
            return match(s, p, i, j + 2);
        }
        if(i < ls && (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)))
            return match(s, p, i + 1, j + 1);
        return false;
    }
}

// Dynamic programming.
class Solution {
    public boolean isMatch(String s, String p) {
        int ls = s.length(), lp = p.length();
        boolean[][] dp = new boolean[ls + 1][lp + 1];
        dp[0][0] = true;
        for(int j = 2; j <= lp; j++)
            dp[0][j] = dp[0][j - 2] && p.charAt(j - 1) == '*';
        for(int i = 1; i <= ls; i++) {
            for(int j = 1; j <= lp; j++) {
                int m = i - 1, n = j - 1;
                if(p.charAt(n) == '*')
                    dp[i][j] = dp[i][j - 2] || dp[i - 1][j] && 
                        (s.charAt(m) == p.charAt(n - 1) || p.charAt(n - 1) == '.');
                else if(s.charAt(m) == p.charAt(n) || p.charAt(n) == '.') 
                    dp[i][j] = dp[i - 1][j - 1];
            }
        }
        return dp[ls][lp];
    }
}