class Solution {
    public String solution(String str1, String str2) {
        StringBuilder sb = new StringBuilder();
        
        char[] chr1 = str1.toCharArray();
        char[] chr2 = str2.toCharArray();

        
        for (int i=0; i<str1.length(); i++) {
            sb.append(chr1[i]);
            sb.append(chr2[i]);
        }
        
    
        return sb.toString();
    }
}