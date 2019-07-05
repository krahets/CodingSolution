class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        self.res = []
        self.swap(nums, 0)
        return self.res

    def swap(self, nums, j):
        if j == len(nums) - 1: self.res.append(list(nums))
        for i in range(j, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.swap(nums, j+1)
            nums[i], nums[j] = nums[j], nums[i]
