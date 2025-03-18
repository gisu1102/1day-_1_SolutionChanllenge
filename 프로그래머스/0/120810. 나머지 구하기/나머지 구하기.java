class Solution {
    public int solution(int num1, int num2) {
        
        while (num1 >= num2) {
            num1 -=num2;
        }
        int answer = num1;
        return answer;
    }
}