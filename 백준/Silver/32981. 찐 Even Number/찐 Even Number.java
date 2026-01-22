import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static final int DIV = 1000000007;
    
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	String firstLine = br.readLine();
	int q = Integer.parseInt(firstLine);

	for (int i = 0; i < q; i++) {
	    String line = br.readLine();
	    int n = Integer.parseInt(line);

	    if (n == 1) {
		System.out.println(5);
		continue;
	    }
	    if (n == 2) {
		System.out.println(20);
		continue;
	    }
	    System.out.println(4 * recursivePower(5, n - 1) % DIV);
	}
    }

    public static long recursivePower(long a, int n) {
	if (n == 0)
	    return 1;

	if (n % 2 == 0) {
	    long halfPower = recursivePower(a, n / 2);
	    return halfPower * halfPower % DIV;
	} else {
	    long halfPower = recursivePower(a, n / 2);
	    return halfPower * halfPower * a % DIV;
	}

    }
}