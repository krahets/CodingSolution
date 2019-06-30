class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1): # top triangle
            p *= nums[i]
            res.append(p)
        for i in range(len(nums) - 1, 0, -1): # bottom triangle
            q *= nums[i]
            res[i - 1] *= q
        return res

s = Solution()
s.productExceptSelf([1, 2, 3, 4])
