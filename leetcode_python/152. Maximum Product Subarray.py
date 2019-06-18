class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mi = ma = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0: mi, ma = ma, mi
            ma = ma * nums[i]
            mi = mi * nums[i]
            res = max(res, ma)
        return res 
