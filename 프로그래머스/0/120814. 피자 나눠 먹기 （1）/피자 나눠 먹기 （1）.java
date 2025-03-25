class Solution {
    public int solution(int n) {
        // n/7 n%7 = 
        
        int answer = 0;
        answer = n/7;
        if(n%7 == 0){
            return answer;
        } else {
            return answer+1;
        }
    }
}