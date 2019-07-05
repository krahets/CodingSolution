class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        res = float("inf")
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]: continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                tmp = nums[k] + nums[i] + nums[j]
                if abs(tmp - target) < abs(res - target): res = tmp
                if tmp > target: j -= 1
                elif tmp < target: i += 1
                else: return target
        return res