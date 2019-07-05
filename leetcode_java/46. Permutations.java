class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> permute(int[] nums) {
        swap(nums, 0);
        return res;
    }
    private void swap(int[] nums, int j) {
        if (j == nums.length - 1) {
            List<Integer> list = new ArrayList<>();
            for (int num : nums) list.add(num);
            res.add(list);
        }
        for (int i = j; i < nums.length; i++) {
            int tmp = nums[i];
            nums[i] = nums[j]; nums[j] = tmp;
            swap(nums, j + 1);
            nums[j] = nums[i]; nums[i] = tmp;
        }
    }
}