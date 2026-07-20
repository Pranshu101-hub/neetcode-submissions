class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su%2: return False
        tar = su//2
        dp = [0]*(tar+1)
        dp[0] = 1
        for i in nums:
            for j in range(tar,i-1,-1):
                dp[j] = dp[j] or dp[j-i]
        print(dp) 
        if dp[-1]: return True
        return False