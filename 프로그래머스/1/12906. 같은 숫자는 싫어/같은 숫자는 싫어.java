import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int count=1;
        //count 세기
        for (int i=1; i<arr.length; i++) {
            if (arr[i] != arr[i-1]) {
                count++;
            }
        }
        
        int[] result = new int[count];
        result[0] = arr[0];
        
        int idx=1;
        for(int i=1; i<arr.length; i++) {
            if ( arr[i] !=arr[i-1] ){
                result[idx++] = arr[i];
            }
        }
        
        return result;
    }
}