class Solution {
    public int search(int[] nums, int target) {
        if(nums.length == 0) return -1;
        int i = 0, j = nums.length - 1;
        while(i < j){
            int m = (i + j) / 2;
            if(nums[m] < nums[j]) j = m;
            else i = m + 1;
        }
        if(i == 0 || nums[i] <= target && target <= nums[nums.length - 1])
            j = nums.length - 1;
        else if(nums[0] <= target && target <= nums[i - 1]){
            j = i - 1;
            i = 0;
        }
        else return -1;
        while(i <= j) {
            int m = (i + j) / 2;
            if(nums[m] < target) i = m + 1;
            else if(nums[m] > target) j = m - 1;
            else return m;
        }
        return -1;
    }
}