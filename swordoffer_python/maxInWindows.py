# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        queue, res = [], []
        for i in range(len(num)):
            while queue and num[queue[-1]] <= num[i]: queue.pop()
            while queue and queue[0] <= i - size: queue.pop(0)
            queue.append(i)
            if size and i + 1 >= size: res.append(num[queue[0]])
        return res


s = Solution()
s.maxInWindows([1,3,2,4,7,6],2)