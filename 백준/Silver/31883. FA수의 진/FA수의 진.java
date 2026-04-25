import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] trafficData = new int[N][4];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                trafficData[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        long time = 0;

        for (int i = 0; i < N; i++) {
            int crosswalk = trafficData[i][0];
            int bridge = trafficData[i][1];
            int green = trafficData[i][2];
            int red = trafficData[i][3];

            long cycle = green + red;
            boolean isGreen = time % cycle < green;

            if (isGreen) {
                time += Math.min(crosswalk, bridge);
            } else {
                long round = time / cycle;
                long timeToGreen = (round + 1) * cycle - time;
                time += Math.min(bridge, timeToGreen + crosswalk);
            }
        }

        System.out.println(time);
    }
}