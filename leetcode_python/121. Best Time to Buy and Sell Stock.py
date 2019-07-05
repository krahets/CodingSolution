class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(price, cost)
            profit = max(price - cost, profit)
        return profit