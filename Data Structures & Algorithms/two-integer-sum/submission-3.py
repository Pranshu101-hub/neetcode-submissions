class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in nums:
            if target - i == i and nums.count(i) > 1:
                print("flag1")
                flag = 1
                break
            elif target - i == i:
                continue
            elif target - i in nums:
                print("flag2")
                flag = 2
                break
        print(i,target-i)
        if flag == 1:
            for i in range(len(nums)):
                if nums[i] == target // 2: l.append(i)
        else:
            for j in range(len(nums)):
                if nums[j] == target - i or nums[j] == i:
                    l.append(j)
        return l