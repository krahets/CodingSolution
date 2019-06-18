import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {
    private static final Map<Character,Character> map = new HashMap<Character,Character>(){{
        put('{','}'); put('[',']'); put('(',')');
    }};
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(Character c : s.toCharArray()){
            if(!stack.isEmpty() && map.containsKey(stack.peek()) && map.get(stack.peek()) == c){
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}