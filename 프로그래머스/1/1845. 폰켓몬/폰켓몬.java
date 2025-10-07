import java.util.*;

class Solution {
    public int solution(int[] nums) {
        
        //N -> 2/N
        //종류에 따라 번호
        //2/N 뽑기(조합) -> 가장 많은 종류 선택하는 방법 -> 종류번호의 개수
        
        int n = nums.length;
        int pick = n/2;
        int answer = 0;
        
        Set<Integer> kinds = new HashSet<>();
        for (int x : nums) kinds.add(x);
        
        answer = Math.min(kinds.size(), pick);
        
        return answer;
    }
}