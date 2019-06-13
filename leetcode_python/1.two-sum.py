class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if str(target - nums[i]) in dic.keys():
                return [dic[str(target - nums[i])], i]
            if str(nums[i]) not in dic.items():
                dic[str(nums[i])] = i


s = Solution()
s.twoSum([2, 7, 11, 15], 9)
