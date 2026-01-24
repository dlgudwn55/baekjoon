import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int n = Integer.parseInt(br.readLine());

	String givenString = br.readLine().trim();
	String longToL = givenString.replace("long", "L");

	int[] fibo = generateFibonacci(80);
	List<Integer> lCountList = getLCountList(longToL);
	
	int ans = 1;
	for (int lCount : lCountList)
	    ans *= fibo[lCount];
	
	System.out.println(ans);
    }

    public static int[] generateFibonacci(int maxN) {
	int[] fibo = new int[maxN+1];
	fibo[0] = 1;
	fibo[1] = 1;
	for (int i = 2; i <= maxN; i++)
	    fibo[i] = fibo[i-1] + fibo[i-2];
	
	return fibo;
    }
    
    public static List<Integer> getLCountList(String givenString) {
	int n = givenString.length();
	List<Integer> lCountList = new ArrayList<>();
	
	int count = 0;
	for (int i = 0; i < n; i++) {
	    if (givenString.charAt(i) == 'L')
		count++;
	    else {
		lCountList.add(count);
		count = 0;
	    }
	}
	lCountList.add(count);
	
	return lCountList;
    }
}