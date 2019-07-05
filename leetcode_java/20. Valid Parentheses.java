import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {
    private static final Map<Character,Character> map = new HashMap<Character,Character>(){{
        put('{','}'); put('[',']'); put('(',')');
    }};
    public boolean isValid(String s) {
        if(s.length() > 0 && !map.containsKey(s.charAt(0))) return false;
        Stack<Character> stack = new Stack<>();
        for(Character c : s.toCharArray()){
            if(stack.isEmpty() || map.containsKey(c)) stack.push(c);
            else if(map.get(stack.peek()) == c) stack.pop();
            else return false;
        }
        return stack.isEmpty();
    }
}