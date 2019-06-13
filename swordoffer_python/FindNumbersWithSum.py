# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        l, r = 0, len(array) - 1
        while l < r:
            if array[l] + array[r] < tsum: l += 1
            elif array[l] + array[r] > tsum: r -= 1
            else: return [array[l], array[r]]
        return []


s = Solution()
print(s.FindNumbersWithSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
