class Solution {
    public String solution(String my_string, int k) {
        String answer = "";
        
        int i = 0;
        while (i < k){
            answer+=my_string;
            i++;
        }
        
        
        return answer;
    }
}