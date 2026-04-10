import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        Map<String, List<String>> data = new HashMap<>();
        Map<String, Integer> nameCounter = new HashMap<>();
        
        int q = Integer.parseInt(br.readLine());

        for (int i = 0; i < q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            String p = st.nextToken();
            
            data.putIfAbsent(s, new ArrayList<>());
            data.get(s).add(p);
        }
        
        int ans = 0;
        
        for (String name : data.keySet()) {
            List<String> history = data.get(name);
            
            for (String action : history) {
        	if (action.equals("+")) {
        	    nameCounter.put(name, nameCounter.getOrDefault(name, 0) + 1);
        	} else {
        	    if (nameCounter.getOrDefault(name, 0) == 0) {
        		ans++;
        	    } else {
        		nameCounter.put(name, nameCounter.get(name) - 1);
        	    }
        	}
            }
            
            ans += nameCounter.getOrDefault(name, 0);
        }
        
        System.out.println(ans);
    }
}