class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        int cnt = 0;
        for(int i=0; i < s.length(); i++){
            if (s.charAt(i) == 'p') cnt += 1;
            else if (s.charAt(i) == 'y') cnt -= 1;
        }
        if(cnt == 0){
            return true;
        }else{
            return false;
        }
    }
}