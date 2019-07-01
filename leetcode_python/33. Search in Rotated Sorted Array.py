class Solution:
    def search(self, nums: [int], target: int) -> int:
        if not nums: return -1
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] < nums[j]: j = m
            else: i = m + 1
        if nums[i] <= target <= nums[-1]: i, j = i, len(nums) - 1
        elif nums[0] <= target <= nums[i - 1]: i, j = 0, i - 1
        else: return -1
        while i <= j:
            m = (i + j) // 2
            if nums[m] > target: j = m - 1
            elif nums[m] < target: i = m + 1
            else: return m
        return -1