class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0, cost = Integer.MAX_VALUE;
        for (int price : prices) {
            cost = Math.min(cost, price);
            profit = Math.max(profit, price - cost);
        }
        return profit;
    }
}