class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        nums = set(nums)
        
        curr,st = 1,1
        for i in nums:
            if i-1 not in nums: 
                curr = 1
                while (i+curr) in nums:
                    curr += 1

                print(curr,st)
                st = max(st,curr)
        return st