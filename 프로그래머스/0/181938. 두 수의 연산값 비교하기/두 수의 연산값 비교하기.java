class Solution {
    public int solution(int a, int b) {
        
        String sa = String.valueOf(a);
        String sab = String.valueOf(2*a*b);
        String sb = String.valueOf(b);
        
        int sum1 = Integer.parseInt(sa + sb);
        int sum2 = Integer.parseInt(sab);
    
        if (sum1<sum2){
            return sum2;
        } else {
            return sum1;
        }
    }
}