import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	String line = br.readLine();
	String[] parts = line.trim().split("\\s+");
	
	int m = Integer.parseInt(parts[0]);
	int t = Integer.parseInt(parts[1]);
	int u = Integer.parseInt(parts[2]);
	int f = Integer.parseInt(parts[3]);
	int d = Integer.parseInt(parts[4]);
	
	String[] s = new String[t];
	for (int i = 0; i < t; i++) {
	    s[i] = br.readLine().trim();
	}
	
	int[] reqTimes = new int[t];
	reqTimes[0] = s[0].equals("f") ? f * 2 : u + d;
	
	for (int i = 1; i < t; i++) {
	    int lapTime = s[i].equals("f") ? f * 2 : u + d;
	    reqTimes[i]= reqTimes[i-1] + lapTime; 
	}
	
	int ans = 0;
	for (int i = 0; i < t; i++) {
	    if (m < reqTimes[i]) break;
	    ans++;
	}
	System.out.println(ans);
    }
}