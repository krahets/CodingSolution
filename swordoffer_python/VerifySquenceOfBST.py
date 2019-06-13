# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        return self.verify(sequence) if sequence else False
    def verify(self, sequence):
        if not sequence: return True
        root = sequence[-1]
        left, right = [], []
        for i in range(len(sequence)):
            if sequence[i] >= root:
                d = i
                break
            left.append(sequence[i])
        for i in range(d, len(sequence)-1):
            if sequence[i] > root:
                right.append(sequence[i])
        if left + right + [root] != sequence: return False
        return self.verify(left) and self.verify(right)


s = Solution()
print(s.VerifySquenceOfBST([1, 2, 4, 3, 6, 8, 7, 5]))
