class Solution {
    public void reverseWords(char[] str) {
        int i = 0;
        for(int j = 0; j < str.length; j++){ // aTbTc
            if(str[j] != ' ') continue;
            reverse(str, i, j);
            i = j + 1;
        }
        reverse(str, i, str.length); // aTbTcT
        reverse(str, 0, str.length); // cba
    }
    private void reverse(char[] str, int i, int j){
        for(int k = i; k < (i + j) / 2; k++){
            char tmp = str[k];
            int g = j - 1 - k + i;
            str[k] = str[g];
            str[g] = tmp;
        }
    }
}