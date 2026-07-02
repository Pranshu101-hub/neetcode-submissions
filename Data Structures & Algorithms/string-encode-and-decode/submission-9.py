class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return 'qwerty'
        sn = ""
        for i in range(len(strs)):
            if i == len(strs) - 1: sn += strs[i]
            else: sn += strs[i]+'[['
        return sn
    def decode(self, s: str) -> List[str]:
        if s == "qwerty": return []
        s = s.split("[[")
        return s
