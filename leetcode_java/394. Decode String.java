import java.util.LinkedList;

// class Solution {
//     public String decodeString(String s) {
//         return dfs(s, 0)[0];
//     }
//     private String[] dfs(String s, int i) {
//         StringBuilder res = new StringBuilder();
//         int multi = 0;
//         while(i < s.length()) {
//             if(s.charAt(i) >= '0' && s.charAt(i) <= '9') 
//                 multi = multi * 10 + Integer.parseInt(String.valueOf(s.charAt(i))); 
//             else if(s.charAt(i) == '[') {
//                 String[] tmp = dfs(s, i + 1);
//                 i = Integer.parseInt(tmp[0]);
//                 while(multi > 0) {
//                     res.append(tmp[1]);
//                     multi--;
//                 }
//             }
//             else if(s.charAt(i) == ']') 
//                 return new String[] { String.valueOf(i), res.toString() };
//             else 
//                 res.append(String.valueOf(s.charAt(i)));
//             i++;
//         }
//         return new String[] { res.toString() };
//     } 
// }


class Solution {
    public String decodeString(String s) {
        StringBuilder res = new StringBuilder();
        int multi = 0;
        LinkedList<Integer> stack_multi = new LinkedList<>();
        LinkedList<String> stack_res = new LinkedList<>();
        for(Character c : s.toCharArray()) {
            if(c == '[') {
                stack_multi.addLast(multi);
                stack_res.addLast(res.toString());
                multi = 0;
                res = new StringBuilder();
            }
            else if(c == ']') {
                StringBuilder tmp = new StringBuilder();
                int cur_multi = stack_multi.removeLast();
                for(int i = 0; i < cur_multi; i++) tmp.append(res);
                res = new StringBuilder(stack_res.removeLast() + tmp);
            }
            else if(c >= '0' && c <= '9') multi = multi * 10 + Integer.parseInt(c + "");
            else res.append(c);
        }
        return res.toString();
    }
}