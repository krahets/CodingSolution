class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for(int money = 1; money <= amount; money++) {
            for(int coin : coins) {
                if(coin <= money)
                    dp[money] = Math.min(dp[money], dp[money - coin]);
            }
            dp[money]++;
        }
        return dp[amount] <= amount ? dp[amount] : -1;
    }
}