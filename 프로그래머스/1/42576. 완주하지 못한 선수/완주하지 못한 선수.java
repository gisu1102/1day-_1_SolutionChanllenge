import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        
        //단한명 제외 -> 한명만 제외
        //동명이인이 있을수있음
        
        Map<String, Integer> cnt = new HashMap<>();
        
        for (String par : participant) {
            cnt.put(par, cnt.getOrDefault(par,0) +1);
        }
        
        for (String com : completion) {
            cnt.put(com, cnt.get(com) -1);
        }
        
        for (Map.Entry<String, Integer> e : cnt.entrySet()){
            if(e.getValue()==1) return e.getKey();
        }
        
        return "false";
        
    }
}