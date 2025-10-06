import java.util.*; 

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        int n = progresses.length;
        int[] days = new int[n];
        
        for (int i=0; i<n; i++) {
            int remain = 100-progresses[i];
            days[i] = (int)Math.ceil((double)remain/speeds[i]);
        }
        
        List<Integer> group = new ArrayList<>();
        int current = days[0];
        int cnt = 1;
        for (int i=1; i<n; i++) {
            if (days[i]<=current){
                cnt++;
            } else {
                group.add(cnt);
                cnt = 1;
                current = days[i];
            }
        }
        
        group.add(cnt);
        
        int[] answer = new int[group.size()];
        for(int i=0; i<group.size(); i++) {
            answer[i] = group.get(i);
        }
        
        return answer;
        
    
    }
}