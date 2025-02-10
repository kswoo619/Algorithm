class Solution {
    public String solution(String s) {
        char[] ss = s.toCharArray();
        int idx = 0;

        for(int i = 0; i < ss.length; i++){
            if (ss[i] == ' ') idx = 0;
            else{
                ss[i] = (idx % 2 == 0 ? Character.toUpperCase(ss[i]):Character.toLowerCase(ss[i]));
                idx++;
            }
        }
    return String.valueOf(ss);
    }
}