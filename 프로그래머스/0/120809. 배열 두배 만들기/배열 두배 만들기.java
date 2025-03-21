class Solution {
    public int[] solution(int[] numbers) {
        /***
        *   1.배열길이 측정
        *   2.해당 배열 순회하며 각 원소 2배
        ***/
        int len = numbers.length;
        int[] answer = new int[len];
        
        for (int i=0; i<len; i++){
            answer[i] = numbers[i]*2; 
        }
        
        return answer;
    }
}