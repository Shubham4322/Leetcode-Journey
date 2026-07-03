class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=prices[0]
        res=0
        for i in range(len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            if (prices[i]-mi) >res:
                res= prices[i]-mi
        return res

