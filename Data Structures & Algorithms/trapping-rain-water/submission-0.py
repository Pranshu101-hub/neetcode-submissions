class Solution:
    def trap(self, height: List[int]) -> int:
        st,end,lm,rm,tot = 0, len(height)-1,0,0,0

        while st<end:
            rm = max(rm,height[end])
            lm = max(lm,height[st])
            if lm > rm:
                tot += rm - height[end]
                end -= 1
            else:
                tot += lm - height[st]
                st += 1
        return tot

