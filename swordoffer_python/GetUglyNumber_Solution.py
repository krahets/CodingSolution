# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7: return index
        t2 = t3 = t5 = 0
        res = [1]
        for i in range(1,index):
            r2, r3, r5 = res[t2] * 2, res[t3] * 3, res[t5] * 5
            res.append(min([r2, r3, r5])) 
            if res[i] == r2: t2 += 1
            if res[i] == r3: t3 += 1
            if res[i] == r5: t5 += 1
        return res[-1]

s = Solution()
print(s.GetUglyNumber_Solution(8))