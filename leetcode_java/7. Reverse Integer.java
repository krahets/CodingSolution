class Solution {
    public int reverse(int x) {
        int res = 0;
        int of = ((1 << 31) - 1) / 10;
        while (x != 0) {
            if (Math.abs(res) > ((1 << 31) - 1) / 10) return 0;
            res = res * 10 + x % 10;
            x /= 10;
        }
        return res;
    }
}


// class Main {
//     public static void main(String[] args) {
//         // Create a new Solution instance
//         Solution solution = new Solution();
//         // Get the answer
//         int answer = solution.reverse(-2147483412);
//         // Print the answer
//         System.out.print(answer);
//     }
// }