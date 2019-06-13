# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.matrix, self.k, self.rows, self.cols = \
        [[0 for _ in range(cols)] for _ in range(rows)], threshold, rows, cols
        return self.moving(0, 0)
    def moving(self, i, j):
        if not 0 <= i < self.rows or not 0 <= j < self.cols or \
        self.matrix[i][j] or self.k < self.sums(i) + self.sums(j):
            return 0
        self.matrix[i][j] = 1
        print([i,j])
        return 1 + self.moving(i+1, j) + self.moving(i-1, j) + self.moving(i, j+1) + self.moving(i, j-1) # still pass without self.moving(i, j-1).
    def sums(self, i):
        m = 0
        while i:
            i, b = i // 10, i % 10
            m += b
        return m


s = Solution()
print(s.movingCount(5, 10, 10))
