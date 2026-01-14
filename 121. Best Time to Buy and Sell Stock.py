# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        b=0
        s=1
        profit=0
        while s<len(prices):
            temp = prices[s]-prices[b]
            if prices[s]>prices[b]:
                profit = max(temp,profit)
            else:
                b=s
            s+=1
       
        return profit
