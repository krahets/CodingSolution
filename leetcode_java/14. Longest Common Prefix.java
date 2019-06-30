class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0) return "";
        int min = strs[0].length(), i = 0;
        for(String s : strs) min = Math.min(min, s.length());
        for(; i < min; i++) {
            for(int j = 0; j < strs.length - 1; j++){
                if(strs[j].charAt(i) != strs[j+1].charAt(i)) return strs[j].substring(0,i);
            }
        }
        return min > 0 ? strs[0].substring(0, i) : "";
    }
}