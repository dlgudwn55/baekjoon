import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int n = Integer.parseInt(br.readLine());

	int[] a = new int[n];
	String line = br.readLine();
	String[] tokens = line.trim().split("\\s+");

	for (int i = 0; i < n; i++) {
	    a[i] = Integer.parseInt(tokens[i]);	    
	}

	Arrays.sort(a);

	int[] right = new int[n];
	for (int i = n - 1; i >= 0; i--) {
	    if (i == n - 1) {
		right[i] = a[i];		
	    } else {
		right[i] = a[i] + right[i + 1];		
	    }
	}

//	for (int i = 0; i < n; i++)
//	    System.out.print(right[i] + " ");
//	System.out.println();

	long ans = 0;
	for (int i = 0; i < n - 1; i++) {
	    ans += a[i] * right[i + 1];	    
	}
	System.out.println(ans);
    }
}
