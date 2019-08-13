class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(dp)): dp[i][0] = i
        for i in range(1, len(dp[0])): dp[0][i] = i
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) if word1[i-1] != word2[j-1] else dp[i-1][j-1]
        return dp[-1][-1]

s = Solution()
s.minDistance("horse", "ros")