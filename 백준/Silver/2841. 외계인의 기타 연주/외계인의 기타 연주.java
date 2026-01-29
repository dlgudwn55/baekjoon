import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int ans = 0;
	
	String line = br.readLine().trim();
	String[] tokens = line.split("\\s+");
	int n = Integer.parseInt(tokens[0]);
	int p = Integer.parseInt(tokens[1]);
	
	int[] ropes = new int[n];
	int[] frets = new int[n];
	
	for (int i = 0; i < n; i++) {
	    line = br.readLine().trim();
	    tokens = line.split("\\s+");
	    int rope = Integer.parseInt(tokens[0]);
	    int fret = Integer.parseInt(tokens[1]);
	    ropes[i] = rope;
	    frets[i] = fret;
	}
	
	Map<Integer, List<Integer>> stackMap = new HashMap<>();
	for (int i = 0; i < n; i++) {
//	    System.out.println(stackMap.get(ropes[i]));
	    if (stackMap.get(ropes[i]) == null) {
		stackMap.put(ropes[i], new ArrayList<>());
		stackMap.get(ropes[i]).add(frets[i]);
		ans++;
		continue;
	    }
	    
	    if (stackMap.get(ropes[i]).size() == 0) {
		stackMap.get(ropes[i]).add(frets[i]);
		ans++;
		continue;
	    }
	    int topFret = stackMap.get(ropes[i]).get(stackMap.get(ropes[i]).size() - 1);
	    if (frets[i] == topFret) {
		continue;
	    } else if (frets[i] > topFret) {
		stackMap.get(ropes[i]).add(frets[i]);
		ans++;
	    } else {
		while (stackMap.get(ropes[i]).size() > 0 && stackMap.get(ropes[i]).get(stackMap.get(ropes[i]).size() - 1) > frets[i]) {
//		    stackMap.get(ropes[i]).removeLast();
		    stackMap.get(ropes[i]).remove(stackMap.get(ropes[i]).size() - 1);
		    ans++;
		}
		if (stackMap.get(ropes[i]).size() == 0 || stackMap.get(ropes[i]).get(stackMap.get(ropes[i]).size() - 1) < frets[i]) {
		    stackMap.get(ropes[i]).add(frets[i]);
		    ans++;
		}
	    }
//	    System.out.println(stackMap.toString());
	}
	System.out.println(ans);
    }
}