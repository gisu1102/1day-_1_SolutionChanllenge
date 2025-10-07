import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
//         Arrays.sort(phone_book);
        
//         for (int i=0; i < phone_book.length -1; i++) {
//             String a = phone_book[i];
//             String b = phone_book[i+1];
            
//             if (b.length() >= a.length()){
//                 if(a.equals(b.substring(0,a.length()))) answer=false;
//             }
//         }

        HashSet<String> set = new HashSet<>();
        
        for (String s : phone_book) {
            set.add(s);
        }
        
        for (String num : phone_book) {
            for(int i=0; i < num.length(); i++){
                if (set.contains(num.substring(0, i))) {
                    return false;
                }
            }

        }
        
        return true;
    }
}