import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        int h = matrix.length, l = matrix[0].length;
        int i = 0, j = -1;
        while(true){
            for(int k = 0; k < l; k++)
                res.add(matrix[i][++j]);
            if(--h == 0) break;
            for(int k = 0; k < h; k++)
                res.add(matrix[++i][j]);
            if(--l == 0) break;
            for(int k = 0; k < l; k++)
                res.add(matrix[i][--j]);
            if(--h == 0) break;
            for(int k = 0; k < h; k++)
                res.add(matrix[++i][j]);
            if(--l == 0) break;
        }
        return res;
    }
}