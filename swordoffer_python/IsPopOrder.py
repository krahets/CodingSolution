# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        imi = [pushV.pop(0)]
        while imi:
            cur = popV.pop(0)
            while imi[-1] != cur:
                if not pushV: return False
                imi.append(pushV.pop(0))
            imi.pop()
        return True

s = Solution()
s.IsPopOrder([1,2,3,4,5],[3,2,5,4,1])