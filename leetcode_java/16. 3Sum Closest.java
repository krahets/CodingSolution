class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        long res = (long)Integer.MAX_VALUE;
        for (int k = 0; k < nums.length - 2; k++) {
            if(k > 0 && nums[k] == nums[k - 1]) continue;
            int i = k + 1, j = nums.length - 1;
            while(i < j) {
                int tmp = nums[k] + nums[i] + nums[j];
                if(Math.abs(tmp - target) < Math.abs(res - target)) res = tmp;
                if(tmp > target) while(i < j && nums[j] == nums[--j]);
                else if(tmp < target) while(i < j && nums[i] == nums[++i]);
                else return target;
            }
        }
        return (int)res;
    }
}