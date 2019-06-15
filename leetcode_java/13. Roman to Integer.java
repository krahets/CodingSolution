import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<Character, Integer> roman = new HashMap<Character, Integer>() {
        {
            put('M', 1000);
            put('D', 500);
            put('C', 100);
            put('L', 50);
            put('X', 10);
            put('V', 5);
            put('I', 1);
        }
    };

    public int romanToInt(String s) {
        int res = 0, pre = 0;
        for(Character c : s.toCharArray()){
            int cur = roman.get(c);
            res += cur > pre ? cur - 2 * pre : cur;
            pre = cur;
        }
        return res;
    }
}