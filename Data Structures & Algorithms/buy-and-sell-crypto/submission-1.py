class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #the way im thinking of it rn. brute force, is. by checking all possible buy/sell combinations. 
        #two loops, first represents buys, second represents sells. 

        #just constantly update max profit. 

        l, r = 0, 1
        maxProfit = 0 
        while r < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            #if r is cheaper than l, we found a cheaper day... 
            if prices[r] < prices[l]: 
                l = r 
                r += 1 
                continue

            r += 1
        
        return maxProfit
