class Solution {
    public int minPatches(int[] nums, int n) {
        int i = 0, count = 0;
        long add = 1;
        while(add <= n){
            if(i < nums.length && nums[i] <= add) add += nums[i++];
            else {
                add += add;
                count ++;
            }
        }
        return count;
    }
}