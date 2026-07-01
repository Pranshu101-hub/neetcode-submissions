class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        while l<r:
            su = nums[l] + nums[r]
            if su == target: return [l+1,r+1]
            elif su>target: r-=1
            else: l+=1