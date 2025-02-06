import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        if (Arrays.stream(d).sum() <= budget) return d.length;
        
        Arrays.sort(d);

        int answer = 0;
        for(int e:d){
            budget -= e;
            if (budget >= 0) answer++;
            else break;
        }
        
        return answer;
    }
}