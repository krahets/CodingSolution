class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        matrix = [[0 for _ in range(len(obstacleGrid[0])+1)] for _ in range(m+1)]
        matrix[0][1] = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] if obstacleGrid[i-1][j-1] != 1 else 0          
        return matrix[-1][-1]
