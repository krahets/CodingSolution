class Solution:
    def minPatches(self, nums: [int], n: int) -> int:
        add, i, count = 1, 0, 0
        while add <= n:
            if i < len(nums) and nums[i] <= add:
                add += nums[i]
                i += 1
            else:
                add += add
                count += 1
        return count


s = Solution()
s.minPatches([1,2,3,8], 80)