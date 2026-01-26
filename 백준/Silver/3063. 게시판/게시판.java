import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int t = Integer.parseInt(br.readLine().trim());
	for (int tn = 0; tn < t; tn++) {
	    String input = br.readLine().trim();
	    String[] tokens = input.split("\\s+");
	    int[] intTokens = new int[8];
	    
	    for (int i = 0; i < 8; i++) {
		// {x1, y1, x2, y2, x3, y3, x4, y4}
		intTokens[i] = Integer.parseInt(tokens[i]);
	    }
	    
	    int x5 = Math.max(intTokens[0], intTokens[4]);
	    int y5 = Math.max(intTokens[1], intTokens[5]);
	    int x6 = Math.min(intTokens[2], intTokens[6]);
	    int y6 = Math.min(intTokens[3], intTokens[7]);
	    
	    int myArea = (intTokens[2]-intTokens[0])*(intTokens[3]-intTokens[1]);
	    int coveredArea = 0;
	    if((x5 < x6) && (y5 < y6)) {
		coveredArea = (x6-x5)*(y6-y5);
	    }
	    System.out.println(myArea - coveredArea);
	}
    }
}