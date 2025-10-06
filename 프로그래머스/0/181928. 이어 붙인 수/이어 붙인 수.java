class Solution {
    public int solution(int[] num_list) {
        
        int len = num_list.length;
        StringBuilder evenSb = new StringBuilder(len);
        StringBuilder oddSb = new StringBuilder(len);
        
        for (int i=0; i<len; i++) {
            if (num_list[i]%2 == 0){
                evenSb.append(num_list[i]);
            } else {
                oddSb.append(num_list[i]);
            }
        }
        int evenNum = Integer.parseInt(evenSb.toString());
        int oddNum = Integer.parseInt(oddSb.toString());
        
        return evenNum+oddNum;
    }
}