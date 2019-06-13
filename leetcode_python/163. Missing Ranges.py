class Solution:
    def findMissingRanges(self, nums: [int], lower: int, upper: int) -> [str]:
        res = []
        low = lower - 1
        nums.append(upper + 1)
        for num in nums:
            dif = num - low
            if dif == 2: res.append(str(low+1))
            elif dif > 2: res.append(str(low+1) + "->" + str(num-1))
            low = num
        return res


s = Solution()
print(s.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
