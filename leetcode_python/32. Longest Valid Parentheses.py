class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == '(': continue
            if s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            elif i > dp[i - 1] and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp) if s else 0