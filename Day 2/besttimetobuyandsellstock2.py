#122. Best Time to Buy and Sell Stock II
#day 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        pr= 0
        
        l = 0
        m = 1

        
        while m < len(prices):

            
            if prices[m] - prices[l] < 0:
                l = m

            
            else:
                pr +=(prices[m] - prices[l])
                l+=1
            
            m+=1
            
            
        return pr
        
