import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> q = new LinkedList<>();
        
        for( int i=0; i<priorities.length; i++) {
            q.offer(new int[]{i,priorities[i]});
        }
        
        int order = 0;
        while(!q.isEmpty()){
            int[] current = q.poll();
            int idx = current[0];
            int priority = current[1];
            
            boolean hasHigher = false;
            for( int[] process : q) {
                if(process[1] > priority) {
                    hasHigher = true;
                    break;
                }
            }
            
            if (hasHigher) {
                q.offer(current);
            } else {
                order++;
                if (idx ==location) return order;
            }
        }
        
        return -1;
        
    }
}