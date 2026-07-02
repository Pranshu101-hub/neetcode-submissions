class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        st,end = 0,1
        maxi = 0
        print(len(s))
        while end<len(s):
            if s[end] not in s[st:end]:
                end+=1
            else:
                while s[end] in s[st:end]:
                    st+=1
            maxi = max(maxi,end-st)
        return maxi