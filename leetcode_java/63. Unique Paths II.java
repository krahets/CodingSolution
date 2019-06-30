class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid.length == 0) return 0;
        int[][] matrix = new int[obstacleGrid.length + 1][obstacleGrid[0].length + 1];
        matrix[0][1] = 1;
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                matrix[i][j] = obstacleGrid[i - 1][j - 1] != 1 ? matrix[i - 1][j] + matrix[i][j - 1] : 0;
            }
        }
        return matrix[matrix.length - 1][matrix[0].length - 1];
    }
}