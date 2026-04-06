import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        int[] c = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            c[i] = Integer.parseInt(st.nextToken());
        }

        int[] nodes = new int[n];
        for (int i = 0; i < n; i++) {
            nodes[i] = c[i];
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            int k = Integer.parseInt(br.readLine());

            if (k < v) {
                sb.append(nodes[k]).append("\n");
            } else {
                int idx = (k - v + 1) % (n - v + 1) + (v - 1);
                sb.append(nodes[idx]).append("\n");
            }
        }

        System.out.print(sb);
    }
}