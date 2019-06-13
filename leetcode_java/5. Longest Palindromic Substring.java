class Solution {
    public String longestPalindrome(String s) {
        if(s.length() == 0) return "";
        int left = 0, right = 0;
        for (int i = 0; i < s.length(); i++) {
            int odd = midExpand(s, i, i);
            int even = midExpand(s, i, i + 1);
            int m = Math.max(odd, even);
            if (m > right - left) {
                left = i - (m - 1) / 2;
                right = i + m / 2;
            }
        }
        return s.substring(left, right + 1);
    }

    private int midExpand(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}