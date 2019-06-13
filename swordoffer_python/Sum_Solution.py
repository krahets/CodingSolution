# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        n and self.Sum_Solution(n-1)
        return self.sum + n

s = Solution()
s.Sum_Solution(10)