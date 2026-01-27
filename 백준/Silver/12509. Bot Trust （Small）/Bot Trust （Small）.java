import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	int t = Integer.parseInt(br.readLine());
	for (int testNo = 1; testNo <= t; testNo++) {
	    String line = br.readLine().trim();
	    String[] tokens = line.split("\\s+");
	    int n = Integer.parseInt(tokens[0]);

	    String[] r = new String[n];
	    int[] p = new int[n];
	    for (int i = 1; i < tokens.length; i += 2) {
		r[i / 2] = tokens[i];
		p[i / 2] = Integer.parseInt(tokens[i + 1]);
	    }

	    int blue = 1;
	    int orange = 1;
	    int pressCount = 0;
	    int time = 0;

	    while (pressCount < n) {
		int idxBlue = -1;
		int idxOrange = -1;
		pressCount += 1;

		for (int i = pressCount - 1; i < n; i++) {
		    if (r[i].equals("B")) {
			idxBlue = i;
			break;
		    }
		}
		for (int i = pressCount - 1; i < n; i++) {
		    if (r[i].equals("O")) {
			idxOrange = i;
			break;
		    }
		}

		// 남은 O가 없고 B만 남은 경우
		if (idxOrange == -1) {
		    int button = p[idxBlue];
		    time += Math.abs(blue - button) + 1;
		    blue = button;
		    continue;
		}

		// 남은 B가 없고 O만 남은 경우
		if (idxBlue == -1) {
		    int button = p[idxOrange];
		    time += Math.abs(orange - button) + 1;
		    orange = button;
		    continue;
		}

		int blueButton = p[idxBlue];
		int orangeButton = p[idxOrange];

		// blue가 orange보다 먼저 버튼 눌러야 할 때
		if (idxBlue < idxOrange) {
		    if (Math.abs(blue - blueButton) < Math.abs(orange - orangeButton)) {
			if (orange < orangeButton)
			    orange = orange + Math.abs(blue - blueButton) + 1;
			else
			    orange = orange - Math.abs(blue - blueButton) - 1;
		    } else {
			orange = orangeButton;
		    }
		    time += Math.abs(blue - blueButton) + 1;
		    blue = blueButton;
		}
		// orange 가 blue보다 먼저 버튼 눌러야 할 때
		else {
		    if (Math.abs(blue - blueButton) > Math.abs(orange - orangeButton)) {
			if (blue < blueButton)
			    blue = blue + Math.abs(orange - orangeButton) + 1;
			else
			    blue = blue - Math.abs(orange - orangeButton) - 1;
		    } else {
			blue = blueButton;
		    }
		    time += Math.abs(orange - orangeButton) + 1;
		    orange = orangeButton;
		}
	    }
	    System.out.println("Case #" + testNo + ": " + time);
	}
    }
}