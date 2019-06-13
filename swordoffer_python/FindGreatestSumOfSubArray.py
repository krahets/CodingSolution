# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        tmp = [array[0]]
        for i in range(1, len(array)):
            tmp += [array[i]] if tmp[i-1] < 0 else [array[i] + tmp[i-1]]
        return max(tmp)


s = Solution()
s.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5])
