class Solution {
    public double solution(int[] numbers) {
        float tmp = 0;
        for(int i = 0; i < numbers.length; i++){
            tmp += numbers[i];
        }
        
        return tmp / numbers.length;
    }
}