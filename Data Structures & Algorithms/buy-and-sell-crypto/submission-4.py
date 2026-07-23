class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        minp = float('inf')
        for i in prices:
            minp = min(minp,i)
            prof = max(prof,i-minp)
        return prof