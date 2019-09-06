class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                if nums[j] != val: nums[i] = nums[j]
                j -= 1
            else: i += 1
        return j + 1