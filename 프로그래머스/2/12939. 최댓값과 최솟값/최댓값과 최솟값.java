// import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] strArr = s.split(" ");
        
        int[] intArr = new int[strArr.length];
        
        for (int i=0; i<strArr.length; i++) {
            intArr[i] = Integer.parseInt(strArr[i]);
        }
        
        int mn = intArr[0];
        int mx = intArr[0];
        
        for (int i=0; i<intArr.length; i++) {
            int cur = intArr[i];
            if (cur < mn) {
                mn = cur;
            }
            if (cur > mx) {
                mx = cur;
            }
        }
        
        return mn + " " + mx;
    }
}