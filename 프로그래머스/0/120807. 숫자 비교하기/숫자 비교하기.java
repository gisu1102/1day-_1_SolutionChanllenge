class Solution {
    public int solution(int num1, int num2) {
        boolean Limit_Check = ((0<=num1 && num1<=10000) &&(0<=num2 && num2<=10000));
        if(num1==num2){
            return 1;
        }
        else return -1;
    }
}