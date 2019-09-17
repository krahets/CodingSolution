class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        dp = [1] * len(s)
        for i in range(1, len(s)):
            if s[i] == '0':
                if '0' < s[i - 1] <='2': dp[i] = dp[i - 2]
                else: return 0
            elif s[i - 1] == '1' or (s[i] <= '6' and '0' < s[i - 1] <='2'):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]