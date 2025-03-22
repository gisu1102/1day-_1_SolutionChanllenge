import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        //오름차순 정렬
        //가운데 값 출력
        Arrays.sort(array);
        int answer = array[array.length/2];
        return answer;
    }
}