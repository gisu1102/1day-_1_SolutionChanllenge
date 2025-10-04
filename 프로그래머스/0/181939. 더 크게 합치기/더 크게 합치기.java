class Solution {
    public int solution(int a, int b) {
        String sa =  String.valueOf(a);
        String sb = String.valueOf(b);
        
        int ab = Integer.parseInt(sa + sb);
        int ba = Integer.parseInt(sb + sa);
        
        return Math.max(ab, ba);
    }
}