class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = 0
        dp = [False]*(len(nums)+1)
        dp[0] = True
        for i in range(len(nums)):
            if dp[i] == True:
                maxi = max(maxi,i+nums[i])
                print(maxi)
                if maxi >= (len(nums)-1):
                    return True
                for j in range(i+1,i+1+nums[i]):
                    dp[j] = True 
                
        print(dp)
        return False