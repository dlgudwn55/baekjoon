import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	String line = br.readLine();
	String[] tokens = line.split("\\s+");
	int n = Integer.parseInt(tokens[0]);
	int k = Integer.parseInt(tokens[1]);

	int[] a = new int[n];
	for (int i = 0; i < n; i++) {
	    a[i] = Integer.parseInt(br.readLine());
	}

	int curr = 0;
	for (int i = 0; i < k; i++) {
	    curr += a[i];
	}

	int ans = curr;
	for (int i = 1; i < n - k + 1; i++) {
	    curr -= a[i - 1];
	    curr += a[i + k - 1];
	    ans = Math.max(ans, curr);
	}

	System.out.println(ans);
    }
}