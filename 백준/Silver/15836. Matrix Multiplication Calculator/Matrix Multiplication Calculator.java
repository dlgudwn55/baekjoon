import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int m, n, p, q;
	int caseNo = 0;
	while (true) {
	    // 행렬 크기 입력
	    String line = br.readLine();
	    String[] parts = line.trim().split("\\s+");
	    m = Integer.parseInt(parts[0]);
	    n = Integer.parseInt(parts[1]);
	    p = Integer.parseInt(parts[2]);
	    q = Integer.parseInt(parts[3]);

	    if (m == 0 && n == 0 && p == 0 && q == 0)
		break;

	    caseNo++;

	    long[][] a = new long[m][n];
	    long[][] b = new long[p][q];

	    // 행렬 A 원소 입력
	    for (int i = 0; i < m; i++) {
		String row = br.readLine();
		String[] items = row.trim().split("\\s+");
		for (int j = 0; j < n; j++) {
		    a[i][j] = Long.parseLong(items[j]);
		}
	    }
	    // 행렬 B 원소 입력
	    for (int i = 0; i < p; i++) {
		String row = br.readLine();
		String[] items = row.trim().split("\\s+");
		for (int j = 0; j < q; j++) {
		    b[i][j] = Long.parseLong(items[j]);
		}
	    }

	    // === 행렬 곱 계산 ===
	    // 행렬 크기 확인
	    if (n != p) {
		System.out.println("Case #" + caseNo + ":");
		System.out.println("undefined");
		continue;
	    }
	    long[][] c = new long[m][q];
	    for (int i = 0; i < m; i++) {
		for (int j = 0; j < q; j++) {
		    for (int k = 0; k < n; k++) {
			c[i][j] += a[i][k] * b[k][j];
		    }
		}
	    }
	    // 결과 출력
	    System.out.println("Case #" + caseNo + ":");
	    for (int i = 0; i < m; i++) {
		System.out.print("| ");
		for (int j = 0; j < q; j++) {
		    System.out.print(c[i][j] + " ");
		}
		System.out.println("|");
	    }
	}
    }
}
