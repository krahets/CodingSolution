# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = matrix.pop(0)
        while matrix:
            matrix = self.rotate(matrix)
            res += matrix.pop(0)
        return res

    def rotate(self, matrix):
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0])-1, -1, -1)]


s = Solution()
print(s.printMatrix([[1, 2], [3, 4]]))
