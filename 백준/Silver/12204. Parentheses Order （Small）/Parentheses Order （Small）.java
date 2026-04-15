import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int t = Integer.parseInt(br.readLine());

        for (int tn = 1; tn <= t; tn++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            
            List<String> parSeqList = new ArrayList<>();
            
            generateParSeq(parSeqList, new StringBuilder(), n*2, 0);
            
            System.out.print("Case #" + tn + ": ");
            if (k > parSeqList.size()) {
                System.out.println("Doesn't Exist!");
            } else {
                System.out.println(parSeqList.get(k - 1));
            }
        }
        
        
    }

    static void generateParSeq(List<String> parSeqList, StringBuilder sb, int maxLength, int openParCount) {
	if (sb.length() == maxLength) {
	    if (openParCount == 0) {
		parSeqList.add(sb.toString());
	    }
	    return;
	}
	
	sb.append('(');
	generateParSeq(parSeqList, sb, maxLength, openParCount + 1);
	sb.deleteCharAt(sb.length() - 1);
	
	if (openParCount > 0) {
	    sb.append(')');
	    generateParSeq(parSeqList, sb, maxLength, openParCount - 1);
	    sb.deleteCharAt(sb.length() - 1);
	}
    }
}