import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String[] c : clothes){
            
            String name = c[0];
            String kind = c[1];
            map.put(kind,map.getOrDefault(kind,0) +1);
        }
        int comb = 1;
        
        for (int cnt : map.values()) {
            comb *= (cnt+1);
        }
        return comb-1;
        
    }
}