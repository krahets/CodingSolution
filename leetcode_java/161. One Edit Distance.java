class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int dif = t.length() - s.length(), i = 0;
        if (dif < 0) return isOneEditDistance(t, s);
        if (dif > 1) return false;
        while (i < s.length() && s.charAt(i) == t.charAt(i)) i++;
        if (i == s.length()) return dif > 0;
        if (dif == 0) i++;
        while (i < s.length() && s.charAt(i) == t.charAt(i + dif)) i++;
        return i == s.length();
    }
}