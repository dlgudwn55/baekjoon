import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int t = Integer.parseInt(br.readLine());

	for (int i = 0; i < t; i++) {
	    BigInteger n = new BigInteger(br.readLine().trim());
	    System.out.println(calculate(n));
	}
    }

    public static BigInteger calculate(BigInteger n) {
	BigInteger plusOne = n.add(BigInteger.valueOf(1));
	BigInteger plusTwo = n.add(BigInteger.valueOf(2));
	
	BigInteger term = n.multiply(plusOne).multiply(plusTwo).divide(BigInteger.valueOf(6));
	return term.multiply(term);
    }
}