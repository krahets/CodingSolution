class Solution557 {
    public String reverseWords(String s) {
        String[] strs = s.split(" ");
        StringBuffer res = new StringBuffer("");
        for(String str : strs){
            StringBuffer tmp = new StringBuffer(str);
            res.append(" ");
            res.append(tmp.reverse().toString());
        }
        return res.toString().trim();    
    }
}

// class Main {
//     public static void main(String[] args) {
//         // Create a new Solution instance
//         Solution557 solution = new Solution557();
//         // Get the answer
//         String s = "I am a boy";
//         String res = solution.reverseWords(s);
//         // Print the answer
//         System.out.print(res);
//     }
// }