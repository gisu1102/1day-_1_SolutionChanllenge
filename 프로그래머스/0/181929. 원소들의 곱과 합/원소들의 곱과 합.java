class Solution {
    public int solution(int[] num_list) {
        
        int multi =1;
        int pow=0;
        for (int i=0; i<num_list.length; i++) {
            multi *= num_list[i];
            pow += num_list[i];
        }
        System.out.println(
        ", multi=" + multi 
        + ", pow=" + pow);
        
        return (multi<pow*pow) ? 1 : 0;
    }
}