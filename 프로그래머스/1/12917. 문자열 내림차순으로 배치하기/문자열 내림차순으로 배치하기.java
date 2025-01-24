import java.util.*;
class Solution {
    public String solution(String s) {
        char[] str = s.toCharArray();
        Arrays.sort(str);
        StringBuilder sb = new StringBuilder(String.valueOf(str));
        sb.reverse();

        return sb.toString();
    }
}