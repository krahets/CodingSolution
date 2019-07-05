class Solution(object):
    def subsets(self, nums):
        res = []
        def children(j, tmp):
            res.append(tmp)
            for i in range(j, len(nums)):
                children(i + 1, tmp + [nums[i]])
        children(0, [])
        return res