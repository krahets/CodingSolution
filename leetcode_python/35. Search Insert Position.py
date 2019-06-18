class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target: left = mid + 1
            else: right = mid - 1
        return left


s = Solution()
print(s.searchInsert([-8, -6, -2, 0, 1, 3, 5], 6))
