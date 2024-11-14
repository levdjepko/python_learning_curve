class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # implement a rolling window to track the lowest and highest item so far
        # then, go over the entire list in one pass and get the difference
        # O(n) time complexity, O(n) space complexity
        buy_price = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            profit = max(profit, price - buy_price)   
        return profit     

        
