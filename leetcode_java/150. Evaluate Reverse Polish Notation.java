

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

class Solution {
    private static final Set<String> SYMBOLS = new HashSet<>(Arrays.asList("+","-","*","/"));
    
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String t : tokens){
            if(SYMBOLS.contains(t)){
                int y = stack.pop();
                int x = stack.pop();
                stack.push(eval(x, y, t));
            } else {
                stack.push(Integer.parseInt(t));
            }
        }
        return stack.peek();
    }

    private int eval(int x, int y, String symbol){
        switch(symbol){
            case "+": return x + y;
            case "-": return x - y;
            case "*": return x * y;
            default:  return x / y;
        }
    }
}