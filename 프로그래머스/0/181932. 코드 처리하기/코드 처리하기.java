class Solution {
    public String solution(String code) {
        char[] ch_code = code.toCharArray();
        StringBuilder sb = new StringBuilder();
        int mode =0;
        for(int idx=0; idx<code.length(); idx++){
            if(ch_code[idx] == '1'){
                if(mode == 1) {
                    mode =0;
                    continue;
                }
                mode=1;
                continue;
            }
            
            if(mode == 0 && idx%2 ==0){
                sb.append(ch_code[idx]);
            } else if ( mode ==1 && idx%2 ==1){
                sb.append(ch_code[idx]);
            }
        }
        
        String answer = sb.toString();
        if (answer.isEmpty()){
            answer = "EMPTY";
        }
        return answer;
    }
}
