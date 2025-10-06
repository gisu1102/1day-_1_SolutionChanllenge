import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        //queue 에 다리위의 무게, 대기시간 삽입
        //다리위트럭 무게 + 대기트럭 무개 <= weight -> 큐에 삽입 아니면 대기
        //대기+ 다리 모두 empty -> 종료
        
        Deque<int[]> onBridge = new ArrayDeque<>();
        
        int time = 0;
        int idx=0;
        int curWeight=0;
        
        while( idx < truck_weights.length || !onBridge.isEmpty()) {
            time++;
            if (!onBridge.isEmpty() && onBridge.peekFirst()[1] == time ) {
                curWeight -= onBridge.poll()[0];
            }
            if (idx < truck_weights.length) {
                int nextWeight = truck_weights[idx];
                if(curWeight + nextWeight <= weight && onBridge.size()<=bridge_length){
                    curWeight += nextWeight;
                    onBridge.offer(new int[]{nextWeight, time+bridge_length});
                    idx++;
                }
            }
            
        }
        
        return time;
    }
}