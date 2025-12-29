class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 873923
        maxp = 0 
        for price in prices:
            mp = min(mp,price)
            maxp = max(maxp, price-mp)
        return maxp
        
