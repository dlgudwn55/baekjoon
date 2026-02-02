import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	    int n = Integer.parseInt(br.readLine());

	    for (int b = 1; b <= n; b++) {
	        int[] arr = new int[n - 1];
            for (int num = 1; num <= b - 1; num++) {
                arr[num - 1] = num;
            }
            for (int num = b + 1; num <= n; num++) {
                arr[num - 2] = num;
	        }

    	    for (int c = b - 1; c < (b - 1) + (n - 1) / 2; c++) {
	    	    System.out.println(b + " " + arr[c % (n - 1)]);
	        }
	    }
    }
}