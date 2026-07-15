import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;

        List<Character> st = new ArrayList<>();
        
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                st.add(c);
            } else {
                if (st.isEmpty()) {
                    return false;
                }
                st.remove(st.size()-1);
            }
        }
        
        return st.isEmpty();

        // return answer;
    }
}