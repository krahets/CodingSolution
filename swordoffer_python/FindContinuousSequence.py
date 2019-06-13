# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res, l, r, s = [], 1, 2, 3
        while l < r:
            if s >= tsum: 
                if s == tsum: res.append(list(range(l,r+1)))
                s -= l
                l += 1
            else: 
                r += 1
                s += r
        return res

    def FindContinuousSequence_1(self, tsum):
        # write code here
        res, key = [], 0.5
        for d in range(int((2*tsum) ** 0.5), 1, -1):
            tmp = tsum / d
            tmp_int = int(tmp)
            if tmp - tmp_int == key:
                if key == 0.5: left, right = -int(d/2 - 1), int(d/2 + 1)
                else: left, right = -int(d/2), int(d/2 + 1)
                res.append(list(range(tmp_int + left, tmp_int + right)))
            key = 0.5 if not key else 0
        return res





s = Solution()
print(s.FindContinuousSequence(1))
print(s.FindContinuousSequence(3))
print(s.FindContinuousSequence(100))

