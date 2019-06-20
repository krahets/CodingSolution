import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (map.containsKey(target - x)) {
                return new int[] { map.get(target - x), i };
            }
            map.put(x, i);
        }
        return new int[] { 0, 0 };
    }
}

// class Main {
//     public static void main(String[] args) {
//         // Create a new Solution instance
//         Solution solution = new Solution();
//         // Create a test case
//         int[] nums = new int[] { 2, 3, 7, 11, 15 };
//         // Get the answer
//         int[] answer = solution.twoSum(nums, 9);
//         // Print the answer
//         System.out.print(answer[0]);
//         System.out.print(answer[1]);
//     }
// }