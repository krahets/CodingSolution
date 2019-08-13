class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[][] adjacency = new int[numCourses][numCourses];
        int[] indegrees = new int[numCourses];
        for(int[] cp : prerequisites) {
            indegrees[cp[0]]++;
            adjacency[cp[1]][cp[0]] = 1;
        }
        LinkedList<Integer> queue = new LinkedList<>();
        for(int i = 0; i < numCourses; i++){
            if(indegrees[i] == 0) queue.addLast(i);
        }
        while(!queue.isEmpty()) {
            int pre = queue.removeFirst();
            numCourses--;
            for(int cur = 0; cur < adjacency.length; cur++) {
                if(adjacency[pre][cur] == 1 && --indegrees[cur] == 0)
                    queue.add(cur);
            }
        }
        return numCourses == 0;
    }
}

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[][] adjacency = new int[numCourses][numCourses];
        int[] flags = new int[numCourses];
        for(int[] cp : prerequisites)
            adjacency[cp[1]][cp[0]] = 1;
        for(int i = 0; i < numCourses; i++){
            if(!dfs(adjacency, flags, i)) return false;
        }
        return true;
    }
    private boolean dfs(int[][] adjacency, int[] flags, int i) {
        if(flags[i] == 1) return false;
        if(flags[i] == -1) return true;
        flags[i] = 1;
        for(int j = 0; j < adjacency.length; j++) {
            if(adjacency[i][j] == 1 && !dfs(adjacency, flags, j)) return false;
        }
        flags[i] = -1;
        return true;
    }
}