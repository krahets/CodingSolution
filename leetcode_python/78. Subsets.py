class Solution(object):
    def subsets(self, nums):
        res = []
        def children(j, tmp):
            res.append(tmp)
            for i in range(j, len(nums)):
                children(i + 1, tmp + [nums[i]])
        children(0, [])
        return res

class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        res = [[]]
        for num in nums:
            res += [r + [num] for r in res]
        return res

s = Solution()
s.subsets([1,2,3,4,5])