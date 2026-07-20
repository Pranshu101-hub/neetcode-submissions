class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d: d[i] += 1
            else: d[i] = 1
        print(d)
        arr,res = [],[]
        for num, cnt in d.items():
            arr.append([cnt, num])
        arr = sorted(arr, reverse = True)
        for i in range(k):
            res.append(arr[i][1])
        return res