# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return self.findLocation(data, k + 0.1) - self.findLocation(data, k - 0.1)

    def findLocation(self, data, k):
        left, right = 0, len(data) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if data[mid] > k: right = mid - 1
            else: left = mid + 1
        return left


s = Solution()
print(s.GetNumberOfK([1,2,3,3,3,3,4,5],6))
