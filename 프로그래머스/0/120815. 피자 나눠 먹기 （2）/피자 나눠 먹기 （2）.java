class Solution {
    public int solution(int n) {
        // 1판 -> 6조각
        // 6*x % n == 0
        // 총 조각 % n == 0
        // 인당 조각 수 = 6,n의 최대 공약수
        
        int answer = n / getGCD(n, 6);
        
        return answer;
    }
    private int getGCD(int a, int b) {
        while(b != 0){
            int tmp= a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}