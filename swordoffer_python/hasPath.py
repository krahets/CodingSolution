# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        self.flags = [0 for _ in range(len(matrix))]
        self.matrix, self.rows, self.cols, self.path = matrix, rows, cols, path
        for i in range(rows):
            for j in range(cols):
                if self.search(i, j, 0): return True
        return False

    def search(self, i, j, k):
        index = self.cols * i + j
        if not 0 <= i < self.rows or not 0 <= j < self.cols or \
        self.flags[index] or self.matrix[index] != self.path[k]:
            return False # 越界 or 已经走过 or 不是所需节点 
        if k == len(self.path) - 1:
            return True # 已经找完，不需要继续递归
        self.flags[index] = 1 # 走过这个点，寻找下个点
        if self.search(i+1, j, k+1) or self.search(i-1, j, k+1) or \
        self.search(i, j+1, k+1) or self.search(i, j-1, k+1):  
            return True # 四条路中有一条可以走通
        self.flags[index] = 0 # 如果无法走通，要释放这个点，以防影响其他路线中走此点
        return False


s = Solution()
print(s.hasPath("ABCESFCSADEE",3,4,"ABCCED"))

