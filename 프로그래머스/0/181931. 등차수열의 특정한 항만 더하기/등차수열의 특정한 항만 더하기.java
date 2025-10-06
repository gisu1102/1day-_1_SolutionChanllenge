class Solution {
    public int solution(int a, int d, boolean[] included) {
        //a +d(n) 등차수열
        //included[i]-> i+1 항
        int len = included.length;
        int[] arr = new int[len];//배열 생성
        
        int answer = 0 ;
        for (int i=0; i<len; i++) {
            if (included[i] == true) {
                answer+=(a+d*i);
            }
        }
        
        return answer;
    }
}