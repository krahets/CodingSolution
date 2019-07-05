class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        children(nums, 0, res, new ArrayList<>());
        return res;
    }
    private void children(int[] nums, int j, List<List<Integer>> res, List<Integer> tmp) {
        res.add(new ArrayList<>(tmp));
        for(int i = j; i < nums.length; i++){
            tmp.add(nums[i]);
            children(nums, i + 1, res, tmp);
            tmp.remove(tmp.size() - 1);
        }
    }
}