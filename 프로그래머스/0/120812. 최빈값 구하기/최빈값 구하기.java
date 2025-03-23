import java.util.*;

class Solution {
    public int solution(int[] array) {
        //값의 빈도 map 에 저장 (key= array_num, value = frequency)
        // 1. 배열 순회 
        // 2. map 에 해당 값 존재 유무 판단  
        // 2.a 존재 x 값 삽입 
        // 2.b 존재 o frequency ++
        // 3. map 에 중복 frequency 확인
        // 3.a 중복x= 해당 frequency 반환
        // 3.b 중복o = -1 반환
        
        int length = array.length;
        
        //map 자료형 생성
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int n : array){
            map.put(n, map.getOrDefault(n, 0) +1 );
        }
            
        //각 Map 요소 반복
        int count = 0;
        int mode = -1;
        boolean multiple = false;
            
        for (Map.Entry<Integer, Integer> entry : map.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
            // 최빈값 설정
            if (value > count){
                count = value;
                mode = key;
                multiple = false;
            } else if( value == count ){
                multiple = true;
            }
            
        }
        
        return multiple==false ? mode:-1;
    }
}