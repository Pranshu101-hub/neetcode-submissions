class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main = {}
        for i in strs:
            d = [0] * 26
            for j in i:
                d[ord(j) - ord('a')] += 1
            d = tuple(d)
            if d in main:
                main[d].append(i)
            else:
                main[d] = [i]
            print(d)
        return list(main.values())