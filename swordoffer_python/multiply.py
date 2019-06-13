# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B, tmp = [1], 1
        for i in range(len(A)-1):
            B.append(B[i]*A[i])
        for i in range(len(A)-1, 0, -1):
            tmp *= A[i]
            B[i-1] *= tmp
        return B


s = Solution()
print(s.multiply([1, 2, 3, 4, 5, 6]))
