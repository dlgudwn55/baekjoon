import java.util.Arrays;
class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;

        Arrays.sort(A);
        
        Arrays.sort(B);
        
        for (int i=0; i<B.length/2; i++) {
            int tmp1 = B[i];
            int tmp2 = B[B.length-1-i];
            B[i] = tmp2;
            B[B.length-1-i] = tmp1;
        }
        
        for (int i=0; i<B.length; i++) {
            answer += A[i]*B[i];
        }

        return answer;
    }
}