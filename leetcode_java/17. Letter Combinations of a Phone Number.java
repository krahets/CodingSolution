class Solution {
    private Map<Character, char[]> map = new HashMap<Character, char[]>() {{ 
        put('1', new char[] {});
        put('2', new char[] {'a', 'b', 'c'});
        put('3', new char[] {'d', 'e', 'f'});
        put('4', new char[] {'g', 'h', 'i'});
        put('5', new char[] {'j', 'k', 'l'});
        put('6', new char[] {'m', 'n', 'o'});
        put('7', new char[] {'p', 'q', 'r', 's'});
        put('8', new char[] {'t', 'u', 'v'});
        put('9', new char[] {'w', 'x', 'y', 'z'});
    }};
    List<String> res = new ArrayList<String>();
    StringBuilder tmp  = new StringBuilder();
    public List<String> letterCombinations(String digits) {
        if(digits.length() == 0) {
            if(tmp.length() > 0) res.add(tmp.toString());
            return res;
        }
        for(char letter : map.get(digits.charAt(0))) {
            tmp.append(letter);
            letterCombinations(digits.substring(1));
            tmp.deleteCharAt(tmp.length() - 1);
        }
        return res;
    }
}