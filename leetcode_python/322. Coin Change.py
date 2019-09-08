class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for money in range(1, amount + 1):
            for coin in coins:
                if coin <= money:
                    dp[money] = min(dp[money], dp[money - coin])
            dp[money] += 1
        return dp[amount] if dp[amount] <= amount else -1
