class Solution:
    def majorityElement(self, nums: [int]) -> int:
        count = 0
        for num in nums:
            if not count: res = num
            count += 1 if num == res else -1
        return res