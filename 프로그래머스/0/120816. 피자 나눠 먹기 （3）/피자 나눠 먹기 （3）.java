class Solution {
    public int solution(int slice, int n) {

        return (n + slice - 1) / slice;  // 올림 처리 공식
    }
}