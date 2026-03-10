import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static boolean checkPalindrome(String text) {
        int left = 0;
        int right = text.length() - 1;

        while (left < right) {
            if (text.charAt(left) != text.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

    public static boolean checkPseudoPalindrome(String text) {
        boolean isLeft = true;
        boolean isRight = true;

        int left = 0;
        int right = text.length() - 1;
        boolean flag = true;

        while (left < right) {
            if (text.charAt(left) != text.charAt(right)) {
                if (flag) {
                    left++;
                    flag = false;
                } else {
                    isLeft = false;
                    break;
                }
            } else {
                left++;
                right--;
            }
        }

        left = 0;
        right = text.length() - 1;
        flag = true;

        while (left < right) {
            if (text.charAt(left) != text.charAt(right)) {
                if (flag) {
                    right--;
                    flag = false;
                } else {
                    isRight = false;
                    break;
                }
            } else {
                left++;
                right--;
            }
        }

        return isLeft || isRight;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String strInput = br.readLine().trim();

            if (checkPalindrome(strInput)) {
                System.out.println(0);
            } else if (checkPseudoPalindrome(strInput)) {
                System.out.println(1);
            } else {
                System.out.println(2);
            }
        }
    }
}