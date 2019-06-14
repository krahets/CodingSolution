class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix: return []
        res = []
        h, l = len(matrix), len(matrix[0])
        i, j = 0, -1
        while True:
            for _ in range(l):
                j += 1
                res.append(matrix[i][j])
            h -= 1
            if not h: break
            for _ in range(h):
                i += 1
                res.append(matrix[i][j])
            l -= 1
            if not l: break
            for _ in range(l):
                j -= 1
                res.append(matrix[i][j])
            h -= 1
            if not h: break
            for _ in range(h):
                i -= 1
                res.append(matrix[i][j])
            l -= 1
            if not l: break
        return res

s = Solution()
s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])