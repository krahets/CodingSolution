class Solution:
    def findMin(self, nums: [int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: left = mid + 1
            else: right = mid
        return nums[left]



s = Solution()
print(s.findMin([3, 4, 1, 2]))
print(s.findMin([3, 1, 2]))
print(s.findMin([1, 2, 3]))
print(s.findMin([1, 2]))
print(s.findMin([2, 1]))
print(s.findMin([1]))



