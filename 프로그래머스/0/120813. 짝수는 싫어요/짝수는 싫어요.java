class Solution {
    public int[] solution(int n) {
        // 길이 가 n/2  반올림 한 배열 생성
        // 1~n 이하 홀수 채워넣기
        int[] answer = new int[(n+1)/2];
        int index = 0;
        for(int i=1; i<=n ; i++){
            if((i%2) != 0){
                answer[index]=i;
                index++;
            }
            
        }
        return answer;
    }
}