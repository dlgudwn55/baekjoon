import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedHashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 4; i++) {
            String line = br.readLine();
            if (line != null) {
                sb.append(line);
            }
        }
        String input = sb.toString();

        Map<Character, Integer> countMap = new LinkedHashMap<>();
        for (char c = 'A'; c <= 'Z'; c++) {
            countMap.put(c, 0);
        }

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c >= 'A' && c <= 'Z') {
                countMap.put(c, countMap.get(c) + 1);
            }
        }

        int maxFreq = 0;
        for (int v : countMap.values()) {
            maxFreq = Math.max(maxFreq, v);
        }

        char[][] ans = new char[maxFreq + 1][51];

        for (int i = 0; i <= maxFreq; i++) {
            for (int j = 0; j < 51; j++) {
                ans[i][j] = ' ';
            }
        }

        for (int i = 0; i < 26; i++) {
            ans[maxFreq][i * 2] = (char) ('A' + i);
        }

        for (int i = 0; i < 26; i++) {
            int freq = countMap.get((char) ('A' + i));
            int col = i * 2;
            for (int r = 0; r < freq; r++) {
                ans[maxFreq - 1 - r][col] = '*';
            }
        }

        for (int i = 0; i <= maxFreq; i++) {
            int end = 50;
            while (end >= 0 && ans[i][end] == ' ') {
                end--;
            }

            if (end < 0) continue;

            for (int j = 0; j <= end; j++) {
                System.out.print(ans[i][j]);
            }
            System.out.println();
        }
    }
}
