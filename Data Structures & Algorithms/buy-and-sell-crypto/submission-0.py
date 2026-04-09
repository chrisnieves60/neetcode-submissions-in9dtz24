class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #the way im thinking of it rn. brute force, is. by checking all possible buy/sell combinations. 
        #two loops, first represents buys, second represents sells. 

        #just constantly update max profit. 

        maxProfit = 0 

        for i in range(len(prices)): 
            for j in range(i+1, len(prices)): 
                profit = prices[j] - prices[i] 
                maxProfit = max(maxProfit, profit) 
        

        return maxProfit 