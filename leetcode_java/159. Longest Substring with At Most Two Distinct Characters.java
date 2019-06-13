class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int[] count = new int[256];
        int i = 0, numDistinct = 0, maxLen = 0;
        for (int j = 0; j < s.length(); j++) {
            if (count[s.charAt(j)] == 0) numDistinct++;
            count[s.charAt(j)]++;
            while (numDistinct > 2) {
                count[s.charAt(i)]--;
                if (count[s.charAt(i)] == 0) numDistinct--;
                i++;
            }
            maxLen = Math.max(maxLen, j - i + 1);
        }
        return maxLen;
    }
}