#Problem no. 121
#Problem of Day 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for i in range (len(prices)):
            diff=prices[i]-buy
            buy=min(buy,prices[i])
            profit=max(profit,diff)
        return profit
