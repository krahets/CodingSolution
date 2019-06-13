# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n: return -1
        res = list(range(n))
        length, index = len(res), 0
        while length > 1:
            index = (index + m - 1) % length
            res.pop(index)
            length = len(res)
        return res[0]


s = Solution()
print(s.LastRemaining_Solution(10,3))